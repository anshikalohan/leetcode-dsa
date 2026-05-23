# LeetCode: 485. Max Consecutive Ones
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/max-consecutive-ones/

"""
Approach:
- Traverse the array and count consecutive 1s.
- If current element is 1:
    increment count
    update max_count
- If current element is 0:
    reset count to 0

Example:
[1,1,0,1,1,1]

Counts:
2 before first 0
3 after second sequence

Answer = 3
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        count = 0
        max_count = 0

        # Traverse array
        for i in range(len(nums)):

            # Consecutive 1 found
            if nums[i] == 1:
                count += 1

                # Update maximum count
                max_count = max(count, max_count)

            else:
                # Reset count when 0 appears
                count = 0

        return max_count


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- Count current streak of 1s.
- Reset count when 0 occurs.
- Track maximum streak using max_count.
- Simple traversal problem.
"""