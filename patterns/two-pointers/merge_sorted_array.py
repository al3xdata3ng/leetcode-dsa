def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

if __name__ == "__main__":

    nums1 = [1,4,4,5,6,9,0,0,0,0,0,0]
    m = 6
    nums2 = [1,2,2,6,8,10]
    n = 6   

    merge(nums1, m, nums2, n)
    print(nums1)  # Expected output: [1,1,2,2,4,4,5,6,6,8,9,10]