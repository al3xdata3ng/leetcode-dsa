def threeSum(nums: list[int]) -> list[list[int]]:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    nums.sort()
    # print(nums)
    i = 0
    output = []

    while nums[i] < 0:
        k = i + 1
        j = len(nums) - 1

        while k < j:
            sum_ = nums[i] + nums[k] + nums[j]
            if sum_ == 0:
                output.append([nums[i], nums[k], nums[j]])
            elif sum_ < 0:
                k += 1
            elif sum_ > 0:
                j -= 1
        i += 1


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(
        threeSum(nums)
    )  # Expected output: [[-1, -1, 2], [-1, 0, 1]] i < len(nums) - 2:
