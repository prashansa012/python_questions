def reverse_int(num:int)->int:
    """
    Reverse the digits of an integer.
    Preserves the sign for negative numbers.
    Raises TypeError if input is not an integer.
    """
    if not isinstance(num,int):
        raise TypeError("Input must be a integer only")

    rev_num = 0
    negative =False
    if num<0:
        negative= True
        num *= (-1)
    while num>0:
        r =  num% 10
        num = num// 10
        rev_num = r + rev_num*10
    if negative:
        return (rev_num *(-1))
    else:
        return (rev_num)
if __name__ == '__main__':
    try:   
        number = int(input("enter a Number to reverse:"))
        print(reverse_int(number))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error: ",e)
