def display_all(args):
    # dictionnary={}
    try:
        
   
            
        
                for key,val in enumerate(args.values()):
                   
            
                    print(f"{key}->({type(val).__name__}: {val})")
                    
    
                
            
    except:
        return 84
# display_all({"test": "hello", "t": 43, "pi": 3.14})