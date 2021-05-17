"""
567. Permutation in String

Given two strings s1 and s2, write a function to return true if s2 contains the permutation 
of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Constraints:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""
from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j= 0, 0
        s1Counter = Counter(s1)
        s2Counter = defaultdict(int)
        count, N = 0, len(s1)

        while j < len(s2):
            cur = s2[j]
            if cur not in s1Counter:
                s2Counter.clear()
                count = 0
                i = j+1
            elif s2Counter[cur] < s1Counter[cur]:
                s2Counter[cur] += 1
                count += 1
                if count == N:
                    return True
            else:
                while i < j:
                    if s2[i] == cur:
                        i += 1
                        break
                    s2Counter[s2[i]] -= 1
                    count -= 1
                    i += 1
            j += 1
        
        return False


s = Solution()
print(s.checkInclusion("ab", "eidbaooo"))
print(s.checkInclusion("aba", "eidbaooo"))
print(s.checkInclusion("aba", "aaa"))
print(s.checkInclusion("aba", "eidbaoobaomnabaa"))
print(s.checkInclusion("aba", "eidbaoobaomnbaa"))
#---- failed TCs -----
print(s.checkInclusion("adc", "dcda"))
print(s.checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))


"""
First solution that timed out.. Realized that the worst case would result in O(n^2)
where n is length of s1

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, N = 0, len(s1)
        s1Counter = Counter(s1)
        
        while i < len(s2):
            if s2[i] in s1Counter:
                j, count = i, 0
                s2Counter = defaultdict(int)
                while j < len(s2):
                    cur = s2[j]
                    if cur not in s1Counter or s2Counter[cur] >= s1Counter[cur]:
                        break
                    s2Counter[cur] += 1
                    count += 1
                    if count == N:
                        return True
                    j += 1
            i += 1

        return False
"""

"""
Leetcode solution:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # This problem is extremely the same as "Find All Anagrams in a String(LC .438)"
        # corner case
        if len(s1) > len(s2):
            return False
        # Focus on the constraint "The input strings only contain lower case letters."
        lst1, lst2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            lst1[ord(s1[i]) - ord("a")] += 1
            lst2[ord(s2[i]) - ord("a")] += 1
        if lst1 == lst2:
            return True
        for i in range(1, len(s2) - len(s1) + 1):
            lst2[ord(s2[i - 1]) - ord("a")] -= 1
            lst2[ord(s2[len(s1) + i - 1]) - ord("a")] += 1
            if lst1 == lst2:
                return True
        return False
"""

"""
Leetcode solution using maps, similar to mine:

class Solution(object):
    def checkInclusion(self, s1, s2):

        counter = collections.Counter(s1)  #create frequency list
        counterEmpty = counter.copy()

        for key in counterEmpty.keys():     #Empty frequency list to compare
            counterEmpty[key] = 0
        left = 0
        for i in range(0, len(s2)):         #Loop over all characters from s2
            if s2[i] in counter.keys():     #If current chr is in frequency, we subtract 1 from frequency
                counter[s2[i]] -= 1
            if i >= len(s1) - 1:            #If we len(s1) characters checked => a posible sollution
                if counterEmpty == counter:     #All of our frequency elements are zero => sollution
                    return True

                if s2[left] in counter.keys():        #Rebuild the frequency if s2[left] is a key
                    counter[s2[left]] += 1
                left += 1          #increasing the left pivot to allways have a len(k) sollution to check

        return False
"""
