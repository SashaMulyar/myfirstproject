while True:
    try:
        l= [int(i) for i in input('введите целые числа через пробел ').split( )]
        break  
    except (IndexError, ValueError, TypeError):
        print('Данные введены неккоректно')
        continue
def get_ranges(arg):
    arg=sorted(list(set(arg)))
    str_arg=''
    previous_num=arg[0]-1
    start_num=0
    for i in arg:
        if start_num==0:
            start_num=i

        if previous_num+1!=i:
            if start_num==i:
                str_arg+=f'{i}, '
            else:
                str_arg+=f'{start_num}-{previous_num}, '
            start_num=i
        if arg[-1]==i:
            if arg[-1]==start_num:
                str_arg+=f'{i}'
            else:
                str_arg+=f'{start_num}-{i}'
                    
        previous_num=i
    return ''.join(str_arg)   
print(get_ranges(l))

# # def is_int(*args):
# #         try:
# #             for i in args:
# #                 int(i)
# #             return True
# #         except ValueError:
# #             print('нужно ввести целое число')
# #             return False
# while True:
#     total_bill=(input('введите сумму общего счета===>>>'))
#     try:
#         total_bill=int(total_bill)
#         assert int(total_bill)
#         break
#     except ValueError:
#         print('введите целое число')
#     amount_of_participants=(input('введите количество участников (от 2)===>>>'))
#     # is_int(amount_of_participants) 
#     sums=[]
#     for i in range(amount_of_participants):
#         a=(input(f'введите сумму {i+1} участника ===>>>'))
#         sums.append(a)
#     # is_int(total_bill,amount_of_participants,a)
#     break

# # def calculation_dept(arg1l, arg2, arg3):
# #     average_bill=arg1l/arg2
# #     for i in range(arg2):
# #         if average_bill-arg3[i]>=0:
# #             print(f'участник {i+1} должен {average_bill-arg3[i]}' )
# # calculation_dept(total_bill, amount_of_participants, sums)




