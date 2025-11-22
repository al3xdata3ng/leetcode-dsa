def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    
    res = []
    i = 0
    j = 0

    while i <= m - 1:
        if nums1[i] > nums2[j]:
            res.append(nums2[j])
            j += 1
        else:
            res.append(nums1[i])
            i += 1
    res.extend(nums2[j:])

    return res  

if __name__ == "__main__":

    nums1 = [1]
    m = 1
    nums2 = []
    n = 0   

    print(merge(nums1, m, nums2, n))