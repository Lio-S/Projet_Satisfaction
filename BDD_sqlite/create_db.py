import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")
import pandas as pd
from Components.db_utilities import create_db_tables, mult_replace
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Components.models import Base, Genders, Customer_types, Type_of_travel, Classes, Satisfaction, Traveler
import csv


df = pd.read_csv('./data/Airline_Dataset.csv')


#Remplacement des valurs répétitives dans la table pour être intégré dans la BDD relationnelle
gender = ['Male','Female']
custom = ['Loyal Customer', 'disloyal Customer']
type = ['Personal Travel', 'Business travel']
classes = ['Eco Plus', 'Business', 'Eco']
satisfaction = ['neutral or dissatisfied','satisfied']

to_replace = [gender, custom, type, classes, satisfaction]

for n in to_replace :
    mult_replace(n, df)#fonction home made, afin de remplacé les contenues d'un dataframe à partir d'une liste


#Renommer chaque colonne pour que leur noms correspondent à celui des colonnes dans la BDD
old = ['id',
 'Gender',
 'Customer Type',
 'Age',
 'Type of Travel',
 'Class',
 'Flight Distance',
 'Inflight wifi service',
 'Departure/Arrival time convenient',
 'Ease of Online booking',
 'Gate location',
 'Food and drink',
 'Online boarding',
 'Seat comfort',
 'Inflight entertainment',
 'On-board service',
 'Leg room service',
 'Baggage handling',
 'Checkin service',
 'Inflight service',
 'Cleanliness',
 'Departure Delay in Minutes',
 'Arrival Delay in Minutes',
 'Satisfaction']

new = ['customer_id', 'gender_id', 'customer_type_id', 'age', 'type_of_travel_id', 'class_id', 
                      'flight_distance', 'inflight_wifi_service', 'departure_arrival_time_convenient', 'ease_of_online_booking',
                      'gate_location', 'food_and_drink', 'online_boarding', 'seat_comfort', 'inflight_entertainment', 
                      'on_board_service', 'leg_room_service', 'baggage_handling', 'checkin_service', 'inflight_service', 
                      'cleanliness', 'departure_delay_in_minutes', 'arrival_delay_in_minutes', 'satisfaction_id']

a = 0
for n in old :
    df.rename(columns = {n : new[a]}, inplace = True)
    a = a + 1

#exportation du fichier.csv nettoyé pour avoir le document intermédiaire
df.to_csv('./data/Airline_Dataset_to_BDD.csv')

#Fonction pour créer la base de données, depuis le fichier models.py
create_db_tables()

db_url = "sqlite:///BDD_sqlite/Airline_Dataset_db.sqlite" #chemin d'accès à la BDD

engine = create_engine(db_url)
   
Session = sessionmaker(bind=engine) #create session
session = Session()

#préparation des valeurs pour les tables dimensionnelles
gender_1 = Genders(id = 1, gender = 'Male')
gender_2 = Genders(id = 2, gender = 'Female')

customer_type_1 = Customer_types(id = 1, customer_type = 'Loyal Customer')
customer_type_2 = Customer_types(id = 2, customer_type = 'disloyal Customer')

type_of_travel_1 = Type_of_travel(id = 1, type_of_travel = 'Personal Travel')
type_of_travel_2 = Type_of_travel(id = 2, type_of_travel = 'Business travel')

class_1 = Classes(id = 1, classes = 'Eco Plus')
class_2 = Classes(id = 2, classes = 'Business')
class_3 = Classes(id = 3, classes = 'Eco')

satisfaction_1 = Satisfaction(id = 1, satisfaction = 'neutral or dissatisfied')
satisfaction_2 = Satisfaction(id = 2, satisfaction = 'satisfied')

session.add_all([gender_1, gender_2, customer_type_1, customer_type_2, type_of_travel_1, type_of_travel_2, customer_type_2, class_1, class_2, class_3,
                 satisfaction_1, satisfaction_2])

#Intégrer les valeurs aux tables dimensionnelles

# Lire le fichier CSV et insérer les données de la table principale de la BDD
with open('data/Airline_Dataset_to_BDD.csv') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        nouvelle_ligne = Traveler(
            customer_id=int(row['customer_id']),
            gender_id=int(row['gender_id']),
            customer_type_id =int(row['customer_type_id']),
            age=int(row['age']),
            type_of_travel_id=int(row['type_of_travel_id']),
            class_id=int(row['class_id']),
            flight_distance=int(row['flight_distance']),
            inflight_wifi_service=int(row['inflight_wifi_service']),
            departure_arrival_time_convenient=int(row['departure_arrival_time_convenient']),
            ease_of_online_booking=int(row['ease_of_online_booking']),
            gate_location=int(row['gate_location']),
            food_and_drink=int(row['food_and_drink']),
            online_boarding=int(row['online_boarding']),
            seat_comfort=int(row['seat_comfort']),
            inflight_entertainment=int(row['inflight_entertainment']),
            on_board_service=int(row['on_board_service']),
            leg_room_service=int(row['leg_room_service']),
            baggage_handling=int(row['baggage_handling']),
            checkin_service=int(row['checkin_service']),
            inflight_service=int(row['inflight_service']),
            cleanliness=int(row['cleanliness']),
            departure_delay_in_minutes=int(row['departure_delay_in_minutes']),
            arrival_delay_in_minutes=(row['arrival_delay_in_minutes']),
            satisfaction_id=int(row['satisfaction_id'])
        )
        session.add(nouvelle_ligne)

# Valider les modifications et fermer la session

session.commit() #conclue l'ajout des produits dans la table produits
    
session.close() # Fermer la session