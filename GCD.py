def gcd(a: int, b: int)-> int:
    """
    Calculates the Greatest Common Divisor (GCD) of two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of the two integers.

    Raises:
        TypeError: If either input is not an integer.
        ValueError: If both inputs are zero.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers")
    if a == 0 and b == 0:
        raise ValueError("GCD is not defined for both values being zero")
    while b!= 0:
        a,b= b,a % b
    return a
if __name__ =="__main__":
    try:
        print(gcd(48,18))
    except TypeError as t:
        print("error:",t)
    except ValueError as v:
        print("error:",v)
    except Exception as e:
        print("error:",e)
    