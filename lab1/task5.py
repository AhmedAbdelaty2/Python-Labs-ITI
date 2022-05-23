def remover(s):
    a = s.replace('a','')
    e = a.replace('e','')
    i = e.replace('i','')
    u = i.replace('u','')
    o = u.replace('o','')

    return o

x = remover('zaiozuez')
print(x)