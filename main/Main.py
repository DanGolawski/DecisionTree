import numpy as np
import pandas as pd
import main.Managers.EntropyCalculator

eps = np.finfo(float).eps

dataset = {'Taste': ['Salty', 'Spicy', 'Spicy', 'Spicy', 'Spicy', 'Sweet', 'Salty', 'Sweet', 'Spicy', 'Salty'],
           'Temperature': ['Hot', 'Hot', 'Hot', 'Cold', 'Hot', 'Cold', 'Cold', 'Hot', 'Cold', 'Hot'],
           'Texture': ['Soft', 'Soft', 'Hard', 'Hard', 'Hard', 'Soft', 'Soft', 'Soft', 'Soft', 'Hard'],
           'Eat': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes']}

df = pd.DataFrame(dataset, columns=['Taste', 'Temperature', 'Texture', 'Eat'])

calculator = main.Managers.EntropyCalculator.EntropyCalculator()

# 1. Root Node Entropy
rne = calculator.calculateRootNodeEntropy(df['Eat'].to_list())

# 2. Gain for every attribute
for attr in df.columns[:-1]:
    # calculator.calculateGainForAttribute(rne, {attr: df[attr].to_list(), 'Eat': df['Eat'].to_list()})
    print(calculator.calculateGainForAttribute(rne, df[[attr, 'Eat']]))

