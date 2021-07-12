"""
621. Task Scheduler

Given a char array representing tasks CPU need to do.
It contains capital letters A to Z where different letters represent different tasks.
Tasks could be done without original order.
Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.
However, there is a non-negative cooling interval n that means between two same tasks,
there must be at least n intervals that CPU are doing different tasks or just be idle.
You need to return the least number of intervals the CPU will take to finish all the given tasks.

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    """
    1. Sort the tasks
    2. Calculate the required amount of intervals for the task with max number
    3. Keep a current count and add the count of each task to it
    4. If a task has the same required amount as task with max number, increase the required amount by 1 as there are more than
    one task with max occurances
    5. Answer will be max of required amount or total count

    Can be solved in two other ways :
    1. Keep a bucket for each of max count and start adding chars into each bucket
    2. Use Min Heap to get the max count and append to task list and heapify at the end of each interval
    """
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        counter = Counter(tasks)
        values = list(counter.values())
        maxInterval = max(values)
        countOfMaxOccurrances = values.count(maxInterval)

        minRequired = maxInterval + n * (maxInterval - 1)
        while countOfMaxOccurrances > 1:
            minRequired += 1
            countOfMaxOccurrances -= 1

        total = max(minRequired, len(tasks))
        return total


sol = Solution()
print(sol.leastInterval(["A","A","A","D","D","D","B","B","B","C","C","C","D","D","D"], 4))
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","A","A","A","A","A","A","A","D","D","D","D","D","D","D","D","B","B","B","B","B","B","B","B","C","C","C","C","C","C","C"]
, 3))

"""
Leetcode solution, Greedy:

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1
        
        frequencies.sort()

        # max frequency
        f_max = frequencies.pop()
        idle_time = (f_max - 1) * n
        
        while frequencies and idle_time > 0:
            idle_time -= min(f_max - 1, frequencies.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
"""

"""
Leetcode solution, Math:

Algorithm

The maximum number of tasks is 26. Let's allocate an array frequencies of 26 elements to keep the frequency of each task.
Iterate over the input array and store the frequency of task A at index 0, the frequency of task B at index 1, etc.
Find the maximum frequency: f_max = max(frequencies).
Find the number of tasks which have the max frequency: n_max = frequencies.count(f_max).
If the number of slots to use is defined by the most frequent task, it's equal to (f_max - 1) * (n + 1) + n_max.
Otherwise, the number of slots to use is defined by the overall number of tasks: len(tasks).
Return the maximum of these two: max(len(tasks), (f_max - 1) * (n + 1) + n_max).

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # frequencies of the tasks
        frequencies = [0] * 26
        for t in tasks:
            frequencies[ord(t) - ord('A')] += 1

        # max frequency
        f_max = max(frequencies)
        # count the most frequent tasks
        n_max = frequencies.count(f_max)

        return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
"""
