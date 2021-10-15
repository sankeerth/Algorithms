def compressWord(word, k):
    if k == 0 or not word: # base case
        return word
    
    word_list = list(word)
    while word_list:
        indicesToRemove = []
        start = (word_list[0], 0)
        count = 0
        for i, c in enumerate(word_list):
            if start[0] == c:
                count += 1
            else:
                start = (c, i)
                count = 1
            if count == k:
                indicesToRemove.append((start[1], i))
                start = ("", 0)

        if not indicesToRemove:
            break

        for indices in indicesToRemove[::-1]:
            del word_list[indices[0]: indices[1]+1]

    return "".join(word_list)


# print(compressWord("abcccbb", 3))
# print(compressWord("bcca", 2))
# print(compressWord("aaaaaa", 1))
print(compressWord("acccccbb", 2))
print(compressWord("accccabbc", 2))
