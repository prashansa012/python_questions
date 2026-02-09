def char_Occurrences_count(word:str)->dict:
    """
     Counts the occurrences of each character in a given string.

    Args:
        word (str): Input string whose characters are to be counted.

    Returns:
        dict: A dictionary where keys are characters and values are
              their corresponding occurrence counts.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    char_count= {}
    for char in word:
        char_count[char] = char_count.get(char,0)+1
    return char_count
if __name__ == "__main__":
    try:
        print(char_Occurrences_count("hello"))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error:",e)
