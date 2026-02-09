def reverse_string(input_wod : str)->str:
    """
         this function will take a word from user as a string
         and will reverse the word by using a for loop 
         adding character one by one at the left
     Raises:
        TypeError: If the input is not a string.

    """
    if not isinstance(input_word,str):
        raise TypeError("Input must be a string")
    reverse = ''
    for char in input_word:
        reverse = char+ reverse
    return reverse
if __name__ == "__main__":
    try:
        input_word = input("enter word to reverse:")
        print(reverse_string(input_word))
    except TypeError:
        print("input must be string")
    except Exception as e:
        print("an error occurred",e)
