def second_largest(nums:list)->int:
    """
    Return the second largest value, or None if it does not exist.
    
    :param nums: takes a list as a input
    handles type error if it does not gets list as input or if all the value inside a list is not float or int
    """
    if not isinstance(nums,list):
        raise TypeError("Input must be a list")
    if not all(isinstance(i, (int, float)) for i in nums):
        raise TypeError("List must contain only numbers")
  

    largest = nums[0]
    for i in nums[1:]:
        
        if i>largest:
            largest=i

    sec_largest = None
    for i in nums:
        if i!= largest:
            if sec_largest is None or i>sec_largest:
                sec_largest=i
    return sec_largest

if __name__ == '__main__':
    try:
        print(second_largest({1,3,4}))
    except TypeError as t:
        print("an error occurred",t)
    except Exception as e:
        print("an error occurred",e)