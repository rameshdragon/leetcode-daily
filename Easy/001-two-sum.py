"""
LeetCode 001: Two Sum
Difficulty: Easy
Date Solved: 2026-04-14

Problem:
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            if complement in hash_map:
                return [hash_map[complement], i]
            
            hash_map[num] = i
        
        return []

# Test
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))  # [0, 1]