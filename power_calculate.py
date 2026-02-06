def check_power(num:int,pow:int)->int:
    '''
    Calculates num raised to the power of pow using multiplication.

    Args:num (int): Base number.
         pow (int): Power (must be a non-negative integer).

    Returns: int: Result of num ** pow.

    Raises:
        TypeError: If num or pow is not an integer.
        ValueError: If pow is negative.
    '''
    
    if not isinstance(num, int) or not isinstance(pow, int):
        raise TypeError("Both num and pow must be integers")

    if pow < 0:
        raise ValueError("Power must be a non-negative integer")

    total =num
    for i in range(1,pow):
        print(total,num,i)
        total *=num
    return total
if __name__ == "__main__":
    try:
        print(check_power(3,2))
    except TypeError as t:
        print("Error:",t)

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")
