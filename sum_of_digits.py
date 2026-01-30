def digit_sum(num:str)->int:
    """
    Returns the sum of a given string
    
    :param: takes a string as input an returns int
    :Error handling: handles value error is the input is not string 
    or if there is any other value then a digit inside the string
    """
    if not isinstance(num,str) :
        raise ValueError("input should be only string type")
    if not all(isinstance(i, (str)) for i in num):
        raise ValueError("input string must contain number in it")
  
    total=0
    for i in num:
        total += int(i)
    return total

if __name__ == "__main__":
    try:
        print(digit_sum("24321"))
    except ValueError as v:
        print("a Value error occured:",v)
    except Exception as e:
      print("an error occurred",e)
