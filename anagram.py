def check_anagram(word1:str, word2:str)->bool:
    """
    Checks whether two strings are anagrams of each other.

    Args:
    word1 (str): First input string.
    word2 (str): Second input string.

    Returns:
        bool: True if both strings are anagrams, otherwise False.

    Raises:
        TypeError: If either input is not a string.
    """
    if not isinstance(word1,str) or not isinstance(word2, str):
        raise TypeError("Input must be string")
    dict = {}

    if len(word1) != len(word2):
        return False
    else:

        for ch in word1:
            if ch in dict:
                dict[ch] +=1
            else:
                dict[ch] =1
        for ch in word2:
            if ch not in dict:
                return False
            dict[ch]-= 1

            if dict[ch]<0:
               return False
              
        else:
            return True
if __name__ == "__main__":
    try:
        print(check_anagram("helo","hllo"))
    except TypeError as t:
        print("error:",t)
    except Exception as e:
        print("error:",e)