
def create_db_tables():
    from sqlalchemy_utils import database_exists, drop_database, create_database #importer package nécessaire
    from Components.models import Base, Genders, Customer_types, Type_of_travel, Classes, Satisfaction, Traveler
    from sqlalchemy import create_engine
# Définir l'URL de la base de données
    db_url = "sqlite:///BDD_sqlite/Airline_Dataset_db.sqlite"

    if database_exists(db_url) : 
        drop_database(db_url)
        print('database already existed and has been deleted') #Si elle existe, elle sera effacée
    else :
        print('database does not exist') #Sinon le programme nous prévient

    create_database(db_url)
    print('A new database has been created') #Sinon le programme nous prévient et en crée une nouvelle
    engine = create_engine(db_url)
    Base.metadata.create_all(engine) #On crée toute les tables depuis le 'package' 'model', tous les objet ayant hérité de 'Base'
    print('Tables have been created')

def mult_replace(x, y) :
    # fonction to replace str by int to fit data in relationnal DB
    # x = list of values to replace, y = df
    a = len(x)
    for n in range(a) :
        i = n+1
        z = y.replace(x[n], i, inplace = True)
    return z