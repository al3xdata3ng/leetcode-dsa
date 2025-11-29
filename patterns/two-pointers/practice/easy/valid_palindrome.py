def isPalindrome(s: str) -> bool:
    """
    :type s: str
    :rtype: bool
    """
    i = 0
    j = len(s) - 1

    while i < j:
        while not s[i].isalnum() and i < len(s) - 1:
            i += 1

        while not s[j].isalnum() and j > 0:
            j -= 1

        if s[i].lower() != s[j].lower() and i < j:
            return False

        i += 1
        j -= 1

    return True


if __name__ == "__main__":
    string = "A man, a plan, a canal: Panama"
    print(isPalindrome(string))  # Output: True
    string = "race a car"
    print(isPalindrome(string))  # Output: False
    string = " "
    print(isPalindrome(string))  # Output: True
    string = ",."
    print(isPalindrome(string))  # Output: True
