def twoSum(numbers: list[int], target: int) -> list[int]:
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
        """
    
    left = 0
    right = len(numbers) - 1

    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left + 1, right + 1]
        elif numbers[left] + numbers[right] > target:
            right -= 1
        elif numbers[left] + numbers[right] > target:
            left += 1

if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # [1, 2]
    print(twoSum([2, 3, 4], 6))       # [1, 3]
    print(twoSum([-1, 0], -1))        # [1, 2]
