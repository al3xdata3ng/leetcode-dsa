def valid_parentheses(parentheses_seq: str) -> bool | None:

    parentheses_pairs_dict: dict = {")": "(", "}": "{", "]": "["}

    stack = []
    for p in parentheses_seq:
        if p not in parentheses_pairs_dict.keys():
            stack.append(p)
        elif stack[-1] == parentheses_pairs_dict[p]:
            stack.pop()

    return len(stack) == 0

if __name__ == "__main__":

    string = "(]"
    print(valid_parentheses(parentheses_seq=string))