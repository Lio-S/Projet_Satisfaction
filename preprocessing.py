import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Chargement des données depuis le fichier CSV
data = pd.read_csv("data/Airline_Dataset.csv")

def preprocess_data(data, test_data, train_data):
    """
    This function preprocesses the given data by dropping unnecessary columns,
    converting categorical variables to binary, and inserting new columns.
    It then saves the preprocessed data into a CSV file and splits it into
    training and testing sets.

    Args:
        data (DataFrame): The input data to be preprocessed.

    Returns:
        tuple: A tuple containing the training and testing data.
    """
    # Convert 'Gender' to binary
    data['Gender'] = np.where(data['Gender']=='Male',1,0)
    data = data.rename(columns={'Gender': 'gender'})
    # Convert 'Customer Type' to binary
    data['Customer Type'] = np.where(data['Customer Type']=='Loyal Customer',1,0)
    data = data.rename(columns={'Customer Type': 'customer_type'})
    # Convert 'Type of Travel' to binary
    data['Type of Travel'] = np.where(data['Type of Travel']=='Business travel',1,0)
    data = data.rename(columns={'Type of Travel': 'ToT'})

    # Convert 'Satisfaction' to binary
    data['Satisfaction'] = np.where(data['Satisfaction']=='satisfied',1,0)
    data = data.rename(columns={'Satisfaction': 'satisfaction'})

    # Insert new columns based on 'Class'
    data.insert(0, 'business', np.where(data['Class']=='Business',1,0))
    data.insert(0, 'eco_plus', np.where(data['Class']=='Eco Plus',1,0))
    data.insert(0, 'eco', np.where(data['Class']=='Eco',1,0))

    # Insert new column based on 'Departure Delay and Arrival Delay'
    data.insert(0, 'delay', data['Departure Delay in Minutes'] + data['Arrival Delay in Minutes'])
    # data['delay'] = data['Departure Delay in Minutes'] + data['Arrival Delay in Minutes']

    # Drop unnecessary columns
    data.drop(["id"], axis=1, inplace=True)
    data.drop(["Departure Delay in Minutes"], axis=1, inplace=True)
    data.drop(["Arrival Delay in Minutes"], axis=1, inplace=True)
    data.drop(["Class"], axis=1, inplace=True)
    data.drop(["Age"], axis=1, inplace=True)

    # formatting data
    data = data.rename(columns={'Baggage handling': 'baggage_handling'})
    data = data.rename(columns={'Cleanliness': 'cleanliness'})
    data = data.rename(columns={'Inflight service': 'inflight_service'})
    data = data.rename(columns={'Checkin service ': 'chk_service'})
    data = data.rename(columns={'Gate location': 'gate_location'})
    data = data.rename(columns={'Food and drink': 'food_and_drink'})
    data = data.rename(columns={'Departure/Arrival time convenient': 'da_time_convenient'})
    data = data.rename(columns={'Flight Distance': 'flight_distance'})
    data = data.rename(columns={'Inflight wifi service': 'iwservice'})
    data = data.rename(columns={'Ease of Online booking': 'ease_online_booking'})
    data = data.rename(columns={'Online boarding': 'online_boarding'})
    data = data.rename(columns={'Seat comfort': 'seat_comfort'})
    data = data.rename(columns={'Inflight entertainment': 'inflight_entertainmt'})
    data = data.rename(columns={'Leg room service': 'leg_room_service'})
    data = data.rename(columns={'On-board service': 'on_board_service'})

    # Save the preprocessed data into a CSV file
    data.to_csv("choix du modèle/Preprocessed_Airline_Dataset.csv", index=False)

    # Split the data into training and testing sets
    X = data.drop("satisfaction", axis=1)
    y = data["satisfaction"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create training and testing data sets
    train_data = pd.concat([X_train, y_train], axis=1)
    test_data = pd.concat([X_test, y_test], axis=1)

    # data['Arrival Delay in Minutes'] = np.where(data['Arrival Delay in Minutes'].isna(),1,0)
    # data.dropna(inplace=True)

    # selected_columns = ["Satisfaction", "Flight Distance", "Inflight wifi service", "Seat comfort", "Inflight entertainment","Type of Travel","Class","Online boarding", "On-board service", "Leg room service", "Customer Type"]
    # data = data[selected_columns]
    # print("isna :",data.isna().sum())
    # print("null :",data.isnull().sum())
    test_data.to_csv("data/Test_Data.csv", index=False)
    train_data.to_csv("data/Train_Data.csv", index=False)
    data.to_csv("data/Airline_Dataset.csv", index=False)

    return (test_data, train_data)