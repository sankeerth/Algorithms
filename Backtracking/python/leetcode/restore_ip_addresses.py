"""
93. Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses that can 
be obtained from s. You can return them in any order. A valid IP address consists of exactly 
four integers, each integer is between 0 and 255, separated by single dots and cannot have 
leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses 
and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]

Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]

Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

Constraints:
0 <= s.length <= 3000
s consists of digits only.
"""
from typing import List
from math import ceil


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        ipLen = 4
        
        def restore(i, ip):
            if len(ip) == ipLen:
                if i == len(s):
                    res.append(".".join(ip))
                return
            
            cur = ""
            for j in range(i, min(i+3, len(s))):
                cur += s[j]
                if len(cur) > 1 and cur[0] == '0' or int(cur) > 255:
                    break
                ip.append(cur)
                restore(j+1, ip)
                ip.pop()
            
        if len(s) > 12:
            return []
        
        restore(0, [])
        return res
        

s = Solution()
print(s.restoreIpAddresses("0000"))
print(s.restoreIpAddresses("1111"))
print(s.restoreIpAddresses("25525511135"))
print(s.restoreIpAddresses("255255111256"))
print(s.restoreIpAddresses("010010"))
print(s.restoreIpAddresses("101023"))
print(s.restoreIpAddresses("1111111111111"))
print(s.restoreIpAddresses("111"))
print(s.restoreIpAddresses("000000"))
print(s.restoreIpAddresses("2525781"))


"""
Other solution:

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def restoreIpAddressesRecursive(index, cur):
            if ceil(len(s)-index) / 3 + len(cur) > 4 or (len(s)-index) + len(cur) < 4:
                return

            # simpler base condition but does unnecessary recursive calls for invalid cases
            # if index == len(s) and len(cur) != 4 or len(cur) == 4 and index != len(s):
            #     return

            if len(cur) == 4:
                res.append(".".join(cur))
                return
            
            val = ""
            for j in range(index, min(len(s), index + 3)):
                val += s[j]
                if len(val) > 1 and val[0] == '0' or int(val) > 255:
                    break  
                restoreIpAddressesRecursive(j+1, cur + [val])

        restoreIpAddressesRecursive(0, [])
        return res
"""
