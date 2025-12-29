def largest_number(num: list)->int:
    """
    Returns the largest number from a list of numeric values.
    Args:
        num (list): A list containing integers or floats.
    Returns:
        int or float: The largest value in the list.
    Raises:
        TypeError: If the input is not a list or contains non-numeric elements.
        IndexError: If the list is empty.
    """
    if not isinstance(num, list):
        raise TypeError("Input must be a list")
 

    largest = num[0]
    for i in num:
        if not isinstance(i,(int,float)):
            raise TypeError(
                f"Invalid element type: {type(i)}"
            )
        if i>largest:
            largest = i
    return largest
if __name__ == "__main__":
    try:
        print(largest_number([1,6.7]))
    except TypeError as t:
        print(f"An error occurred: {t}")
        # print("input must be a list")
    except IndexError :
        print("list must have atleast 1 element")
    except Exception as e:
        print(f"An error occurred: {e}")