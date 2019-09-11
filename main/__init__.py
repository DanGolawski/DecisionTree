import numpy as np
import pandas as pd

eps = np.finfo(float).eps
from numpy import log2

dataset = {'Taste': ['Salty', 'Spicy', 'Spicy', 'Spicy', 'Spicy', 'Sweet', 'Salty', 'Sweet', 'Spicy', 'Salty'],
           'Temperature': ['Hot', 'Hot', 'Hot', 'Cold', 'Hot', 'Cold', 'Cold', 'Hot', 'Cold', 'Hot'],
           'Texture': ['Soft', 'Soft', 'Hard', 'Hard', 'Hard', 'Soft', 'Soft', 'Soft', 'Soft', 'Hard'],
           'Eat': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes']}

df = pd.DataFrame(dataset, columns=['Taste', 'Temperature', 'Texture', 'Eat'])


def main_entropy():
    entropy = 0
    values = df.iloc[:, -1].unique()
    for v in values:
        fraction = df.iloc[:, -1].value_counts()[v] / len(df)
        entropy += -fraction*np.log2(fraction)
    return entropy

def attribute_entropy(title):
    entropy = 0
    results = df.iloc[:, -1].unique() # gives [Yes, No]
    values = df[title].unique()
    for v in values:
        probability = df[title].value_counts()[v] / len(df)
        entropy += probability*get_S()


entropy0 = main_entropy() # first entropy of result column
columns_no = len(df.columns)
attribute_entropy('Taste')
