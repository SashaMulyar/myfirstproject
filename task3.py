with open('text.txt', 'r', encoding='utf-8') as t:
    t=t.read()
t=t.split()
print(t)


f=open('ready.txt', 'w',encoding='utf-8' )
for s in t:
    f.write(s + '\n')
    