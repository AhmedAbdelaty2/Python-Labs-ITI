def look_for(s,c):
    l = []
    for pos,char in enumerate(s):
        if(char == c):
            l.append(pos)
    return l

x = look_for('google','o')
print(x)