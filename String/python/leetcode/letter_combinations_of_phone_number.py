"""
17. Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []

        l = len(digits)

        digit_to_alpha_mapping = {"1": "*", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs",
                                  "8": "tuv", "9": "wxyz", "0": " "}

        result = list()

        for char in digit_to_alpha_mapping[digits[0]]:
            result.append(char)

        for index, digit in enumerate(digits[1:], start=1):
            label = digit_to_alpha_mapping[digit]
            while len(result[0]) == index:
                top = result.pop(0)
                for char in label:
                    result.append(top + char)

        return result

sol = Solution()
print(sol.letterCombinations("120"))
print(sol.letterCombinations("122"))
print(sol.letterCombinations("123"))
print(sol.letterCombinations("20314"))
print(sol.letterCombinations("1920"))
print(sol.letterCombinations("456"))

"""
Leetcode discuss solution:

vector<string> letterCombinations(string digits) {
    vector<string> res;
    string charmap[10] = {"0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    res.push_back("");
    for (int i = 0; i < digits.size(); i++)
    {
        vector<string> tempres;
        string chars = charmap[digits[i] - '0'];
        for (int c = 0; c < chars.size();c++)
            for (int j = 0; j < res.size();j++)
                tempres.push_back(res[j]+chars[c]);
        res = tempres;
    }
    return res;
}
"""
