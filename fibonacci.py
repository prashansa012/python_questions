def fibonacci(num:int)->list:
    '''
    function Generates a list of Fibonacci numbers up to num given.

    Args:num (int): Number of terms to generate (must be a positive integer)

    Returns:list: List containing Fibonacci sequence up to num terms

    Error: 
    '''
    if not isinstance(num, int):
            raise TypeError("num must be an integer")

    if num <= 0:
            raise ValueError("num must be a positive integer")
    a,b = 0,1
    list1 = [0]
    if num == 1:
        return 0
    for i in range(num-1):
        c = a +b
        b =a
        a= c
        list1.append(c)
    return list1
if __name__ == "__main__":
    try:
        print(fibonacci(10))
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")