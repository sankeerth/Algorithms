"""
76. Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window in s which will contain all the characters in t. 
If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
"""


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = Counter(t)
        res, minimum = "", float('inf')
        start, count = 0, len(t)
        
        for end, c in enumerate(s):
            if c in counter:
                if counter[c] > 0:
                    count -= 1
                counter[c] -= 1
            
            while count == 0 and start <= end:
                c = s[start]
                if c in counter:
                    counter[c] += 1
                    if counter[c] > 0:
                        count += 1
                if end-start+1 < minimum:
                    res = s[start:end+1]
                    minimum = end-start+1
                start += 1

        return res


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("ACDFEBDAC", "CAB"))
print(sol.minWindow("ACBFEBDAC", "CAB"))
print(sol.minWindow("ACDFEBDAC", "BA"))
print(sol.minWindow("ACBFEBDAC", "CA"))
print(sol.minWindow("cabefgecdaecf", "cae"))
print(sol.minWindow("aaaaaaaaaaaabbbbbcdd", "abcdd"))
print(sol.minWindow("abdebc", "abc"))
print(sol.minWindow("abdbbbcade", "abc"))
print(sol.minWindow("a", "aa"))


"""
For most substring problem, we are given a string and need to find a substring of it which satisfy some restrictions. A general way is to use a hashmap assisted with two pointers. The template is given below.

int findSubstring(string s) {
        vector<int> map(128,0);
        int counter; // check whether the substring is valid
        int begin=0, end=0; //two pointers, one point to tail and one  head
        int d; //the length of substring

        for() { /* initialize the hash map here */ }

        while(end<s.size()){

            if(map[s[end++]]-- ?){  /* modify counter here */ }

            while(/* counter condition */){ 
                 
                 /* update d here if finding minimum*/

                //increase begin to make it invalid/valid again
                
                if(map[s[begin++]]++ ?){ /*modify counter here*/ }
            }  

            /* update d here if finding maximum*/
        }
        return d;
}
"""
