# LeetCode: 1752. Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

"""
Approach:
- A sorted and rotated array will have at most one "drop".
- A drop occurs when nums[i] > nums[i + 1].
- Use modulo (%) to compare the last element with the first element.

Example:
[3,4,5,1,2]
Only one drop: 5 > 1

[2,1,3,4]
Two drops:
2 > 1
4 > 2
So it is not valid.
"""

class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        n = len(nums)
        count = 0

        for i in range(n):

            # Check for decreasing point
            if nums[i] > nums[(i + 1) % n]:
                count += 1

        # Valid if at most one drop exists
        return count <= 1


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- Use modulo to handle circular comparison.
- Sorted rotated array => maximum one decreasing point.
- If drops > 1 => not sorted & rotated.
"""