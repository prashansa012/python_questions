def factorial(num:int)->int:
    """
    getting factorial of a given number using recursion
    
    :param num: as integer
    :return: an int value 
    :error handling: handelling type error if input is not an integer and
                     value error if value is in negitive
    """
    if not isinstance(num,int):
        raise TypeError("the input must be integer type")
    if num<0 :
        raise ValueError("input must be a positive number")
    fact = 1
    if num==0 or num==1:
        return 1
    else:
        fact = num * factorial(num-1)
    return fact
if __name__ == "__main__":

    try:
        print(factorial(6))
    except TypeError as t:
        print("type error occurred:", t)
    except ValueError as v:
        print("value error occurred:",v)
    except Exception as e:
        print("an error occured",e)