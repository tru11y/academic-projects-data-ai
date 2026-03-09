def increment(args):
    return([n+1 if type(n) is int else n for n in args])
    
# increment([3, 4, 9, 'a', "qvb", {}])