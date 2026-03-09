def my_args_handler(*args):
   try:
        return ", ".join(args)
   except:
       return 84
    
    
#print(my_args_handler("a", 'b', 'c', 'poke','jour', 'nuit'))