#coding:utf-8
import re
from functools import reduce
def sub_calc (formula): # Вычислить значение сложения, вычитания, умножения и деления
    flag=True
    while flag:
        m=re.search('\d+\.?\d*[*/]-?\d+\.?\d*',formula)#5.12*-123.12 -5.12/-123.12
                 #print ('Соответствует \ n', m.group ())
        if m:
            sub_mul_div=m.group()
            res=calc_mul_div(sub_mul_div)
                         formula = formula.replace (m.group (), res) # Заменить результат выражения умножения и деления, и цикл, чтобы определить, есть ли выражение умножения и деления
                         print ('Результат \ n', формула)
        else:
                         print ('Расчет умножения и деления завершен')
            flag=False
         print ('Выражение после вычисления умножения и деления \ n', формула)
    result=calc_add_stract(formula)
    return  result
 def calc_add_stract (formula): # Вычислить все сложения и вычитания
         print ('Вычислить выражение сложения и вычитания \ n', формула)
    formula=format_formula(formula)
         print ('Выражение минус после обработки знака \ n', формула)
 
         # Для выражения сложения и вычитания-становится + -, чтобы разделить на список для вычисления сокращения
    formula=formula.replace('-','+-')
    formula_list=formula.split('+')
         print ('Список после разделения равен \ n', formula_list) # Первое число отрицательное, тогда первое поле списка пусто
    if formula_list[0]=='':
        formula_list=formula_list[1:]
    result=0
    '''
    for i in formula_list:
        if '-' in i:
            stract_list = i.split('-')
            result = float(stract_list[0]) - float(stract_list[1]) + result
        else:
            result += float(i)
    '''
    result = reduce(lambda x, y: float(x) + float(y), formula_list)
    return str(result)
 
 
 
def format_formula(formula):
    formula=  formula.replace('--','+')
    formula = formula.replace('-+', '-')
    formula = formula.replace('++', '+')
    formula = formula.replace('+-', '-')
    return formula
 
 
 def calc_mul_div (formula): # Вычислить одно выражение умножения и деления
         print ('Вычислить выражение умножения и деления \ n', формула)
    first_list=re.split('[*/]',formula)
         print ('Список выражений однократного умножения и деления \ n', first_list)
    res=0
    if '*' in formula:
        res=float(first_list[0])*float(first_list[1])
    elif '/' in formula:
        res=float(first_list[0])/float(first_list[1])
    return str(res)
def calc(formula):
    flag=True
    while flag:
        tmp=re.search('\([^()]*\)',formula)
        if tmp:
                         print ('Соответствует \ n', tmp.group ())
            sub_formula=tmp.group().strip('()')
                         res = sub_calc (sub_formula) # Сначала вычислить выражение в круглых скобках
                         formula = formula.replace (tmp.group (), res) # Замените исходные скобки на результат, вычисленный по выражению, и повторите цикл, чтобы определить, есть ли скобки
                         print ('Вычисленная строка \ n', формула)
        else:
            flag=False
         print ('Последняя строка \ n', формула)
    result=sub_calc(formula)
    return result
 
 
if __name__=='__main__':
    formula='1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )'
    formula=formula.replace(' ','')
         print ('Строка после удаления пробелов равна \ n', формула)
    ret=calc(formula)
         print ('Окончательный результат вычисления \ n', ret)
    #2776672.6952380957