from math import ceil

def string_recombination(a, b):
    x = ceil(len(a)/2)
    y = ceil(len(b)/2)
    return (a[:x]+b[:y]+a[x:]+b[y:])

a = "ahmed"
b = "adam"

print(string_recombination(a, b))