from math import ceil


class Solution:
    def split(self, input1):
        
        lastSpace = 0
        curStart = 0
        ans = []
        totalSplit = 0
        count = 0
        i = 0
        while i < len(input1):
            count += 1
            if input1[i] == ' ':
                lastSpace = i
            if count == 155:
                if input1[i] != ' ':
                    if (i < len(input1) - 1 and input1[i+1] == ' ') or i == len(input1) - 1:
                        lastSpace = i
                totalSplit += 1
                count = 0
                ans.append(input1[curStart:lastSpace+1])
                if i > lastSpace:
                    i = lastSpace
                curStart = i + 1
            i += 1
        if curStart < len(input1):
            if totalSplit == 0:
                return [input1]
            ans.append(input1[curStart:])
            totalSplit += 1
        
        for i, s in enumerate(ans):
            ans[i] = s + '(' + str(i+1) + '/' + str(totalSplit) + ')'
        return ans

def segments(message):
    result = []

    partition = 20
    start_index = 0
    index = start_index
    max_index = 0
    message_length = len(message)

    segment = ""
    current_segment, num_segments = 1, 1
    def get_segment(current_segment):
        segment = "(" + str(current_segment) + "/" + str(num_segments) + ")"
        return segment

    if message_length / partition > 1:
        num_segments = int(ceil(len(message)/(partition - 5)))
        segment = get_segment(current_segment)
    
    while index < message_length:
        if index - start_index > (partition - len(segment) - 1):
            result.append(message[start_index:max_index+1] + get_segment(current_segment))
            current_segment += 1
            start_index = max_index + 1
        
        if message[index] == " ":
            max_index = max(index, max_index)
        
        index += 1

    if start_index < message_length:
        result.append(message[start_index:] + get_segment(current_segment))

    return result


s = Solution()
print(s.split("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))
#print(Solution.split("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."))
#print(solution("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."))


'''
while index < message_length:
        if index - start_index <= (partition - len(segment) - 1) and message[index] == " ":
            max_index = max(index, max_index)
        elif index - start_index > (partition - len(segment) - 1):
            result.append(message[start_index:max_index+1] + get_segment(current_segment))
            current_segment += 1
            start_index = max_index + 1
        index += 1

if start_index < message_length:
        result.append(message[start_index:])

    return result
'''

# def solution(message):
#     partition = 160
#     segments = int(ceil(len(message)/partition))
#     segment = 1

#     for index, char in enumerate(message):
#         size = '(' + str(segment) + '/' + str(segments) + ')'
#         length = partition - len(size)
#         if index >
#         if char == ' ':



'''
def solution(codes, numbers):
    if not codes:  # edge case
        return []
    
    char_to_digit_mapping = {
        "A": "2",
        "B": "2",
        "C": "2",
        "D": "3",
        "E": "3",
        "F": "3",
        "G": "4",
        "H": "4",
        "I": "4",
        "J": "5",
        "K": "5",
        "L": "5",
        "M": "6",
        "N": "6",
        "O": "6",
        "P": "7",
        "Q": "7",
        "R": "7",
        "S": "7",
        "T": "8",
        "U": "8",
        "V": "8",
        "W": "9",
        "X": "9",
        "Y": "9",
        "Z": "9",
    }

    number_to_code_mapping = {}
    nums = list(set(numbers))
    nums.sort()
    
    result = []

    for code in codes:
        num = ""
        for char in code:
            num += char_to_digit_mapping[char]
        number_to_code_mapping[num] = code

    print(number_to_code_mapping)

    for num in nums:
        for key in number_to_code_mapping.keys():
            if key in num:
                result.append(num)
                break

    return result

print(solution(["TWLO", "HTCH", "CODE", "FLOWERS"], ["+17474824380", "+14157088956", "+919810155555", "+15109926333", "+1415123456", "+18003569377"]))
'''

'''
def solution(message):
    result = []
    start, current, end = 0, 0, 0
    partition = 10

    for index, char in enumerate(message):
        current += 1
        if char == ' ':
            if current == partition:
                end = current + 1
                result.append(message[start:end])
                start = end
                current = current - partition
            elif current > partition:
                result.append(message[start:end])
                start = end
                end = index+1
                current = end - start + 1
            else:
                end = current

    result.append(message[start:])
            
    return result
'''


