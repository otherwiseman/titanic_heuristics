# customheuristic.py
# predicts Titanic pssenger survival with 80.02 % accuracy using a combination
# of passenger gender, age, socioeconomic class, and fare price paid
# completed as part of Data Science project 

import numpy
import pandas
import statsmodels.api as sm
file_path = r'C:/Users/LJM/Downloads/titanic_data.csv'
def custom_heuristic(file_path):

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        if (passenger['Sex'] == 'female' or passenger['Pclass'] == 1 and passenger['Age'] <= 18):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1
        elif (passenger['Fare'] > 263):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1
        elif (passenger['Pclass'] == 1 and passenger['Age'] >= 77):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1
        elif (passenger['Age'] <= 6):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1
        elif (passenger['Pclass'] == 2 or passenger['Pclass'] == 3):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 0
        elif (passenger['Age'] <= 8):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1
        elif (passenger['Sex'] == 'male' or passenger['Pclass'] == 3):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 0
        elif (passenger['Age'] >= 18 or passenger['Pclass'] == 3):
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 0
        else:
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 0 
    return predictions
