# problem statement url: https://leetcode.com/problems/two-sum/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

""" 
Steps:

1. Sort array with quick sort or merge sort - O(nlogn)
2. Iterate over the array and calculate the some of two consecutive elements
"""

def sort_array(array: list) -> list | None:

    array.sort()

    return array

def two_sum(nums: list[int], target:int) -> list[int] | None:

    sorted_array = sort_array(array=nums) # O(nlogn)

    for index in range(len(sorted_array)): # O(n)
        consecutive_sum = sorted_array[index] + sorted_array[index + 1]

        if consecutive_sum == target:
            return [index, index + 1]
            break

if __name__ == "__main__":

    nums = [2,7,11,15]
    target = 9 

    output = two_sum(nums=nums, target=target)

    print(output)