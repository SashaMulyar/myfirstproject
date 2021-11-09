def ob():
    global res
    global lv
    global j
    if (lv[j]>='a' and lv[j]<='z'):
        t = input(lv[j]+"=")
        j += 1
        return int(t)
    elif (lv[j]=='0' or lv[j]=='1'):
        t = int(lv[j])
        j += 1
        return t
    elif (lv[j]=='('):
        t = int(v())
        j += 1
        if (lv[j-1]!=')'):
            print("Синтаксическая ошибка")
        else:
            return t


def mint():
    global res
    global lv
    global j
    t = ob()
    while(j<len(lv)):
        if (lv[j]=='&'):
            j += 1
            s = ob()
            t=t*s
        else:
            break
    return t


def v():
    global lv
    global res
    global j
    t = ob()
    if lv[j]=='^':
        otr = 1
        j += 1
    else:
        otr = 0
        j += 1
    t = mint()
    if otr ==1:
        t=(t+1)%2
    while(j<len(lv)):
        if (lv[j]=='+'):
            j+=1
            if mint()==1:
                t=1
        else:
            break
    return t


j = 0
lv = input("Введите логическое выражение:")
res = v()
print(res)