def moveZeroes(nums: list[int]) -> int:
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j], nums[i] = nums[i], nums[j]
            j += 1
    return j

if __name__ == "__main__":
    arr = [0, 1, 0, 3, 12]
    moveZeroes(arr)
    print(arr)  # Output: [1, 3, 12, 0, 0]