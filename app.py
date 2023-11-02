import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from preprocessing import preprocess_data


# Chargement des données prétraitées
train_data = pd.read_csv("data/Train_Data.csv")
test_data = pd.read_csv("data/Test_Data.csv")
X_train = train_data.drop("Satisfaction", axis=1)
X_test = test_data.drop("Satisfaction", axis=1)
y_train = train_data["Satisfaction"]
y_test = test_data["Satisfaction"]


prevision_df_tab, apprentissage_df_tab, dashboard_test_tab = st.tabs(['Prévision', 'Apprentissage', 'Test et ajout données'])

with prevision_df_tab:
    # Créer une application Streamlit
    st.title("Tableau de bord Prévision")

    # Créer le modèle Random Forest
    clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced')  

    # Entraîner le modèle
    clf.fit(X_train, y_train)

    # Prédire la satisfaction client
    def predict_satisfaction(features):
        prediction = clf.predict(features)
        return prediction

    # Interface utilisateur avec Streamlit
    st.title("Prédiction de la satisfaction client")
    st.write("Entrez les caractéristiques du client pour prédire sa satisfaction.")

    # Entrée des caractéristiques du client
    feature1 = st.slider("Caractéristique 1", min_value=0, max_value=10)
    feature2 = st.slider("Caractéristique 2", min_value=0, max_value=10)
    feature3 = st.slider("Caractéristique 3", min_value=0, max_value=10)
    feature4 = st.slider("Caractéristique 4", min_value=0, max_value=10)
    feature5 = st.slider("Caractéristique 5", min_value=0, max_value=10)
    feature6 = st.slider("Caractéristique 6", min_value=0, max_value=10)
    feature7 = st.slider("Caractéristique 7", min_value=0, max_value=10)
    feature8 = st.slider("Caractéristique 8", min_value=0, max_value=10)
    feature9 = st.slider("Caractéristique 9", min_value=0, max_value=10)
    feature10 = st.slider("Caractéristique 10", min_value=0, max_value=10)
    feature11 = st.slider("Caractéristique 11", min_value=0, max_value=10)
    feature12 = st.slider("Caractéristique 12", min_value=0, max_value=10)
    feature13 = st.radio("Caractéristique 13", ["Oui", "Non"])
    feature14 = st.radio("Caractéristique 14", ["Oui", "Non"])
    feature15 = st.radio("Caractéristique 15", ["Oui", "Non"])
    feature16 = st.radio("Caractéristique 16", ["Oui", "Non"])
    feature17 = st.radio("Caractéristique 17", ["Oui", "Non"])
    feature18 = st.radio("Caractéristique 18", ["Oui", "Non"])
    feature19 = st.radio("Caractéristique 19", ["Oui", "Non"])
    feature20 = st.radio("Caractéristique 20", ["Oui", "Non"])
    feature21 = st.radio("Caractéristique 21", ["Oui", "Non"])
    feature22 = st.radio("Caractéristique 22", ["Oui", "Non"])
    feature23 = st.radio("Caractéristique 23", ["Oui", "Non"])
    feature24 = st.radio("Caractéristique 24", ["Oui", "Non"])

    # Prédire la satisfaction client
    features = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10, feature11, feature12, feature13, feature14, feature15, feature16, feature17, feature18, feature19, feature20, feature21, feature22, feature23, feature24]]
    prediction = predict_satisfaction(features)

    # Afficher la prédiction
    st.write("La satisfaction client prédite est :", prediction)


with apprentissage_df_tab:
    # Créez une application Streamlit
    st.title("Tableau de bord pour l'apprentissage automatique")

    # Création et entraînement du modèle
    clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced')  
    clf.fit(X_train, y_train)

    # Prédiction sur l'ensemble de test
    y_pred = clf.predict(X_test)

    # Affichage de la précision du modèle
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f"Précision du modèle : {accuracy:.2f}")
    # Affichage du rapport de classification
    # print('y_test =', y_test)

    #####################A Developper
    # target_names = train_data.columns
    # report = classification_report(y_test, y_pred, target_names=train_data.columns)
    report = classification_report(y_test, y_pred)
    st.text("Rapport de classification :")
    st.text(report)

    # Affichage des données dans Streamlit
    st.header("Données d'entraînement et de test")
    st.write("Données d'entraînement :")
    # st.write(X_train)
    st.dataframe(X_train)

    st.write("Données de test :")
    # st.write(X_test)
    st.dataframe(X_test)

# # Affichage d'un graphique
# st.header("Graphique")
# st.bar_chart(data.data)

with dashboard_test_tab:
    # Créez une application Streamlit
    st.title("Tableau de bord Tests et nouvelles données")
        
    # Créez des onglets
    onglet_selectionne = st.radio("Sélectionnez type de fichier :", ("Fichier CSV", "Fichier Excel", "Fichier JSON"))

    # Onglet "Fichier CSV"
    if onglet_selectionne == "Fichier CSV":
        st.header("Lecture de données depuis un fichier CSV")

        file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
        if file is not None:
            data = pd.read_csv(file)
            result = preprocess_data(data,test_data, train_data)
            # X_train = result.
            # X_test = result.test_data
            # y_train = Preprocessing.y_train
            # y_test = Preprocessing.y_test
            # Affichez les données du fichier CSV
            r
            st.dataframe(data)
            if st.button("Lancer le modèle") :
                # Création et entraînement du modèle
                clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced')  
                clf.fit(X_train, y_train)
                # Prédiction sur l'ensemble de test
                y_pred = clf.predict(X_test)
                # Affichage de la précision du modèle
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Précision du modèle : {accuracy:.2f}")
                report = classification_report(y_test, y_pred)
                st.text("Rapport de classification :")
                st.text(report)
                # Affichage des données dans Streamlit
                st.header("Données d'entraînement et de test")
                st.write("Données d'entraînement :")
                # st.write(X_train)
                st.dataframe(X_train)
                st.write("Données de test :")
                # st.write(X_test)
                st.dataframe(X_test)

    # Onglet "Fichier Excel"
    elif onglet_selectionne == "Fichier Excel":
        st.header("Lecture de données depuis un fichier Excel")

        # Chargement des données depuis un fichier Excel
        file = st.file_uploader("Téléchargez un fichier Excel", type=["xlsx"])
        if file is not None:
            data = pd.read_excel(file)
            # Division des données en ensembles d'entraînement et de test
            Preprocessing(data)
            X_train, X_test, y_train, y_test = Preprocessing(X_train, X_test, y_train, y_test)

            # Affichez les données du fichier Excel
            st.dataframe(data)
            if st.button("Lancer le modèle") :
                # Création et entraînement du modèle
                clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced')  
                clf.fit(X_train, y_train)
                # Prédiction sur l'ensemble de test
                y_pred = clf.predict(X_test)
                # Affichage de la précision du modèle
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Précision du modèle : {accuracy:.2f}")
                report = classification_report(y_test, y_pred)
                st.text("Rapport de classification :")
                st.text(report)
                # Affichage des données dans Streamlit
                st.header("Données d'entraînement et de test")
                st.write("Données d'entraînement :")
                # st.write(X_train)
                st.dataframe(X_train)
                st.write("Données de test :")
                # st.write(X_test)
                st.dataframe(X_test)

    # Onglet "Fichier JSON"
    elif onglet_selectionne == "Fichier JSON":
        st.header("Lecture de données depuis un fichier JSON")

        # Chargement des données depuis un fichier JSON
        file = st.file_uploader("Téléchargez un fichier JSON", type=["json"])
        if file is not None:
            data = json.load(file)
            # Division des données en ensembles d'entraînement et de test
            X = data.drop("Satisfaction", axis=1)
            y = data["Satisfaction"]
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            # Affichez les données du fichier JSON
            st.json(data)
            if st.button("Lancer le modèle") :
                # Création et entraînement du modèle
                clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced')  
                clf.fit(X_train, y_train)
                # Prédiction sur l'ensemble de test
                y_pred = clf.predict(X_test)
                # Affichage de la précision du modèle
                accuracy = accuracy_score(y_test, y_pred)
                st.write(f"Précision du modèle : {accuracy:.2f}")
                report = classification_report(y_test, y_pred)
                st.text("Rapport de classification :")
                st.text(report)
                # Affichage des données dans Streamlit
                st.header("Données d'entraînement et de test")
                st.write("Données d'entraînement :")
                # st.write(X_train)
                st.json(X_train)
                st.write("Données de test :")
                # st.write(X_test)
                st.json(X_test)
        