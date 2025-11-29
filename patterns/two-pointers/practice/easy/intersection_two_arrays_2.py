from collections import Counter

def intersect(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    c1, c2 = Counter(nums1), Counter(nums2)
    intersection = []

    for i in c1.keys():
        for j in c2.keys():
            if i == j:
                intersection.extend([i] * min(c1[i], c2[j]))
    
    return intersection


if __name__ == "__main__":
    arr1 = [1, 2, 2, 1]
    arr2 = [2, 2]
    print(intersect(arr1, arr2))  # Output: [2, 2]

# https://leetcode.com/problems/intersection-of-two-arrays-ii/solutions/1468295/python-2-approaches-3-follow-up-question-ka3i/