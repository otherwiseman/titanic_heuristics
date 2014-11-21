# titanicsimpleheuristic.py
# a program to predict whether or not a passenger survived the Titanic
# crash based on their gender. The program predicts with 78.68% accuracy. 
import numpy
import pandas
import statsmodels.api as sm
file_path = r'C:/Users/LJM/Downloads/titanic_data.csv'
def simple_heuristic(file_path):
    '''
    This exercise waas originally a machine learning
    challenge on Kaggle
    (seen here: http://www.kaggle.com/c/titanic-gettingStarted/data)

    I completed it as part of a Data Science course through Udacity. 
    '''

    predictions = {}
    df = pandas.read_csv(file_path)
    for passenger_index, passenger in df.iterrows():
        if (passenger['Sex'] == 'male'): 
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 0
        elif (passenger['Sex'] == 'female'): 
            passenger_id = passenger['PassengerId']
            predictions[passenger_id] = 1

    predictions[passenger_id] = 0

                                    
    return predictions
