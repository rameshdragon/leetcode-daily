# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium

from collections import defaultdict

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagram_map = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        anagram_map[key].append(s)
    return list(anagram_map.values())
