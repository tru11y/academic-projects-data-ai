def double_return(args):
    try:
        # keys=()
        # values=()
        k=[]
        v=[]
        for key,value in args.items():
            k.append(key)
            v.append(value)


        return (f"{k,v}")
    except:
        return 84

# print(double_return({"a": 1, "b": 2}))