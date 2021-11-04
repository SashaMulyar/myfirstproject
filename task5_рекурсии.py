l=[8,9,7,[7,[5,7],4],3]
def sum1(lst):
    total = 0
    for element in lst:
        if (type(element) == type([])):
            total = total + sum1(element)
        else:
            total = total + element
    return total
print("Сумма элементов равна:", sum1(l))




# while True:
#     try:
#         x = int(input('введите число==>>')) + 1
#         break  
#     except ValueError:
#         print('неверный ввод')
#         continue
# def fib(x):
#     if x==1:
#         return 0
#     if x==2:
#         return 1
#     return fib(x-1)+fib(x-2)
# def fiblist(x):
#     l = []
#     for i in range(1,x):
#         b = fib(i)
#         l.append(b)
#     return (', '.join(map(str,l)))
# print(fiblist(x))