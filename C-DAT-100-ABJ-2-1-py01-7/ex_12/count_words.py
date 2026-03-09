def count_words(args):
    # chaines =[]
    # for lettre in args:
    #     if lettre in chaines:
    #         chaines[lettre]+=1
    #     else:
    #         chaines[lettre]=1
    return {x: args.count(x) for x in args}       

# print(count_words(["Hello", "Hello", "world"]))