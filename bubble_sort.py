my_list = [85,47,96,26,94,79,64,76,16,20]
def bubble_sort(my_list:list)->list:
    """
    bubble_sort function sort the list using bubble method by comparing 2 elements 
    
    :param my_list: list type
    :return: sorted list
    :raise: Type error if the input is not a list of integers
    """
    if not isinstance(my_list,list):
        raise TypeError("input must be list type")
    for val in my_list:
        if not isinstance(val,int):
            raise TypeError("each element must be a integer")

    for i in range(0,len(my_list)):
        for j in range(0,len(my_list)-i-1):
            if my_list[j]>my_list[j+1]:
                my_list[j],my_list[j+1] = my_list[j+1],my_list[j]
    return(my_list)

if __name__ == "__main__":
    try:
        print(bubble_sort([85,47,96,"1",94,79,64,76,16,20]))
    except TypeError as t:
        print("error:", t)
    except Exception as e:
        print("error:", e)

