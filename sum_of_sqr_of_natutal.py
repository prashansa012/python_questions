def sum_of_sqr(num:int)->int:
    """
   sum_of_sqr functions retuns te sum of square of n natural numbers given by the user

    :type num: int
    :return: number , sum of all the squares
    :error handling: handles TypeError if the given input is not a number
    """
    if not isinstance(num,int):
        raise TypeError("input must be a integer type")
    
    sum = 0
    for i in range(1,num+1):
        sum += i**2
    return sum
if __name__ == "__main__":
    try:
        print(sum_of_sqr(12))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error" , e)


