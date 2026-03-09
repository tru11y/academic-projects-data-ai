def show_methods(args):
    try:
        #method= [m for m in dir(args) if not m.startswith('__') and not m.endswith('__')]
        # for met in method:
        methods=[]
        for method in dir(args):
            methods.append(method)
        
        print(methods)
    except:
        return 84

# show_methods("a string object")