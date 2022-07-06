address = input()
s = ''
for i in address:
    if i == '.': s += '[.]'
    else: s+= i
print(s)