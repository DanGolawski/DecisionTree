class Predictor:
    def predict(self, tree, objectt):
        keys = tree.keys()
        answer = ''
        for k in keys:
            if type(tree[k][objectt[k]]) is dict:
                return self.predict(tree[k][objectt[k]], objectt)
            else:
                return tree[k][objectt[k]]

            # print(k)
            # if type(tree[k]) is dict:
            #     self.predict(tree[k])
            #     # print(tree[k])
            # else:
            #     print(tree.get(k))
