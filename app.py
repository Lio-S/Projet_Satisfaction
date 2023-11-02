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
from preprocessing import Preprocessing


# Chargement des données prétraitées
train_data = pd.read_csv("data/Train_Data.csv")
test_data = pd.read_csv("data/Test_Data.csv")
X_train = train_data.drop("Satisfaction", axis=1)
X_test = test_data.drop("Satisfaction", axis=1)
y_train = train_data["Satisfaction"]
y_test = test_data["Satisfaction"]


# X = pd.DataFrame(train_data, columns=train_data.feature_names)
# y = pd.DataFrame(train_data)

# # Ajout de nouvelles données
# new_data = pd.DataFrame({"Flight Distance": [500], "Inflight wifi service": [4], "Seat comfort": [3], "Inflight entertainment": [5]})
# data = pd.concat([data, new_data], ignore_index=True)
# data.to_csv("Mon_Projet/data/Preprocessed_Airline_Dataset.csv", index=False)

# Gestion des onglets
# tabs = st.sidebar.radio("Sélectionnez un onglet :", ("Prévision", "Apprentissage", "Test et ajout données",))

# if tabs == "Prévision":
#     st.header("Prévision")
#     st.write("Contenu de l'onglet 1")

# elif tabs == "Apprentissage":
#     st.header("Apprentissage")
#     st.write("Contenu de l'onglet 2")

# elif tabs == "Test et ajout données":
#     st.header("Onglet 3")
#     st.write("Test et ajout données")
prevision_df_tab, apprentissage_df_tab, dashboard_test_tab = st.tabs(['Prévision', 'Apprentissage', 'Test et ajout données'])

with prevision_df_tab:
    # Créez une application Streamlit
    st.title("Tableau de bord Prévision")



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
            result = Preprocessing(data)
            X_train = result.train_data
            X_test = result.test_data
            y_train = Preprocessing.y_train
            y_test = Preprocessing.y_test
            # Affichez les données du fichier CSV
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
        