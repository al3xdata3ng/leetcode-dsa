def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """

    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        length = right - left
        width = min(height[left], height[right])
        area = length*width

        if area > max_area:
            max_area = area
        
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return max_area

if __name__ == "__main__":
    print(maxArea([1,8,6,2,5,4,8,3,7]))  # Expected output: 49
    print(maxArea([1,1]))                # Expected output: 1