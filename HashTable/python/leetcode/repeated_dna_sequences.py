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
from collections import deque


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []

        alpha_to_code = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        dict_dna_seq = dict()
        dq = deque()
        repeated_dna_seq = set()
        sliding_window = 10
        prev_hash = 0

        for i in range(sliding_window):
            dq.append(s[i])
            prev_hash += alpha_to_code[s[i]] * (4 ** (sliding_window - i))

        dict_dna_seq[prev_hash] = 1

        for i in range(sliding_window, len(s)):
            dq.popleft()
            dq.append(s[i])
            curr_hash = prev_hash - (alpha_to_code[s[i - sliding_window]] * (4 ** sliding_window))
            curr_hash *= 4
            curr_hash += 4 * alpha_to_code[s[i]]

            if curr_hash in dict_dna_seq:
                repeated_dna_seq.add(''.join(dq))
            else:
                dict_dna_seq[curr_hash] = 1

            prev_hash = curr_hash

        return list(repeated_dna_seq)

sol = Solution()
print(sol.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
