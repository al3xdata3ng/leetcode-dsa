from typing import Optional
# 0 --> -1
# 1 --> -2
# 2 --> -3
# 3 --> -4

def valid_parentheses(string: str) -> Optional[bool]:

    mid_way = int(len(string) / 2)

    for i in range(0, mid_way):
        print(string[i], string[-(i + 1)])
        if not( \
             (
            string[i] == "(" and string[-(i + 1)] == ")" \
            ) \
            or \
            (
            string[i] == "[" and string[-(i + 1)] == "]" \
            ) \
            or \
            (
            string[i] == "{" and string[-(i + 1)] == "}" \
            )
        ):
            return False
    return True
    
if __name__ == "__main__":

    string = "{[[{()}]]}"
    print(valid_parentheses(string=string))





        