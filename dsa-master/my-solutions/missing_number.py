# WARNING: works only if integers are starting from 1!

def missing_number(array: list[int]) -> int | None:
    n = len(array) + 1 
    expected_sum: int = int(n*(n + 1) / 2)
    actual_sum: int = sum(array) # O(n) time compexity

    return expected_sum - actual_sum


if __name__ == "__main__":

    array = [152, 164, 169, 153, 174, 157, 163, 168, 173, 154, 159, 172, 166, 167, 155, 162, 170, 176, 160, 165, 175, 178, 161, 171, 158, 180, 177, 156, 181, 183, 182, 186, 184, 185, 187, 188, 189, 190, 191, 192, 194, 195, 196, 197, 198, 193, 199, 200, 201, 202]

    print(missing_number(array=array))