"""
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG".
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].
"""
from typing import List


class Solution(object):
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        window_len = 10
        char_code = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        queue, res, hash_set = [], set(), set()
        cur_hash = 0

        if not s or len(s) <= window_len:
            return res

        for i in range(window_len):
            char = s[i]
            queue.append(char)
            cur_hash += char_code[char] * (4 ** (window_len - i))

        hash_set.add(cur_hash)
            
        for i in range(window_len, len(s)):
            cur_char = s[i]
            first_char = queue.pop(0)
            queue.append(cur_char)
            cur_hash -= char_code[first_char] * (4 ** (window_len))
            cur_hash *= 4
            cur_hash += char_code[cur_char] * 4

            if cur_hash in hash_set:
                res.add("".join(queue))

            hash_set.add(cur_hash)

        return list(res)


sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
