def is_leap_year(yr:int)->bool:
    """
    Checks whether a given year is a leap year.
    A year is a leap year if:
    It is divisible by 4 and not divisible by 100, OR
    It is divisible by 400

    Args: yr (int): Year to be checked

    Returns:
        bool: True if leap year, False otherwise
    raise:
        typeError: if year is not integer
        valueError: if year is not positive
    """
    if not isinstance(yr, int):
            raise TypeError("Year must be an integer")

    if yr <= 0:
            raise ValueError("Year must be a positive integer")
    if (yr%4 == 0 and yr%100 !=0) or yr%400 ==0:
        return True
    else:
        return False
if __name__ == "__main__":
    try:
        print(is_leap_year(1900))
    except TypeError as t:
        print(f"Type Error: {t}")   
    except ValueError as v:
        print(f"Value Error: {v}")

    except Exception as e:
        print(f"Unexpected Error: {e}")