l='five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'
l=l.split(' ')
b=[]
d={'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 'twelve':12, 'thirteen':13, 'fourteen':14, 'fiveteen':15, 'sixteen':16, 'seventeen':17, 'eighteen':18, 'nineteen':19, 'twenty':20}
for i in l:
    b.append(d[i])

print(b)

