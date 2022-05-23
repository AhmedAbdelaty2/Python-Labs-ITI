def only_unique(x):
    y = set(x)
    return list(y)

l = only_unique([0,1,4,5,7,1,1,4,1,5,1])
print(l)