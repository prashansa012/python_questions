def digit_sum(num:int)->int:
    """
    Returns the sum of a given number
    
    :param: takes a digit as input an returns int
    :Error handling: handles value error if the input is not intiger type 
    """
    if not isinstance(num,int) :
        raise ValueError("input should be only integer type")
   
    total=0
    while num>0:
        digit = num%10
        total += digit
        num //= 10
    return total


if __name__ == "__main__":
    try:
        print(digit_sum(12345))
    except ValueError as v:
        print("a Value error occured:",v)
    except Exception as e:
      print("an error occurred",e)


