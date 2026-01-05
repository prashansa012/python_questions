def palindrome(word: str)->bool:
    """
    Checks whether the given string is a palindrome.
    returns:
       a boolan if true or false
    Raises ValueError for invalid input.

    """
    if not isinstance(word, str):
        raise ValueError("Input must be a string")

    if word.strip() == "":
        raise ValueError("Empty string is not allowed")

    reverse = ""
    for char in word:
        reverse = char + reverse
    if word == reverse:
        return True
if __name__ == "__main__":
    try:
        word = input("enter the word to check whether palindrome or not: ").lower()
        if palindrome(word):
            print("String is a palindrome")
        else:
            print("String is not a palindrome")
    except ValueError as v:
        print(f"Error: {v}")
    except Exception as e:
        print(f"Unexpected error: {e}")

