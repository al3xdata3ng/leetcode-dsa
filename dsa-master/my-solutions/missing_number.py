# WARNING: works only if integers are starting from 1!


def missing_number(array: list[int]) -> int | None:
    n = len(array)
    expected_sum: int = int(n * (n + 1) / 2)
    actual_sum: int = sum(array)  # O(n) time compexity

    return expected_sum - actual_sum


if __name__ == "__main__":
    array = [
        34,
        41,
        19,
        33,
        26,
        22,
        7,
        10,
        12,
        36,
        4,
        5,
        20,
        14,
        2,
        16,
        30,
        46,
        21,
        28,
        17,
        24,
        1,
        43,
        18,
        0,
        40,
        3,
        13,
        9,
        8,
        38,
        27,
        47,
        32,
        45,
        39,
        25,
        6,
        15,
        48,
        29,
        11,
        44,
        42,
        49,
        37,
        23,
        31,
        35,
    ]

    print(missing_number(array=array))
