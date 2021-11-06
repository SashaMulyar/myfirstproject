l=[4,5,6,7,8,9,10,11,12,13,14,15]
# def binar_search(some_list,x):
#     left=0 
#     right=len(some_list)-1
#     mid=(left+right)//2
#     if x==some_list[mid]:
#         return mid
#     if x>some_list[mid]:
#         return binar_search(some_list[mid+1:],x)+(mid+1)
#     return binar_search(some_list[:mid],x)
# print(binar_search(l,12))


def binary_search_recursive(some_list, x): 
    if len(some_list) == 0: 
        return 0 
    else: 
        mid = len(some_list)//2 
    if (x == some_list[mid]): 
        return l.index(x) 
    else: 
        if x > some_list[mid]: 
            return binary_search_recursive(some_list[mid+1:],x) 
        else: 
            return binary_search_recursive(some_list[:mid],x)
print(binary_search_recursive(l,8))

