def missing_number(array: list[int]) -> int | None:
    n = len(array) + 1 
    expected_sum: int = int(n*(n + 1) / 2)
    actual_sum: int = sum(array) # O(n) time compexity

    return expected_sum - actual_sum


if __name__ == "__main__":

    array = [3, 5, 1, 4]

    print(missing_number(array=array))