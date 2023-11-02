import sys, os
sys.path.append(os.path.dirname(__file__) + "/..")
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from Components.models import Genders, Customer_types, Type_of_travel, Classes, Satisfaction, Traveler

db_url = "sqlite:///BDD_sqlite/Airline_Dataset_db.sqlite"
engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session() #on ouvre une nouvelle session
inspector = inspect(engine)




# Obtenir les noms des tables
table_names = inspector.get_table_names()

# Afficher les noms des tables
for table_name in table_names:
    print('valeur de la table :', table_name)

#Exécuter une requête pour récupérer les données de chaque table de dimension
genders = session.query(Genders).all() #Ici on récupère le nom de chaque produits dans la table 'gender_tbl'
customer_types = session.query(Customer_types).all() #Ici on récupère le nom de chaque produits dans la table 'customer_types_tbl'
type_of_travels = session.query(Type_of_travel).all() #Ici on récupère le nom de chaque produits dans la table 'type_of_travel_tbl'
classe = session.query(Classes).all() #Ici on récupère le nom de chaque produits dans la table 'classes_tbl'
satisfactions = session.query(Satisfaction).all() #Ici on récupère le nom de chaque produits dans la table 'satisfaction_tbl'
customers_id = session.query(Traveler).all() #Ici on récupère le nom de chaque produits dans la table 'travelers_tbl'



for ind, genders in enumerate(genders): 
        print(ind,"-",genders.gender)

for ind, customer_types in enumerate(customer_types): 
        print(ind,"-",customer_types.customer_type)

for ind, type_of_travels in enumerate(type_of_travels): 
       print(ind,"-",type_of_travels.type_of_travel)

for ind, classe in enumerate(classe): 
        print(ind,"-",classe.classes)

for ind, satisfactions in enumerate(satisfactions): 
        print(ind,"-",satisfactions.satisfaction)

for ind, customers_id in enumerate(customers_id): 
        print(ind,"-",customers_id.gender_id)


#Lire avec jointures multiples

joint = session.query(Traveler, Genders, Customer_types, Type_of_travel, Classes, Satisfaction).\
    join(Genders, Traveler.gender_id == Genders.id).\
    join(Customer_types, Traveler.customer_type_id == Customer_types.id).\
    join(Type_of_travel, Traveler.type_of_travel_id == Type_of_travel.id).\
    join(Classes, Traveler.class_id == Classes.id).\
    join(Satisfaction, Traveler.satisfaction_id == Satisfaction.id).all()

# Afficher les résultats de la jointure
print("Tout le monde est là ?")
for traveler, gender, customer, type_of_travel, classes, satisfaction in joint:
    print(
        f"traveler ID: {traveler.id}, gender: {gender.gender}, customer: {customer.customer_type}, type_of_travel: {type_of_travel.type_of_travel}, classes : {classes.classes}, satisfaction : {satisfaction.satisfaction}")

# Fermer la session
session.close()