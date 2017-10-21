"""
49. Group Anagrams

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""
from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        char_to_prime_mapping = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                                 89, 97, 101]

        prime_sum_of_anagrams = defaultdict(list)
        result = list()

        for string in strs:
            prime_sum = 1
            for char in string:
                prime_sum *= char_to_prime_mapping[ord(char) - ord('a')]
            prime_sum_of_anagrams[prime_sum].append(string)

        for _, anagram_list in prime_sum_of_anagrams.items():
            result.append(anagram_list)

        return result

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
