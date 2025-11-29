def isSubsequence(s: str, t: str) -> bool:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if s == "": return True

    i = 0 
    j = 0

    while i < len(t) and j < len(s):

        if t[i] == s[j]:
            j += 1
        i += 1

    return j == len(s)

if __name__ == "__main__":
    print(isSubsequence("abc", "ahbgdc"))  # True
    print(isSubsequence("axc", "ahbgdc"))  # False