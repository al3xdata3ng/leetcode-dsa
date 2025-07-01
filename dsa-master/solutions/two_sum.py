# problem statement url: https://leetcode.com/problems/two-sum/description/?utm_source=instabyte.io&utm_medium=referral&utm_campaign=interview-master-100

""" 
Brute force solution would be a double for loop, which would lead to O(n^2) time complexity.

Intuition for achieving O(n) time complexity:

Think of each iteration as an equation with a single unknown:
current_iteration_value = target - x => x = target - current_iteration_value

So the solution of the problem comes down to detecting the iteration which solves this equation.

Solution inspired from: https://instabyte.io/p/amazon-coding-challenge-netflix-design
"""

from typing import Optional

def two_sums(array: list[int], target: int) -> Optional[list]:

    idx_int_dict = {}
    for i, integer in enumerate(array):
        complement = target - integer # this would be the solution of our equation

        if complement in idx_int_dict:

            return [idx_int_dict[complement], i]
    
        idx_int_dict[integer] = i

if __name__ == "__main__":

    nums = [3,3]
    target = 6

    print(two_sums(array=nums, target=target))




