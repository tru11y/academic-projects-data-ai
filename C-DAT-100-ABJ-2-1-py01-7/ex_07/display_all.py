def display_all(args):
    # dictionnary={}
    try:
        
        for key,val in args.items():
            val=f"({type(val).__name__}: {val})"
            print(val)
    except:
        return 84
# display_all({"test": "hello", "t": 43, "pi": 3.14})