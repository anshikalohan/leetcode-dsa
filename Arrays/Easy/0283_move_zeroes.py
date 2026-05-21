# LeetCode: 283. Move Zeroes
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/move-zeroes/

"""
Approach:
- Use two pointers.
- j keeps track of position where next non-zero element should go.
- Traverse array with i:
    - If nums[i] is non-zero:
        swap nums[i] and nums[j]
        increment j

This moves all non-zero elements to the front
while maintaining relative order.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """

        j = 0

        # Traverse array
        for i in range(len(nums)):

            # Place non-zero element at correct position
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]

                j += 1


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- Two pointers technique.
- j stores position for next non-zero element.
- Maintains relative order of non-zero elements.
- In-place solution with constant space.
"""