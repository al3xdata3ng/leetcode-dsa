def reverseVowels(s: str) -> str:
    """
    :type s: str
    :rtype: str
    """
    
    vowels =  ['a', 'e', 'i', 'o', 'u']

    i = 0
    j = len(s) - 1
    s = list(s)

    while i < j:

        while i < j and s[i].lower() not in vowels:
            i += 1 

        while i < j and s[j].lower() not in vowels:
            j -= 1 

        s[i], s[j] = s[j], s[i]

        i += 1 
        j -= 1
    
    return "".join(s)


if __name__ == "__main__":
    s = "hello"
    print(reverseVowels(s))  # holle

    s = "leetcode"
    print(reverseVowels(s))  # leotcede