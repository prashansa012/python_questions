def Decimal_to_binary(num:int)->int:
    """
    Decimal_to_binary function converts a decimal number to binary number
    accepts a decimal and returns its binary 
    :param num: must be a integer type 
     
    raise:
    handles typeError if the input is not integer type
    """
    if not isinstance(num,int):
        raise TypeError("input must be a integer")
    bin = []
    if num == 0:
        return 0
    while num>0:
        quotient = num//2
        rem = num% 2
        num = quotient
        bin.append(str(rem))
    binary ="".join(bin)[::-1]
    return(int(binary))
if __name__ == "__main__":
    try:
        decimal = int(input("decimal="))
        binary_num = Decimal_to_binary(decimal)
        print(binary_num,f"(the binary representation of {decimal} is {binary_num} )")
    except TypeError as t:
        print("error:" , t)
    except Exception as e:
        print("error:",e)
