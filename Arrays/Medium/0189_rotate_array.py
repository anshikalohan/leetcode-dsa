# LeetCode: 189. Rotate Array
# Difficulty: Medium
# Topic: Arrays
# Link: https://leetcode.com/problems/rotate-array/

"""
Approach:
Use the Reversal Algorithm.

Steps:
1. Reverse the entire array
2. Reverse first k elements
3. Reverse remaining elements

Example:
nums = [1,2,3,4,5,6,7], k = 3

Step 1:
[7,6,5,4,3,2,1]

Step 2:
[5,6,7,4,3,2,1]

Step 3:
[5,6,7,1,2,3,4]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        # Handle cases where k > n
        k = k % n

        # Helper function to reverse array portion
        def reverse(left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]

                left += 1
                right -= 1

        # Reverse whole array
        reverse(0, n - 1)

        # Reverse first k elements
        reverse(0, k - 1)

        # Reverse remaining elements
        reverse(k, n - 1)


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- Uses reversal technique for in-place rotation.
- k % n handles large rotations.
- Three reversals achieve final rotated array.
- Optimized solution with constant extra space.
"""