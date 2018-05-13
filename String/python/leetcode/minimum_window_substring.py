"""
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
If there is no such window in S that covers all characters in T, return the empty string "".

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
"""


from collections import Counter


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s:
            return ""
        if not t:
            return s[0]

        char_count = Counter(t)
        counter = len(t)
        i, j = 0, 0
        begin, end = 0, float('inf')

        while j < len(s):
            current = s[j]
            if current in char_count:
                if char_count[current] > 0:
                    counter -= 1
                char_count[current] -= 1

            while counter == 0:
                if end - begin > j - i:
                    begin, end = i, j
                current = s[i]
                if current in char_count:
                    char_count[current] += 1
                    if char_count[current] > 0:
                        counter += 1
                i += 1

            j += 1

        return s[begin:end + 1] if end - begin != float('inf') else ""


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
print(sol.minWindow("", "ABC"))
print(sol.minWindow("ADOBECODEBANC", ""))


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