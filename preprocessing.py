import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Chargement des données depuis le fichier CSV
data = pd.read_csv("data/Airline_Dataset.csv")

def Preprocessing(data) :
    # Prétraitement des données pour extraire les colonnes pertinentes
    data.drop(["id"], axis=1, inplace=True)
    data['Gender'] = np.where(data['Gender']=='Male',1,0)
    data['Customer Type'] = np.where(data['Customer Type']=='Loyal Customer',1,0)
    # data['Customer Type'] = np.where(data['Customer Type']=='Loyal Customer',1,0)
    data['Type of Travel'] = np.where(data['Type of Travel']=='Business travel',1,0)
    data['Satisfaction'] = np.where(data['Satisfaction']=='satisfied',1,0)
    data.insert(0, 'Business', np.where(data['Class']=='Business',1,0))
    data.insert(0, 'Eco_Plus', np.where(data['Class']=='Eco Plus',1,0))
    data.insert(0, 'Eco', np.where(data['Class']=='Eco',1,0))
    data.drop(["Class"], axis=1, inplace=True)
    # data['Arrival Delay in Minutes'] = np.where(data['Arrival Delay in Minutes'].isna(),1,0)
    # data.dropna(inplace=True)

    # selected_columns = ["Satisfaction", "Flight Distance", "Inflight wifi service", "Seat comfort", "Inflight entertainment","Type of Travel","Class","Online boarding", "On-board service", "Leg room service", "Customer Type"]
    # data = data[selected_columns]
    # print("isna :",data.isna().sum())
    # print("null :",data.isnull().sum())

    # Enregistrement des données prétraitées dans un nouveau fichier CSV
    data.to_csv("choix du modèle/Preprocessed_Airline_Dataset.csv", index=False)

    # # Division des données en ensembles d'entraînement et de test
    X = data.drop("Satisfaction", axis=1)
    y = data["Satisfaction"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Enregistrement des ensembles d'entraînement et de test dans des fichiers CSV
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)
    return test_data, train_data

def Ecriture_csv(data, test_data, train_data):
    test_data.to_csv("choix du modèle/Test_Data.csv", index=False)
    train_data.to_csv("choix du modèle/Train_Data.csv", index=False)
    data.to_csv("choix du modèle/Airline_Dataset.csv", index=False)
