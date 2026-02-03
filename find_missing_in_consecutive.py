def missing_consecutive_number(nums:list)->int:
    """
    missing_consecutive_number function  finds the missing number in a consecutive list

    
    :param nums: list type
    :return: returns a missing integer
    :raise: handles TypeError if the input is not a list
    """
    if not isinstance(nums,list):
        raise TypeError("input must be a list of integers")
    for i in range(0,len(nums)-1):
        if nums[i] == nums[i+1]-1:
            continue
        else:
            return( nums[i]+1)
if __name__ == "__main__":
    try:
        print("missing number is: ",missing_consecutive_number([10, 11, 12, 14, 15]))
    except TypeError as t:
        print("error: ",t)
    except Exception as e:
        print("error:",e)

    