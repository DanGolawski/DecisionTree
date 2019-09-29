import main.Models.Tree
import operator
import main.Managers.EntropyCalculator



class TreeBuilder:

    calculator = main.Managers.EntropyCalculator.EntropyCalculator()

    def build_root_node(self, dataframe):

        main_entropy = self.calculator.calculateRootNodeEntropy(dataframe['Eat'].to_list())
        potential_roots = {}
        for attr in dataframe.columns[:-1]:
            # potential_roots.append({attr : calculator.calculateGainForAttribute(rne, df[[attr, 'Eat']])})
            potential_roots[attr] = self.calculator.calculateGainForAttribute(main_entropy, dataframe[[attr, 'Eat']])

        best_node = self.find_best_node(potential_roots)
        for node in dataframe[best_node].unique():
            sub_dataframe = dataframe.loc[dataframe[best_node] == node]
            del sub_dataframe[best_node]
            print(sub_dataframe)

    def find_best_node(self, titles_gains):
        val = -1
        best = ""
        for key in titles_gains.keys():
            if titles_gains[key] > val:
                val = titles_gains[key]
                best = key
        return best
