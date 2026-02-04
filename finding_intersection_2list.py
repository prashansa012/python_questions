
def finding_intersection_in_two_lists(list1:list,list2:list)->list:
    """
    finding_intersection_in_two_lists ufnction returns a list which contains the common element of both the given lists  
    
    :param list1 and list2: list type

    :return: a list of common elements of 2 lists
    :raise: Type error if both the arguments are not list type
    """
    if not isinstance(list1,list) or not isinstance(list2,list):
        raise TypeError("input should be a list")
    final = list(filter(lambda x:x in list1,list2))
    return(final)
if __name__ == "__main__":
    try:
        print(finding_intersection_in_two_lists(['apple','banana', 'cherry'],['cherry', 'date', 'apple'] ))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error:", e)