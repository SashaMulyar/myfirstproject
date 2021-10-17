str1='qwert'
str2='rewq'
x=(i for i in str1+str2 if i not in str1 or i not in str2)
print(x)
if not x:
    print('str1 равно str2')
else:
    print('str1 не равно str2')


if str1[0].find(str2[0])>-1:
    print('str1 contains str2')
else:
    print('str1 doesnt contains str2')


if str1==reversed(str1):
    print('явл полиндромом') 
else:
    print('не является полиндромом')   




