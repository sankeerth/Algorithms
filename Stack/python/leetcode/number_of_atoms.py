"""
726. Number of Atoms

Given a chemical formula (given as a string), return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

One or more digits representing that element's count may follow if the count is greater than 1. 
If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together to produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, return the count of all elements as a string in the following form: the first name (in sorted order), 
followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:
Input: formula = "H2O"
Output: "H2O"
Explanation: The count of elements are {'H': 2, 'O': 1}.

Example 2:
Input: formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation: The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:
Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation: The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Example 4:
Input: formula = "Be32"
Output: "Be32"

Constraints:
1 <= formula.length <= 1000
formula consists of English letters, digits, '(', and ')'.
formula is always valid.
"""
from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:        
        def compute(formula, start):
            counter, stackCount = defaultdict(int), {}
            element = ""
            i, count = start, 1

            while i < len(formula):
                char = formula[i]
                if stackCount and not char.isdigit():
                    for key in stackCount:
                        stackCount[key] *= count
                        counter[key] += stackCount[key]
                    stackCount = {}

                if char.isupper():
                    if element:
                        counter[element] += count
                    count = 1
                    element = char
                elif char.islower():
                    element += char
                elif char.isdigit():
                    count = int(char) if not formula[i-1].isdigit() else count * 10 + int(char)
                elif char == '(':
                    if element:
                        counter[element] += count
                        element = ""
                    stackCount, i = compute(formula, i+1)
                elif char == ')':
                    if element:
                        counter[element] += count
                    return counter, i

                i += 1

            if stackCount:
                for key in stackCount:
                    stackCount[key] *= count
                    counter[key] += stackCount[key]
            if element:
                counter[element] += count
            return counter

        counter = compute(formula, 0)
        
        result = []
        for element in sorted(counter):
            result.append(element + str(counter[element] if counter[element] > 1 else ""))

        return "".join(result)


sol = Solution()
print(sol.countOfAtoms("H2O"))
print(sol.countOfAtoms("H2O2"))
print(sol.countOfAtoms("Be32"))
print(sol.countOfAtoms("(H2O2)3"))
print(sol.countOfAtoms("(H2O)Se"))
print(sol.countOfAtoms("(H2O)3Se"))
print(sol.countOfAtoms("(H2O)3Se3"))
print(sol.countOfAtoms("Mg(OH)2"))
print(sol.countOfAtoms("K4(ON(SO3)2)2"))
print(sol.countOfAtoms("(SO3)2(H2O)4"))
