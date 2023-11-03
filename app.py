import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from components.utils_streamlit import run_disable, enable
from preprocessing import preprocess_data

# ----------------------- session state declaration -----------------------
#intern function and session logics and declared in this section

if 'result_prediction_btn' not in st.session_state:
    st.session_state.result_prediction_btn = False

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
    # # Interface utilisateur avec Streamlit
    st.title("Prédiction de la satisfaction client")
    st.write("Entrez les caractéristiques du client pour prédire sa satisfaction.")

    cols_up1, cols_up2,cols_up3, cols_up4,cols_up5 = st.columns([1,1,1,1,1])

    with cols_up1:
        # # Entrée des caractéristiques du client
        max_value_delay = dataset['delay'].max()
        mean_value_delay = int(dataset['delay'].mean())
        delay = st.slider("arrival and departure delay", min_value=0, max_value=max_value_delay, step=1, value=mean_value_delay, key="delay")
    with cols_up2:
        pass_class_selec = st.selectbox("Passenger Class", ('Eco', 'Eco +', 'Business'))
        if pass_class_selec == 'Eco' :
            eco = 1
            eco_plus = 0
            business = 0
        elif pass_class_selec == 'Eco+' :
            eco = 0
            eco_plus = 1
            business = 0
        elif pass_class_selec == 'Business' :
            eco = 1
            eco_plus = 0
            business = 1
    with cols_up3:
        custumer_type = int(st.radio("Custumer Type", ["1", "0"], key="custumer_type"))
    with cols_up5:
        st.write("(Custumer Type = '1' pour Loyal Customer)")

    cols_up1, cols_up2,cols_up3, cols_up4, cols_up5 = st.columns([1,1,1,1,1])

    with cols_up1:
        ToT = int(st.radio("Type of Travel", ["1", "0"], key="ToT"))
    with cols_up2:
        st.write("(Type of Travel = '1' pour Business travel)")
    with cols_up3:
        max_value_flight_distance = dataset['flight_distance'].max()
        mean_value_flight_distance = int(dataset['flight_distance'].mean())
        flight_distance = st.slider("Flight Distance", min_value=0, max_value=max_value_flight_distance, step=1, value=mean_value_flight_distance) 
    with cols_up4:
        gender = int(st.radio("Gender", ["1", "0"], key="gender"))
    with cols_up5:
        st.write("(Gender = '1' pour Homme)")

    # Créer le modèle Random Forest
    clf_client = RandomForestClassifier(n_jobs=-1,class_weight='balanced') 
    dataset = pd.read_csv("data/Airline_Dataset.csv")
    features = ["delay", "eco", "eco_plus", "business", "gender", "customer_type", "ToT", "flight_distance", "satisfaction"]
    votes = ["cleanliness", "inflight_service", "chk_service", "gate_location", "food_and_drink", "da_time_convenient", "iwservice",
     "ease_online_booking", "online_boarding", "seat_comfort", "inflight_entertainmt", "leg_room_service", "on_board_service","baggage_handling"]
    dataset_features = dataset[features] 
    dataset_votes = dataset[votes] 
    dataset_features = pd.concat([dataset_features, dataset_votes], axis=1)
    X = dataset_features.drop("satisfaction", axis=1)
    y = dataset_features["satisfaction"]
    # Entraîner le modèle
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf_client.fit(X_train, y_train)
    st.header("Voting :")

    cols_up1, cols_up2,cols_up3, cols_up4 = st.columns([1,1,1,1])

    with cols_up1:
        cleanliness = st.slider("cleanliness", min_value=0, max_value=5, step=1,key="cleanliness", value=int(dataset_votes.cleanliness.mean()))
    with cols_up2:
        inflight_service = st.slider("inflight_service", min_value=0, max_value=5, step=1,key="inflight_service", value=int(dataset_votes.inflight_service.mean()))
    with cols_up3:
        chk_service = st.slider("Checkin service", min_value=0, max_value=5, step=1,key="chk_service", value=int(dataset_votes.chk_service.mean()))
    with cols_up4:
        gate_location = st.slider("Gate location", min_value=0, max_value=5, step=1,key="gate_location", value=int(dataset_votes.gate_location.mean()))

    cols_up5, cols_up6,cols_up7, cols_up8,cols_up9 = st.columns([1,1,1,1,1])

    with cols_up5:
        food_and_drink = st.slider("Food and drink", min_value=0, max_value=5, step=1,key="food_and_drink", value=int(dataset_votes.food_and_drink.mean()))
    with cols_up6:
        da_time_convenient = st.slider("Dep/Arr time convenient", min_value=0, max_value=5, step=1,key="da_time_convenient", value=int(dataset_votes.da_time_convenient.mean()))
    with cols_up7:
        iwservice = st.slider("Inflight wifi", min_value=0, max_value=5, step=1,key="iwservice", value=int(dataset_votes.iwservice.mean()))
    with cols_up8:
        ease_online_booking = st.slider("Ease online booking", min_value=0, max_value=5, step=1,key="ease_online_booking", value=int(dataset_votes.ease_online_booking.mean()))    
    with cols_up9:
        online_boarding = st.slider("Online boarding", min_value=0, max_value=5, step=1,key="online_boarding", value=int(dataset_votes.online_boarding.mean())) 

    cols_up10, cols_up11,cols_up12, cols_up13,cols_up14 = st.columns([1,1,1,1,1])

    with cols_up10:
        seat_comfort = st.slider("Seat comfort", min_value=0, max_value=5, step=1,key="seat_comfort", value=int(dataset_votes.seat_comfort.mean()))
    with cols_up11:
        inflight_entertainmt = st.slider("Inflight entertainment", min_value=0, max_value=5, step=1,key="inflight_entertainmt", value=int(dataset_votes.inflight_entertainmt.mean()))
    with cols_up12:
        leg_room_service = st.slider("Leg room service", min_value=0, max_value=5, step=1,key="leg_room_service", value=int(dataset_votes.leg_room_service.mean()))
    with cols_up13:
        on_board_service = st.slider("On-board service", min_value=0, max_value=5, step=1,key="on_board_service", value=int(dataset_votes.on_board_service.mean()))    
    with cols_up14:
        baggage_handling = st.slider("Baggage handling", min_value=0, max_value=5, step=1,key="baggage_handling", value=int(dataset_votes.baggage_handling.mean()))    
    
    # Prédire la satisfaction client
    result_prediction_btn = st.session_state.result_prediction_btn
    result_prediction_btn = st.button(label='Prédire la satisfaction client', type="primary",key='button_pred', disabled= result_prediction_btn)

    if result_prediction_btn :
        with st.spinner('Génération de la prédiction...'): # loading widget
            st.title("Rapport de prévision :")
            st.write("Extrait de dataset_features")
            X = pd.DataFrame([
                delay, eco, eco_plus, business, gender, custumer_type, ToT, flight_distance, cleanliness, inflight_service,
                chk_service, gate_location, food_and_drink, da_time_convenient, iwservice,
                ease_online_booking, online_boarding, seat_comfort, inflight_entertainmt,
                leg_room_service, on_board_service, baggage_handling
            ])
            X = np.array(X).reshape(1, -1)
            X = pd.DataFrame(X, columns=["delay", "eco", "eco_plus", "business", "gender", "customer_type", "ToT",
            "flight_distance", "cleanliness", "inflight_service", "chk_service", "gate_location",
            "food_and_drink", "da_time_convenient", "iwservice", "ease_online_booking", "online_boarding",
            "seat_comfort", "inflight_entertainmt", "leg_room_service", "on_board_service", "baggage_handling"])
            X
            prediction = clf_client.predict(X)
            predict_proba = clf_client.predict_proba(X)[0][1]
            efficacite_modele = clf_client.score(X_test, y_test)
            st.write(f"Probabilité de Satisfaction : {predict_proba:.2f}")
            st.write(f"Score du modèle : {efficacite_modele:.2f}")
            # Afficher la prédiction
            if prediction > 0.5:
                st.success('Satisfaction client : Positive !', icon='✅')
            else:
                st.success('La satisfaction client prédite est : Negative !', icon='🚨')
            # Affichage de la précision du modèle
        st.session_state.running = False

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
        