
def remove_duplicates(nums:list)->list:
    if not isinstance(nums,list):
        raise TypeError("the input must be list type")
    if not all(isinstance(i, int) for i in nums):
        raise TypeError("list must contain integer type")
    new_list = []
    for i in nums:
        if i not in new_list:
            new_list.append(i)
    return new_list

if __name__ == "__main__":
    try:
        print(remove_duplicates([1,2,3,2,3,4,5]))
    except TypeError as t:
        print("a Type error occurred:",t)
    except Exception as e:
        print("an error occurred :", e)