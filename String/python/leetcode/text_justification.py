"""
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

Constraints:
1 <= words.length <= 300
1 <= words[i].length <= 20
words[i] consists of only English letters and symbols.
1 <= maxWidth <= 100
words[i].length <= maxWidth
"""
from typing import List
from math import ceil


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, queue = [], []
        i, charCount = 0, 0

        for word in words:
            if charCount + len(word) + len(queue) > maxWidth:
                if len(queue) == 1:
                    sentence = queue.pop()
                    sentence += ' ' * (maxWidth - charCount)
                else:
                    temp = []
                    while len(queue) > 1:
                        temp.append(queue.pop(0))
                        spaces = ' ' * ceil((maxWidth - charCount) / len(queue))
                        temp.append(spaces)
                        charCount += len(spaces)
                    temp.append(queue.pop())
                    sentence = ''.join(temp)

                res.append(sentence)
                queue = []
                charCount = 0
            
            queue.append(word)
            charCount += len(word)

        sentence = ' '.join(queue)
        sentence += ' ' * (maxWidth - len(sentence))
        res.append(sentence)

        return res


sol = Solution()
print(sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(sol.fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(sol.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20))
print(sol.fullJustify(["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16)) # failed testcase

"""
First attempt that failed on last testcase:

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, queue = [], []
        i, count = 0, 0

        while i < len(words):
            count += len(words[i])
            if not queue or (count + len(queue)) <= maxWidth:
                queue.append(words[i])
                i += 1
            else:
                count -= len(words[i])
                numSpaces = len(queue)-1 if len(queue) > 1 else 1
                spaceLen = ceil((maxWidth - count) / numSpaces)
                # print(count, spaceLen)

                charCount = len(queue[0])
                temp = [queue.pop(0)]
                while queue:
                    top = queue.pop(0)
                    charCount += len(top)
                    spaces = ' ' * min(maxWidth-charCount, spaceLen)
                    charCount += len(spaces)
                    temp.append(spaces)
                    temp.append(top)

                if charCount < maxWidth:
                    temp.append(' ' * (maxWidth - charCount))
                count = 0
                res.append(''.join(temp))

        last = ' '.join(queue)
        spaceLen = (maxWidth - len(last))
        last += ' ' * spaceLen
        res.append(last)

        return res   
"""
