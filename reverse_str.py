def reverse_string(input_str : str)->str:
    """
         this function will take a input from user as a string
         and will reverse the string by using a for loop 
         adding character one by one at the left
     Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(input_str,str):
        raise TypeError("Input must be a string")
    reverse = ''
    for i in input_str:
        reverse = i+ reverse
    return reverse
if __name__ == "_main_":
    try:
        input_str = input("enter string to reverse:")
        print(reverse_string(input_str))
    except TypeError:
        print("input must be string")
    except Exception as e:
        print("an error occurred",e)
