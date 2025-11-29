def removeElement(nums: list[int], val: int) -> int:
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """

    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    k = removeElement(nums, val)
    print(k)  # Expected output: 2
    print(nums[:k])  # Expected output: [2, 2]
