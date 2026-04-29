# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
