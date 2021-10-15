"""
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""

class Solution:
    def numberToWords(self, num: int) -> str:
        if num < 0:
            return ""
        
        if num == 0:
            return "Zero"

        digitMap = {
            "1": ["One Hundred ", "Ten", "One"],
            "2": ["Two Hundred ", "Twenty ", "Two"],
            "3": ["Three Hundred ", "Thirty ", "Three"],
            "4": ["Four Hundred ", "Forty ", "Four"],
            "5": ["Five Hundred ", "Fifty ", "Five"],
            "6": ["Six Hundred ", "Sixty ", "Six"],
            "7": ["Seven Hundred ", "Seventy ", "Seven"],
            "8": ["Eight Hundred ", "Eighty ", "Eight"],
            "9": ["Nine Hundred ", "Ninety ", "Nine"],
            "0": ["", "", ""]
        }

        tensMap = {
            "10": "Ten",
            "11": "Eleven",
            "12": "Twelve",
            "13": "Thirteen",
            "14": "Fourteen",
            "15": "Fifteen",
            "16": "Sixteen",
            "17": "Seventeen",
            "18": "Eighteen",
            "19": "Nineteen"
        }

        suffix = {
            1: "",
            2: " Thousand ",
            3: " Million ",
            4: " Billion ",
            5: " Trillion "
        }

        def calculateThreeDigits(s):
            r = ""
            if len(s) == 1:
                r = digitMap[s[0]][2]
            else:
                if s[-2] == "1":
                    r += tensMap[s[-2:]]
                else:
                    r = digitMap[s[-2]][1] + digitMap[s[-1]][2]
            if len(s) == 3:
                r = digitMap[s[0]][0] + r

            return r

        s = str(num)
        l = len(s)
        i, count = l, 1
        result = ""
        while i > 0:
            start = i-3 if i-3 > 0 else 0 
            r = calculateThreeDigits(s[start:i])
            if r != "":
                result = r + suffix[count] + result
            count += 1
            i -= 3

        return " ".join(result.split())


s = Solution()
print(s.numberToWords(123))
print(s.numberToWords(1234567))
print(s.numberToWords(1234567891))
print(s.numberToWords(17))
print(s.numberToWords(103))
print(s.numberToWords(0))
print(s.numberToWords(5))
print(s.numberToWords(10))
print(s.numberToWords(44))
print(s.numberToWords(39))
print(s.numberToWords(99))
print(s.numberToWords(1008))
print(s.numberToWords(1000008))
print(s.numberToWords(1000000008))
