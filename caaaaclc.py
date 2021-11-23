import re
def Jsq(Num):
    global Sum
    d=[]
    for i in Num: # Traverse в Num
        if i.isnumeric(): #judgment, является ли это число
            pass
        else:
            d.append (i) # Поместить пройденные числа в список b
    for i in Num:
        if i == "+" or i == "-" or i == "*" or i == "/": # символ оценки
            Num = Num.replace(i, ",")
    Num = Num.split(",")
    Num=(list(filter(lambda x: x != '', Num)))
    k=[]
    for i in Num:
        i=int(i)
        k.append(i)
    Sum=0
    for i in range(len(d)):
        if "*" in d and "/" in d:
            m = d.index("*")
            n = d.index("/")
            if m < n:
                Sum = k[m] * k[m + 1]
                k[m] = Sum
                del k[m + 1]
                d.remove(d[m])
                i = 0
            else:
                Sum = int(k[n]) / int(k[n + 1])
                k[n] = Sum
                del k[n + 1]
                d.remove(d[n])
                i = 0
        elif "*" in d:
            m = d.index("*")
            Sum = k[m] * k[m + 1]
            k[m] = Sum
            del k[m + 1]
            d.remove(d[m])
            i = 0
        elif "/" in d:
            n = d.index("/")
            Sum = k[n] / k[n + 1]
            k[n] = Sum
            del k[n + 1]
            d.remove(d[n])
            i = 0
    for i in range(len(d)):
        if "+" in d and "-" in d:
            m = d.index("+")
            n = d.index("-")
            if m < n:
                Sum = k[m] + k[m + 1]
                k[m] = Sum
                k.remove(k[m + 1])
                d.remove(d[m])
            else:
                Sum = k[n] - k[n + 1]
                k[n] = Sum
                k.remove(k[n + 1])
                d.remove(d[n])
            i = 0
        elif "+" in d:
            m = d.index("+")
            Sum = k[m] + k[m + 1]
            k[m] = Sum
            k.remove(k[m + 1])
            d.remove(d[m])
        elif "-" in d:
            n = d.index("-")
            Sum = k[n] - k[n + 1]
            k[n] = Sum
            k.remove(k[n + 1])
            d.remove(d[n])
        i = 0
    return Sum


def chazhao():
    global Nba
    global Num
    global m
    global n
    for i in Nba:
        if i == "(":
            m=Nba.rfind("(")
    n=Nba[m:]
    for i in n:
        if i ==")":
            c=n.find(")")
    Num=n[1:c]
    Jsq(Num)
    j=str(Sum)
    Nba=Nba.replace(Nba[m:m+c+1],j)

Nba = input ("Пожалуйста, введите формулу расчета:")


while True:
    if "(" in Nba:
        chazhao()
    else:
        Jsq(Nba)
        print(Sum)
        break
