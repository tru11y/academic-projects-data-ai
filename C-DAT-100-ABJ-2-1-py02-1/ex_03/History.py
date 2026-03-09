import json


class Budget:
    def __init__(self, path=None):
        self._transactions = {}
        self.path = path
        self.getpath()

    def getpath(self):
        with open(self.path, "r") as file:
            data = json.load(file)
            for dat in data["transactions"]:
                #    print(dat[" category "])
                # if dat[" category "] in (self._transactions):
                #     True
                    # self._transactions[dat[" category "]] = dat[" value "]
                # else:
                    self._transactions[dat[" category "]] = dat[" value "]

    def get_category(self):
        cat = []
        for key in self._transactions.keys():

            cat.append(key)
        return cat

        # print(self._transactions)
        #    print(data)

    def show_transactions(self,args):
        
            if self._transactions[args] > 0:
                print(f"You received {self._transactions[args]} euros")
            elif self._transactions[args] < 0:
                print(f"You spent {abs(self._transactions[args])} euros")


#     def show_transactions(self):

#         try:

#             for key,arg in enumerate(self._transactions):
#                 if arg > 0:
#                     print(f"You received {arg} euros")
#                 else:
#                     print(f"You spent {abs(arg)} euros")
#         except:
#             return 84

#     def add_transactions(self, transations):
#         for key, transaction in enumerate(transations):

#             if (type(key) is float) or (type(key) is int):
#                 self._transactions[key]=(transaction)
#             else:
#                 print(f"{TypeError}")
#                 # return 84


# transactions = {
#     " transactions ": [
#         {" value ": -42, " category ": " transport "},
#         {" value ": 1234, " category ": " salary "},
#     ]
# }
# wallet = Budget()
# wallet.add_transactions(transactions)
# wallet.show_transactions()
# wallet = Budget("ex_03/data.json")

# for category in wallet.get_category():
#     print(category)
#     wallet.show_transactions(category)

