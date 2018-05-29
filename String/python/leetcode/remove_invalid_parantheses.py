"""
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution:
    """
    This solution is from leetcode discuss. Similar to my approach but I use list to store intermediate results
    and it is quite verbose!

    Key Points:
    Generate unique answer once and only once, do not rely on Set.
    Do not need preprocess.

    We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter.
    The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more
     ‘)’ than ‘(‘ in the prefix.

    To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix.
    However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2]
    but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.

    After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string.
    However, we need to keep another information: the last removal position. If we do not have this position,
    we will generate duplicate by removing two ‘)’ in two steps only with a different order.
    For this, we keep tracking the last removal position and only remove ‘)’ after that.

    Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘?
    The answer is: do the same from right to left.
    However a cleverer idea is: reverse the string and reuse the code!
    Here is the final implement in Java.
    """
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = list()

        def remove(s, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    stack += 1
                elif s[i] == par[1]:
                    stack -= 1
                if stack >= 0:
                    continue

                for j in range(last_j, i+1):
                    if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                        remove(s[0:j] + s[j+1:], i, j, par)
                return

            reverse = s[::-1]
            if par[0] == '(':
                remove(reverse, 0, 0, [')', '('])
            else:
                result.append(reverse)

        remove(s, 0, 0, ['(', ')'])
        return result


sol = Solution()
print(sol.removeInvalidParentheses(")))))))))))))()))))))"))
print(sol.removeInvalidParentheses("(()"))
print(sol.removeInvalidParentheses("()(()"))
print(sol.removeInvalidParentheses("(()(()"))
print(sol.removeInvalidParentheses("(()(()(()"))
print(sol.removeInvalidParentheses("())(()"))
print(sol.removeInvalidParentheses("()())()(()"))
print(sol.removeInvalidParentheses("()())()"))
print(sol.removeInvalidParentheses("(a)())()"))
print(sol.removeInvalidParentheses(")("))
print(sol.removeInvalidParentheses(")()"))
print(sol.removeInvalidParentheses(")(a)a)"))
print(sol.removeInvalidParentheses("a)(a)a)"))
print(sol.removeInvalidParentheses(")o(v("))


"""
Another leetcode discuss solution:
In BFS we handle the states level by level, in the worst case, we need to handle all the levels, we can analyze the 
time complexity level by level and add them up to get the final complexity.

On the first level, there's only one string which is the input string s, let's say the length of it is n, to check 
whether it's valid, we need O(n) time. On the second level, we remove one ( or ) from the first level, 
so there are C(n, n-1) new strings, each of them has n-1 characters, and for each string, we need to check whether it's 
valid or not, thus the total time complexity on this level is (n-1) x C(n, n-1). Come to the third level, 
total time complexity is (n-2) x C(n, n-2), so on and so forth...

Finally we have this formula:
T(n) = n x C(n, n) + (n-1) x C(n, n-1) + ... + 1 x C(n, 1) = n x 2^(n-1).

public class Solution {
    public List<String> removeInvalidParentheses(String s) {
      List<String> res = new ArrayList<>();
      
      // sanity check
      if (s == null) return res;
      
      Set<String> visited = new HashSet<>();
      Queue<String> queue = new LinkedList<>();
      
      // initialize
      queue.add(s);
      visited.add(s);
      
      boolean found = false;
      
      while (!queue.isEmpty()) {
        s = queue.poll();
        
        if (isValid(s)) {
          // found an answer, add to the result
          res.add(s);
          found = true;
        }
      
        if (found) continue;
      
        // generate all possible states
        for (int i = 0; i < s.length(); i++) {
          // we only try to remove left or right paren
          if (s.charAt(i) != '(' && s.charAt(i) != ')') continue;
        
          String t = s.substring(0, i) + s.substring(i + 1);
        
          if (!visited.contains(t)) {
            // for each state, if it's not visited, add it to the queue
            queue.add(t);
            visited.add(t);
          }
        }
      }
      
      return res;
    }
    
    // helper function checks if string s contains valid parantheses
    boolean isValid(String s) {
      int count = 0;
    
      for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        if (c == '(') count++;
        if (c == ')' && count-- == 0) return false;
      }
    
      return count == 0;
    }
}
"""

"""
My solution:

class Solution:
    def removeInvalidParentheses(self, s):
        result = list()
        current = list()
        result.append('')

        def copy(combinations, result):
            if not combinations:
                return result
            temp = list()
            while result:
                res = result.pop(0)
                for combination in combinations:
                    temp.append(res + ''.join(combination))
            return temp

        def get_combinations_of_cl_gt_op(current, result):
            combinations = list()
            string = ''.join(current)
            for i in range(len(string)-1, -1, -1):
                if string[i] == ')':
                    res = string[:i] + string[i+1:]
                    combinations.append(res)

            return copy(combinations, result)

        def get_combinations_of_op_gt_cl(current, result):
            combinations = list()
            current = current[::-1]
            cur = ''.join(current)
            while result:
                string = cur + result.pop(0)
                for i in range(len(string)):
                    if string[i] == '(':
                        res = string[:i] + string[i+1:]
                        combinations.append(res)

            result.append('')
            return copy(combinations, result)

        def parse_backward(s, result):
            current = list()
            op, cl = 0, 0
            for i in range(len(s)-1, -1, -1):
                if s[i] == '(':
                    op += 1
                    current.append('(')
                elif s[i] == ')':
                    cl += 1
                    current.append(')')
                else:
                    current.append(s[i])

                if op > cl:
                    result = get_combinations_of_op_gt_cl(current, result)
                    if not result:
                        result.append('')
                    op, cl = 0, 0
                    current.clear()

            return current[::-1], result

        def parse_forward(current, result):
            op, cl = 0, 0
            for i in range(len(s)):
                if s[i] == '(':
                    op += 1
                    current.append('(')
                elif s[i] == ')':
                    cl += 1
                    current.append(')')
                else:
                    current.append(s[i])

                if cl > op:
                    result = get_combinations_of_cl_gt_op(current, result)
                    if not result:
                        result.append('')
                    op, cl = 0, 0
                    current.clear()

            if op > cl:
                result_copy = list(result)
                result.clear()
                result.append('')
                current, result = parse_backward(''.join(current), result)
                result = copy(result, result_copy)

            return current, result

        current, result = parse_forward(current, result)

        if current:
            cur = ''.join(current)
            current.clear()
            current.append(cur)

        return list(set(copy(current, result)))
"""