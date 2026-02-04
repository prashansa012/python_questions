def whitespace_remove(str1:str)->str:
    """
    whitespace_remove function removes all  spaces, tabs, newlines from the given string
    
    :param str1: string type  
    :return: a string without spaces, tabs, newlines
    :raise: Type error if the input is not string
    """
    if not isinstance(str1, str):
        raise TypeError("input must be a string")


    expected_output= "".join(filter(lambda x:x!=" ", str1))
    return expected_output
if __name__== "__main__":
    try:
        print(whitespace_remove("hello my name is prashansa"))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error:", e)

    