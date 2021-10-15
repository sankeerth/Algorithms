"""
1178. Number of Valid Words for Each Puzzle

With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage"; while invalid words are "beefed" (doesn't include "a") and "based" (includes "s" which isn't in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that are valid with respect to the puzzle puzzles[i].
 

Example :

Input: 
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa" 
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There're no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
 

Constraints:

1 <= words.length <= 10^5
4 <= words[i].length <= 50
1 <= puzzles.length <= 10^4
puzzles[i].length == 7
words[i][j], puzzles[i][j] are English lowercase letters.
Each puzzles[i] doesn't contain repeated characters.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        pass


sol = Solution()
print(sol.findNumOfValidWords(["aaaa","asas","able","ability","actt","actor","access"], ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]))


"""
class Solution:
    # [1]
	# Generates a bit mask given a word, where the i-th bit being 1 mean
	# the word contains the i-th letter of the alphabet.
	# For example the word 'acf' -> 100101 because a, c, f are the 1st, 3rd,
	# and 6th letters of the alphabet, so those corresponding bits are 1.
    def getBitMask(self, word: str) -> int:
        mask = 0
        for c in word:
		    # Maps 'a' -> 0, 'b' -> 1, 'c' -> 2, ...
            i = ord(c) - ord('a')
			# Sets the i-th bit to 1.
            mask |= 1 << i
        return mask

    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
	    # [2]
		# Maps the bit mask for every word to the count of words with that same bit mask.
		# For example 'abd' and 'baddd' would have the same mask because they are composed
		# of the same set of characters.
        letterFrequencies = {}
        for word in words:
            mask = self.getBitMask(word)
            letterFrequencies[mask] = letterFrequencies.get(mask, 0) + 1
        
        solution = [0] * len(puzzles)
        
        for i in range(len(puzzles)):
            puzzle = puzzles[i]
            mask = self.getBitMask(puzzle)
            subMask = mask
            total = 0
			
			# The index of the first bit in the puzzle. We need this to check if the
			# submasks we generate are of valid words.
            firstBitIndex = ord(puzzle[0]) - ord('a')

			# [3]
            # In this while loop we want to go through all possible "submasks" of the bit
			# mask for the current puzzle. If our puzzle bit mask is 1011, for example, we
			# would generate 1011, 1010, 1001, 1000, 0011, 0010, 0001, 0000
            while True:
				# [4]
			    # If this submask contains the first letter of the puzzle, it's a valid word. Here
				# we add to the number of words we've seen with this mask to our total.
                if subMask >> firstBitIndex & 1:
                    total += letterFrequencies.get(subMask, 0)
				# We've exhausted all possible submasks.
                if subMask == 0:
                    break
				# Get rid of the right-most bit, and restore any bits to the right of it that were
				# originally in the mask. If the original mask was '01011' current submask is '01000',
				# then submask - 1 = '00111' and (submask - 1) & mask = '00011'.
                subMask = (subMask - 1) & mask
            solution[i] = total
        
        return solution
"""


"""
Naive solution (TLE) to check if each char in set of word in words exist in set of puzzle in puzzles:

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordSetList, puzzleSetList = [], []
        res = [0] * len(puzzles)

        for word in words:
            wordSetList.append(set(word))

        for puzzle in puzzles:
            puzzleSetList.append(set(puzzle))

        for i, puzzle in enumerate(puzzles):
            for wordSet in wordSetList:
                if puzzle[0] in wordSet:
                    count = 0
                    for char in wordSet:
                        if not char in puzzleSetList[i]:
                            break
                        count += 1
                    if count == len(wordSet):
                        res[i] += 1

        return res
"""

"""
Using primes also gives TLE, essentially eliminates the 'for char in wordSet:' loop. Therefore time complexity is still O(num puzzles) * O(num words):

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        wordPrimeList, puzzlePrimeList = [], []
        wordCount = defaultdict(int)
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        res = [0] * len(puzzles)

        for word in words:
            s = set(word)
            if len(s) > 7:
                continue
            prime = 1
            for char in s:
                prime *= primes[ord(char) - ord('a')]
            wordPrimeList.append(prime)
            wordCount[prime] += 1

        for puzzle in puzzles:
            s = set(puzzle)
            prime = 1
            for char in s:
                prime *= primes[ord(char) - ord('a')]
            puzzlePrimeList.append(prime)

        for i, puzzlePrime in enumerate(puzzlePrimeList):
            for wordPrime in wordPrimeList:
                firstChar = puzzles[i][0]
                firstCharPrime = primes[(ord(firstChar)) - ord('a')]
                if wordPrime % firstCharPrime != 0:
                    continue
                if puzzlePrime % wordPrime == 0:
                    res[i] += wordCount[wordPrime]

        return res
"""
