def shows( args :dict):
  
    # dictionnary={}
    try:
        for i in [f"({key})->({type(val).__name__}: {(val)})" for key,val in args.items()]:
            print(i)
        # for key,val in args.items():
        #     value=f"({type(val).__name__}: {(val)})"
        #     print(f"{key}->{value}")
    except:
        return 84
# shows({"test": "hello", "t": 43, "pi": 3.14})
                
            
    # except:
    #     return 84
# display_all({"test": "hello", "t": 43, "pi": 3.14})