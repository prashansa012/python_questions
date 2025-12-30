def is_prime(num: int)->str:
    """
    Returns if the number is a prime or not 
    Args:
      num as a int is passed
    returns:
      returns a msg
    Raises:
       ValueError: If the input is not a number
    """
    if not isinstance(num, int):
        raise ValueError("input must be int type")

    for i in range(2,num):
        if (num%i == 0):
            return (num,"is not a prime number")
            break
    else:
        return(num,"is  a prime number")

if __name__ == "__main__":
    try:
        num = int(input("enter the number to check: "))
        print(is_prime(num))
    except ValueError:
        print("input must be int type")
    except Exception as e:
        print(f"An error occurred: {e}")