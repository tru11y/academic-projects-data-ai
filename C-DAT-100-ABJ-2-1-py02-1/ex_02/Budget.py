class Budget:
    _transactions=[]
        
    def show_transactions(self):
        try:
            for arg in self._transactions:
                if arg>0:
                    print(f"You received {arg} euros")
                else:
                    print(f"You spent {abs(arg)} euros")  
        except:
            return 84
    
    def add_transactions(self,transations):
        for transaction in transations:
            try:
                if ((type(transaction) is float) or (type(transaction) is int)):
                    self._transactions.append(transaction)
                 
            except ValueError as e:
                raise ValueError ('Bad parameter')
         
            
# transactions = [512 , 42.08 , -12, "hello", 64]
# wallet = Budget ()
# wallet . add_transactions ( transactions )
# wallet . show_transactions ()