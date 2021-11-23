import blogic
def iiinput():
    expr=input('input the exprassion==>>')
    blogic.validation(expr)
    return print((blogic.term(expr))[0])

if __name__=='__main__':
    iiinput()