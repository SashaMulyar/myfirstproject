import re

from data import num 
from data import mul_oper
from data import sum_oper
a='[0-9 \.\(\)\-\+\*\/]'
def term(expr):
    return sum(expr)

def validation(expr):
        match = re.search(a, expr)
        if match:
            print('validation is ok')
        else:
            print('wrong input, restart the programm')
            exit()

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

def value(expr):
    res, rest=num(expr)
    if res!=None:
        return res, rest
    res, rest=grouping(expr)
    return res, rest

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
