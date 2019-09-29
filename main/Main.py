import numpy as np
import pandas as pd
import main.Managers.EntropyCalculator
import main.Managers.TreeBuilder

eps = np.finfo(float).eps

dataset = {'Taste': ['Salty', 'Spicy', 'Spicy', 'Spicy', 'Spicy', 'Sweet', 'Salty', 'Sweet', 'Spicy', 'Salty'],
           'Temperature': ['Hot', 'Hot', 'Hot', 'Cold', 'Hot', 'Cold', 'Cold', 'Hot', 'Cold', 'Hot'],
           'Texture': ['Soft', 'Soft', 'Hard', 'Hard', 'Hard', 'Soft', 'Soft', 'Soft', 'Soft', 'Hard'],
           'Eat': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes']}

df = pd.DataFrame(dataset, columns=['Taste', 'Temperature', 'Texture', 'Eat'])

# 1. Root Node Entropy
calculator = main.Managers.EntropyCalculator.EntropyCalculator()
# rne = calculator.calculateRootNodeEntropy(df['Eat'].to_list())

# 2. Gain for every attribute
# potential_roots = {}
# for attr in df.columns[:-1]:
#     # potential_roots.append({attr : calculator.calculateGainForAttribute(rne, df[[attr, 'Eat']])})
#     potential_roots[attr] = calculator.calculateGainForAttribute(rne, df[[attr, 'Eat']])

# 3. Building tree
builder = main.Managers.TreeBuilder.TreeBuilder()
builder.build_root_node(df)