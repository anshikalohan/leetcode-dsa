# LeetCode: 217. Contains Duplicate
# Difficulty: Easy
# Topic: Arrays
# Link: https://leetcode.com/problems/contains-duplicate/

"""
Approach:
- Use a set to keep track of visited elements.
- Traverse the array:
    - If element already exists in set:
        duplicate found -> return True
    - Otherwise add element to set
- If traversal completes, no duplicates exist.

Example:
[1,2,3,1]

1 -> add
2 -> add
3 -> add
1 -> already in set -> return True
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()

        # Traverse array
        for num in nums:

            # Duplicate found
            if num in seen:
                return True

            seen.add(num)

        return False


# Time Complexity: O(n)
# Space Complexity: O(n)


"""
Short Notes:
- Set provides O(1) average lookup.
- If element already exists in set => duplicate.
- Simple hashing-based approach.
"""