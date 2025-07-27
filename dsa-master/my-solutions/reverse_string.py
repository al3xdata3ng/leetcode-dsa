def reverse_string(string: list) -> None:

    left = 0
    right = len(string) - 1

    while left <= right:

        string[left], string[right] = string[right], string[left]

        left += 1
        right -= 1

if __name__ == "__main__":

    string = ['h', 'e', 'l', 'l', 'o']

    reverse_string(string=string)
    print(string)

