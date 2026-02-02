def even_num_generater(num:int)->list:
    """
    this function returns a list of even number upto given input integer
    Error Handling: it handles a type error when the input is not a integer type.
    """
    if not isinstance(num,int):
        raise TypeError("input must be a integer")
    even_list=[]
    for i in range(2,num+1):
        if i%2 == 0:
            even_list.append(i)
    return even_list
if __name__ == "__main__":
    try:
        print(even_num_generater(9))
    except TypeError as t:
        print("a type error occurred:",t)
    except Exception as e:
        print("an error ocured:",e)