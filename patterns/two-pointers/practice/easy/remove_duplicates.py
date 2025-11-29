def removeDuplicates(nums: list[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """

    k = 1

    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i]:
            nums[k] = nums[i + 1]
            k += 1

    return k


if __name__ == "__main__":
    nums = [1, 1, 2]
    k = removeDuplicates(nums)
    print(k)  # Expected output: 2
    print(nums[:k])  # Expected output: [1, 2]
