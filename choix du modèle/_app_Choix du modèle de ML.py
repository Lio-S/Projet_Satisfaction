import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


# Chargement des données prétraitées
train_data = pd.read_csv("Train_Data.csv")
test_data = pd.read_csv("Test_Data.csv")
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
target_names = train_data.columns
report = classification_report(y_test, y_pred, target_names=train_data.columns)
st.text("Rapport de classification :")
st.text(report)

# Affichage des données dans Streamlit
st.header("Données d'entraînement et de test")
st.write("Données d'entraînement :")
# st.write(X_train)
st.dataframe(X_train.head())

st.write("Données de test :")
# st.write(X_test)
st.dataframe(X_test.head())

# # Affichage d'un graphique
# st.header("Graphique")
# st.bar_chart(data.data)
