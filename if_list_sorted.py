def  is_lsit_sorted(nums:list)->bool:
    """
    is_lsit_sorted function checks the list if the list is sorted in accending order or not 
    
    :param nums:list
    :return:  a boolen value
    :raise :
    handles Type error if the in put is not a list
    """
    if not isinstance(nums,list):
        raise TypeError("input of the function should be list")
    length = (len(nums))
    for i in range(0,length-1):
        if nums[i]<nums[i+1]:
            continue
        else:
            return False
    return True
if __name__ == "__main__":
    try:
        print(is_lsit_sorted([1,3,5,7,9]))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error:",e)

