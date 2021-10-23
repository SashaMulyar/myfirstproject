with open('text.txt', 'r', encoding='utf-8') as t:
    t=t.read()
t=t.split()
print(t)

p=''
for i in range(len(t)):
    p+=t[i]+' '
    if len(p)==40:
        print(p)
        p=''
    if i == (len(t)-1):
        print(p)
        break
    if len(p)+len(t[i+1])>40:
        print(p)
        p=''



    

    
    