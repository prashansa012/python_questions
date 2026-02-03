def binary_search(list_sorted:list,target:int)->int:
    if not isinstance(list_sorted,list):
        raise TypeError("given input must be a list")
    if not isinstance(target,int):
        raise TypeError("target must be a integer")
    lower = 0
    upper = len(list_sorted)-1
    while lower<=upper:
        mid = (upper+lower)//2
        if target == list_sorted[mid]:
            return(mid)
        elif target< list_sorted[mid]:
            upper = mid -1
        elif target>list_sorted[mid]:
            lower = mid +1
    else:
        return(-1)
    
if __name__ =="__main__":
    try:
        print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],14))
    except TypeError as t:
        print('type error occurred: ',t)
    except Exception as e:
        print("an error occured: ",e)

