def count_vowels(str_input : str)->int:
    """
    Counts the number of vowels in a string.
    Raises ValueError if input is not a valid string.
    """
    
    if str_input.isdigit():
        raise ValueError("Input must be a string, not a number")

    if str_input.strip() == "":
        raise ValueError("Empty string is not allowed")

    vowels = ("a","e","i","o","u")
    count =0
    for char in str_input:
        if char in vowels:
            count += 1
    return count
if __name__ == "__main__":
    try:
      str_input = input("enter string to count vowels in it:").lower()
      print(f'"{str_input}" word has ',count_vowels(str_input),'vowel')
    except ValueError as v:
      print(f"Error: {v}")
    except Exception as e:
      print("an error occurred",e)