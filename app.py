import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
# from components.utils_streamlit import run_disable, enable

# ----------------------- session state declaration -----------------------
#intern function and session logics and declared in this section

# if 'running' not in st.session_state:
#     st.session_state.running = False

# Chargement des données prétraitées
train_data = pd.read_csv("data/Test_Data.csv")
test_data = pd.read_csv("data/Test_Data.csv")
X_train = train_data.drop("satisfaction", axis=1)
X_test = test_data.drop("satisfaction", axis=1)
y_train = train_data["satisfaction"]
y_test = test_data["satisfaction"]

dataset = pd.read_csv("data/Airline_Dataset.csv")
prevision_df_tab, apprentissage_df_tab, dashboard_test_tab = st.tabs(['Prévision', 'Apprentissage', 'Test et ajout données'])

with prevision_df_tab:
    # Créer une application Streamlit
    st.title("Tableau de bord Prévision")

    # # Interface utilisateur avec Streamlit
    st.title("Prédiction de la satisfaction client")
    st.write("Entrez les caractéristiques du client pour prédire sa satisfaction.")

    cols_up1, cols_up2,cols_up3, cols_up4,cols_up5,cols_up6 = st.columns([1,1,1,1,1,1])

    with cols_up1:
        # # Entrée des caractéristiques du client
        max_value_delay = dataset['delay'].max()
        mean_value_delay = int(dataset['delay'].mean())
        delay = st.slider("delay", min_value=0, max_value=max_value_delay, step=1, value=mean_value_delay)
    with cols_up2:
        eco = st.radio("Eco", ["1", "0"])
    with cols_up3:
        eco_plus = st.radio("Eco Plus", ["0", "1"])
    with cols_up4:
        business = st.radio("Business", ["0", "1"])
    with cols_up5:
        custumer_type = st.radio("Custumer Type", ["1", "0"])
    with cols_up6:
        st.write("(Custumer Type = '1' pour Loyal Customer)")

    cols_up1, cols_up2,cols_up3, cols_up4, cols_up5 = st.columns([1,1,1,1,1])

    with cols_up1:
        ToT = st.radio("Type of Travel", ["1", "0"])
    with cols_up2:
        st.write("(Type of Travel = '1' pour Business travel)")
    with cols_up3:
        max_value_flight_distance = dataset['flight_distance'].max()
        mean_value_flight_distance = int(dataset['flight_distance'].mean())
        flight_distance = st.slider("Flight Distance", min_value=0, max_value=max_value_flight_distance, step=1, value=mean_value_flight_distance) 
    with cols_up4:
        gender = st.radio("Gender", ["1", "0"])
    with cols_up5:
        st.write("(Gender = '1' pour Homme)")
        
    # Créer le modèle Random Forest
    clf_client = RandomForestClassifier(n_jobs=-1,class_weight='balanced') 
    # Prédire la satisfaction client
    def Predire_la_satisfaction_client() :
        with st.spinner('Working AI magic...'): # loading widget
            # features = [delay, eco, eco_plus, business, custumer_type, ToT, flight_distance, gender]
            features = ["delay", "eco", "eco_plus", "business", "gender", "customer_type", "ToT", "flight_distance"]
            features_votes = ["cleanliness", "inflight_service", "chk_service", "gate_location", "food_and_drink", 
            "da_time_convenient", "flight_distance", "flight_distance", "iwservice", "ease_online_booking", "online_boarding", 
            "seat_comfort", "inflight_entertainmt", "leg_room_service", "on_board_service","baggage_handling"]
            dataset_features = dataset.loc[:, features] 
            dataset_features.insert(8, 'satisfaction', dataset['satisfaction'])
            dataset_votes = dataset.loc[:, features_votes] 
            dataset_features = pd.concat([dataset_votes, dataset_features], axis=1)
            st.title("Rapport de prévision :")
            st.write("Extrait de dataset_features")
            st.write(dataset_features.head)
            # st.write(dataset_features.dtypes)
            # Split the data into training and testing sets
            X = dataset_features.drop("satisfaction", axis=1)
            y = dataset_features["satisfaction"]
            # Entraîner le modèle
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            clf_client.fit(X_train, y_train)
            # dataset_features = dataset.loc[:, features] 
            prediction = clf_client.predict(X_test)
            prediction_mean = prediction.mean()
            # st.write(prediction)
            st.write(prediction_mean)
            if prediction_mean > 0.5:
                st.write("Satisfaction client : Positive")
                st.success('Positif !', icon='✅')
            else:
                st.write("Satisfaction client : Negative")
                st.success('Negatif!', icon='🚨')
         # , feature9, feature10, feature11, feature12, feature13, feature14, feature15, feature16, feature17, feature18, feature19, feature20, feature21, feature22, feature23]]
            # Afficher la prédiction
            # st.write("La satisfaction client prédite est :", prediction)
            # Affichage de la précision du modèle
            accuracy = accuracy_score(y_test, prediction)
            st.write(f"Précision du modèle : {accuracy:.2f}")
            # Affichage du rapport de classification
            report = classification_report(y_test, prediction)
            st.text("Rapport de classification :")
            st.text(report)
    st.button(label='Prédire la satisfaction client', type="primary", on_click=Predire_la_satisfaction_client,key=1)
    

    # with cols_up2:   
    #     feature9 = st.slider("iwservice", min_value=0, max_value=5, step=1)
    #     feature10 = st.slider("da_time_convenient", min_value=0, max_value=5, step=1)
    #     feature11 = st.slider("ease_online_booking", min_value=0, max_value=5, step=1)
    #     feature12 = st.slider("gate_location", min_value=0, max_value=5, step=1)
    #     feature13 = st.slider("food_and_drink", min_value=0, max_value=5, step=1)
    #     feature14 = st.slider("online_boarding", min_value=0, max_value=5, step=1)
    #     feature15 = st.slider("seat_comfort", min_value=0, max_value=5, step=1)
    #     feature16 = st.slider("inflight_entertainmt", min_value=0, max_value=5, step=1)
    #     feature17 = st.slider("on_board_service", min_value=0, max_value=5, step=1)
    #     feature18 = st.slider("leg_room_service", min_value=0, max_value=5, step=1)
    #     feature19 = st.slider("baggage_handling", min_value=0, max_value=5, step=1)
    #     feature20 = st.slider("chk_service", min_value=0, max_value=5, step=1)
    #     feature21 = st.slider("inflight_service", min_value=0, max_value=5, step=1)
    #     feature22 = st.slider("cleanliness", min_value=0, max_value=5, step=1)
    #     feature23 = st.radio("Satisfaction", ["Oui", "Non"])
        # feature24 = st.radio("Caractéristique 19", ["Oui", "Non"])


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
            result = preprocess_data(data, test_data, train_data)
            
            # Afficher les données du fichier CSV
            st.dataframe(data)
            if st.button("Lancer le modèle",type="primary") :
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
            result = preprocess_data(data, test_data, train_data)
            # Afficher les données du fichier Excel
            st.dataframe(data)
            if st.button("Lancer le modèle",type="primary") :
                # Création et entraînement du modèle
                clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced', warm_start=True)  
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
            result = preprocess_data(data, test_data, train_data)
            # Affichez les données du fichier JSON
            st.json(data)
            if st.button("Lancer le modèle",type="primary") :
                # Création et entraînement du modèle
                clf = RandomForestClassifier(n_jobs=-1,class_weight='balanced', warm_start=True)  
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
        