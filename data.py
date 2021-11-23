import re

def mul_oper(expr):
    expr=expr.lstrip()
    res=re.match('[*/]',expr)
    if res:
        return res.group(0), expr[res.end():]
    else:
        return None, expr


def sum_oper(expr):
    expr=expr.lstrip()
    res=re.match('[+-]', expr)
    if res:
        return res.group(0), expr[res.end():]
    else:
        return None, expr



def num(expr):
    expr=expr.lstrip()
    res=re.match('^[+-]?\d(\.\d+)?',expr)
    if res:
        return float(res.group(0)),expr[res.end():]
    else:
        return None,expr

