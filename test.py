t=input('Please input for how many months you want to open a deposit:\n')
print('you entered',t)
b=input('Please input the initial amount:\n')
print('you entered',b)
n=input('Please input the year rate, %:\n')
print('you entered',n)
total_amount=int(b)*((1+(int(n)/100)/12)**int(t))
print('Total amount will be',round(total_amount, 2),'rubles')

