l=[5,6,7,8,9,10,11,12,13,14]
def binar_search(some_list,x):
    left=0 
    right=len(some_list)-1
    mid=(left+right)//2
    if x==some_list[mid]:
        return mid
    if x>some_list[mid]:
        return binar_search(some_list[mid+1:],x)+(mid+1)
    return binar_search(some_list[:mid],x)
print(binar_search(l,12))