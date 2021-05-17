"""
767. Reorganize String

Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].
"""
import heapq


class Solution:
    def reorganizeString(self, S: str) -> str:
        heap = [(-S.count(c), c) for c in set(S)]
        maxCount = -1 * min(heap, key=lambda x: x[0])[0]
        # char with highest count sits at alternate pos and there must be at least (l+1) char in S (including m)
        # for a string with no same adjacent char
        if maxCount > (len(S) + 1) / 2: # derived from -> (m*2)-1-m > l-m
            return ""

        res = []
        heapq.heapify(heap)
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            
            res.append(char1)
            res.append(char2)

            if count1 + 1 < 0:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 + 1 < 0:
                heapq.heappush(heap, (count2 + 1, char2))

        # remaining char in heap must have a count of 1 else it will be an invalid case which must be handled above
        if heap:
            _, char = heapq.heappop(heap)
            res.append(char)
                
        return "".join(res)


s = Solution()
print(s.reorganizeString("a"))
print(s.reorganizeString("bb"))
print(s.reorganizeString("aba"))
print(s.reorganizeString("aaba"))
print(s.reorganizeString("aaaavvv"))
print(s.reorganizeString("aaaavvvv"))
print(s.reorganizeString("aaaavvvccc"))
print(s.reorganizeString("aaaaabb"))
print(s.reorganizeString("aaaaabbb"))
print(s.reorganizeString("aaaabbccxz"))
print(s.reorganizeString("aaaaabbccxz"))


"""
My other solution that is fast! (p99.36%):

class Solution:
    def reorganizeString(self, S: str) -> str:
        res = []
        counter = Counter(S)
        sortedCount = sorted(counter.items(), key=lambda x: x[1])

        high = sortedCount[-1][1]
        if high-1 > len(S)-high:
            return ""
        
        for c, count in sortedCount:
            for i in range(0, count):
                res.insert(i*2, c)

        return "".join(res)
"""
