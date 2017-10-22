"""
    22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]

        result = list()

        def generate_parantheses_recr(open, close, s):
            if open == 0:
                for i in range(close):
                    s += ')'
                result.append(s)
            else:
                generate_parantheses_recr(open-1, close, s+'(')
                if open < close:
                    generate_parantheses_recr(open, close-1, s+')')

        generate_parantheses_recr(n-1, n, '(')

        return result

sol = Solution()
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(0))
print(sol.generateParenthesis(4))

"""
Inefficient C++ code using only recursion

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        return generateParanthesis(n,n);
    }

    vector <string> generateParanthesis(int start, int close){
        vector<string> returnValue;
        if(start == 0){
            string str = "";
            for(int i = 0; i < close; i++)
                str+= ')';
            returnValue.push_back(str);
            return returnValue;
        }
        if(start == close){
            vector<string> ret1 = generateParanthesis(start - 1, close);
            for(string s : ret1){
                returnValue.push_back("(" + s);
            }
        }
        else{
            vector<string> ret1 = generateParanthesis(start - 1, close);
            for(string s : ret1){
                returnValue.push_back("(" + s);
            }
            vector<string> ret2 = generateParanthesis(start, close - 1);
            for(string s : ret2){
                returnValue.push_back(")" + s);
            }
        }
        return returnValue;
    }
};
"""
