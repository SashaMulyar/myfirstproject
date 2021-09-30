import math
print('zx**3+ax**2+bx+c=0')
z=int(input('z='))
a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
D=(b**2)-(4*a*c)
if D>0:
    print(('x1=') (-b+sqrt(D))/(2*a))
    print(('x2=') (-b-sqrt(D))/(2*a))
elif D==0:
    print(('x1=') (-b+sqrt(D))/(2*a))        
else:
    print('нет корней')