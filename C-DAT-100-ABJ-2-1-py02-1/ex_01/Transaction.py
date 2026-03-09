def show_transactions(args:list):
    for arg in args:
        if arg>0:
            print(f"You received {arg} euros")
        elif arg<0:
            print(f"You spent {abs(arg)} euros")
            

# show_transactions([0,5,-1])