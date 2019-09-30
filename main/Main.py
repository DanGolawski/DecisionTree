import pandas as pd
import main.Managers.EntropyCalculator
import main.Managers.TreeBuilder
import main.Managers.Predictor as Predictor

dataset = {'Taste': ['Salty', 'Spicy', 'Spicy', 'Spicy', 'Spicy', 'Sweet', 'Salty', 'Sweet', 'Spicy', 'Salty', 'Salty',
                     'Spicy', 'Spicy', 'Spicy', 'Spicy', 'Sweet', 'Salty', 'Sweet', 'Spicy', 'Salty'],
           'Temperature': ['Hot', 'Hot', 'Hot', 'Cold', 'Hot', 'Cold', 'Cold', 'Hot', 'Cold', 'Hot', 'Hot', 'Hot',
                           'Hot', 'Cold', 'Hot', 'Cold', 'Cold', 'Hot', 'Cold', 'Hot'],
           'Texture': ['Soft', 'Soft', 'Hard', 'Hard', 'Hard', 'Soft', 'Soft', 'Soft', 'Soft', 'Hard', 'Soft', 'Soft',
                       'Hard', 'Hard', 'Hard', 'Soft', 'Soft', 'Soft', 'Soft', 'Hard'],
           'Eat': ['No', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes',
                   'Yes', 'No', 'Yes', 'Yes', 'Yes']}

df = pd.DataFrame(dataset, columns=['Taste', 'Temperature', 'Texture', 'Eat'])

builder = main.Managers.TreeBuilder.TreeBuilder()

tree = builder.build_root_node(df)

print(tree)

data = {'Taste': 'Salty', 'Temperature': 'Hot', 'Texture': 'Hard'}

predictor = Predictor.Predictor()
print(predictor.predict(tree, data))


