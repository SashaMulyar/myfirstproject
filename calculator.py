# def ob():
#     global res
#     global lv
#     global j
#     if (lv[j]>='a' and lv[j]<='z'):
#         t = input(lv[j]+"=")
#         j += 1
#         return int(t)
#     elif (lv[j]=='0' or lv[j]=='1'):
#         t = int(lv[j])
#         j += 1
#         return t
#     elif (lv[j]=='('):
#         t = int(v())
#         j += 1
#         if (lv[j-1]!=')'):
#             print("Синтаксическая ошибка")
#         else:
#             return t


# def mint():
#     global res
#     global lv
#     global j
#     t = ob()
#     while(j<len(lv)):
#         if (lv[j]=='&'):
#             j += 1
#             s = ob()
#             t=t*s
#         else:
#             break
#     return t


# def v():
#     global lv
#     global res
#     global j
#     t = ob()
#     if lv[j]=='^':
#         otr = 1
#         j += 1
#     else:
#         otr = 0
#         j += 1
#     t = mint()
#     if otr ==1:
#         t=(t+1)%2
#     while(j<len(lv)):
#         if (lv[j]=='+'):
#             j+=1
#             if mint()==1:
#                 t=1
#         else:
#             break
#     return t


# j = 0
# lv = input("Введите логическое выражение:")
# res = v()
# print(res)




# num -> /^[+-]?\d+(\.\d+)?/
# group -> ( term )
# value -> num | group
# mul -> num [*/] mul
# mul -> num
# sum -> mul [+-] sum
# sum -> mul
# term -> sum

import re


def num(expr):
    expr=expr.lstrip()
    res=re.match('^[+-]?\d(\.\d+)?',expr)
    if res:
        return float(res.group(0)),expr[res.end():]
    else:
        return None,expr

def value(expr):
    res, rest=num(expr)
    if res!=None:
        return res, rest
    res, rest=grouping(expr)
    return res, rest

def grouping(expr):
    expr=expr.lstrip()
    rest=''
    if expr[0]=='(':
        rest=expr[1:]
    else:
        return None, expr
    numb, rest=term(rest)
    if rest[0]!=')':
        return None, expr
    return numb, rest[1:]

def mul_oper(expr):
    expr=expr.lstrip()
    res=re.match('[*/]',expr)
    if res:
        return res.group(0), expr[res.end():]
    else:
        return None, expr

def mul(expr):
    numb1, rest1=value(expr)

    if numb1==None:
        return None, expr

    operator, rest2=mul_oper(rest1)

    if operator==None:
        return numb1, rest1

    numb2, rest2=mul(rest2)

    if operator=='*':
        return numb1*numb2, rest2
    if operator=='/':
        return numb1/numb2, rest2

    return None, expr

def sum_oper(expr):
    expr=expr.lstrip()
    res=re.match('[+-]', expr)
    if res:
        return res.group(0), expr[res.end():]
    else:
        return None, expr

def sum(expr):
    numb1, rest1=mul(expr)

    if numb1==None:
        return None, expr

    operator, rest2=sum_oper(rest1)

    if operator==None:
        return numb1, rest1

    numb2, rest2=sum(rest2)

    if operator=='+':
        return numb1+numb2, rest2
    if operator=='-':
        return numb1-numb2, rest2

    return None, expr


def term(expr):
    return sum(expr)

def validation(expr):
        match = re.search(a, expr)
        if match:
            print('validation is ok')
        else:
            print('wrong input, restart the programm')
            exit()
    

def iiinput():
    expr=input('input the exprassion==>>')
    validation(expr)
    return print((term(expr))[0])

a='[0-9 \.\(\)\-\+\*\/]'
if __name__=='__main__':
    iiinput()
        