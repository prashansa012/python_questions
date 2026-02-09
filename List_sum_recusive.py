def list_sum(nums:list)->int:
    """
    Calculates the sum of all numeric elements in a list.
    Args:
        nums (list): A list containing numeric values.
    Returns:
        int: Sum of all elements in the list. Returns 0 for an empty list.

    Raises:
        TypeError: If the input is not a list or contains non-numeric values.
    """
    if not isinstance(nums, list):
        raise TypeError("Input must be a list")
    total = 0
    if len(nums)==0:
        return 0
    else:
        while len(nums)>=1:
            if len(nums) ==1:
                return nums[0]
            else:
                popped = nums.pop()
                total = popped + list_sum(nums)
                return total

if __name__ == "__main__":
    try:
        print(list_sum([1,2,3,4,5,6]))
    except TypeError as t:
        print(f"Type Error: {t}")   
    except Exception as e:
        print(f"Unexpected Error: {e}")