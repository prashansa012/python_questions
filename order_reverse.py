def str_order_reverse(str1:str)->str:
    """
    this function reverse the order of given string 

    argument:
    takes a string as an input

    raise:
    handles Type error if the input is not string type
    """
    if not isinstance(str1,str):
        raise TypeError("given input must be a string")
    
    split_str = str1.split()
    reversed_str =[]
    for word in split_str[::-1]:
        reversed_str.append(word)
    return(" ".join(reversed_str))
if __name__ == "__main__":
    try:
        print(str_order_reverse("Python is fun"))
    except TypeError as t:
        print("error:", t)
    except Exception as e:
        print("an error occurred: ",e)
    
