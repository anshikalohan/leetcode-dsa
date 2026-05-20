# LeetCode: 26. Remove Duplicates from Sorted Array
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

"""
Approach:
- Since the array is sorted, duplicates are adjacent.
- Use two pointers:
    i -> points to last unique element
    j -> scans the array
- When a new unique element is found:
    - move i forward
    - place nums[j] at nums[i]

Example:
Input: [1,1,2]
After processing:
[1,2,_]

Return: 2
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Edge case
        if not nums:
            return 0

        i = 0

        # Traverse array
        for j in range(1, len(nums)):

            # Found new unique element
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        # Length of unique elements
        return i + 1


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- Two pointers technique.
- Array is sorted, so duplicates are consecutive.
- i tracks unique elements position.
- In-place modification required.
"""