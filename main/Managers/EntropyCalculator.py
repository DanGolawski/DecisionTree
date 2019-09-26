from math import log2


class EntropyCalculator:

    def calculateRootNodeEntropy(self, results):
        values = set(results)
        calculation = 0
        for v in values:
            proportion = results.count(v) / len(results)
            calculation -= proportion * log2(proportion)
        return calculation

    def calculateGainForAttribute(self, main_entropy, list):
        col_names = list.columns.to_list()
        unique_attr = list.iloc[:, 0].unique()
        unique_reslt = list.iloc[:, -1].unique()
        # print(list[(list[col_names[0]]==unique_attr[0]) & (list[col_names[-1]]==unique_reslt[0])])
        entropy = 0
        # print(list[list.iloc[:,0]==unique[0]])
        for ua in unique_attr:
            proportion = len(list[list.iloc[:, 0] == ua]) / len(list)
            # print(ua + " proportion..." + str(proportion))
            internal_sum = 0
            for ur in unique_reslt:
                internal_proportion = len(list[(list[col_names[0]] == ua) & (list[col_names[-1]] == ur)]) / len(
                    list[list[col_names[0]] == ua])
                if internal_proportion != 0:
                    internal_sum += internal_proportion * log2(internal_proportion)
            entropy += -proportion * internal_sum
            # print(ua + '...' + str(entropy))
        return main_entropy - entropy
