# LeetCode: 136. Single Number
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/single-number/

"""
Approach:
- Use XOR operation.

XOR Properties:
1. a ^ a = 0
2. a ^ 0 = a
3. XOR is commutative and associative

Since every element appears twice except one:
- Duplicate numbers cancel each other out.
- Remaining value is the single number.

Example:
[4,1,2,1,2]

4 ^ 1 ^ 2 ^ 1 ^ 2
= 4 ^ (1 ^ 1) ^ (2 ^ 2)
= 4 ^ 0 ^ 0
= 4
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        result = 0

        # XOR all elements
        for num in nums:
            result ^= num

        return result


# Time Complexity: O(n)
# Space Complexity: O(1)


"""
Short Notes:
- XOR removes duplicate numbers.
- Same numbers cancel each other.
- Final remaining number is the answer.
- Optimal constant space solution.
"""