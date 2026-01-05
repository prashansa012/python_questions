def factorial(num: int)->int:
    """
    takes a integer from user
    Returns the factorial of a non-negative integer.
    Raises 
        ValueError for invalid or negative input.
    """
    if not isinstance(num, int):
        raise ValueError("input must be int type")
    if num <= 0:
        raise ValueError("factorial is not defined for negative numbers or zero")

    result = 1
    for fact in range(1,num+1):
        result = result*fact
    return result

if __name__ == "__main__":
    try:
        number = int(input("enter the number to check its factorial:"))
        print(factorial(number)," if number is ",number)
    except ValueError as v:
        print(f"An error occurred: {v}")
    except Exception as e:
        print(f"An error occurred: {e}")

