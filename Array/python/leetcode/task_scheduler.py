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

from collections import defaultdict


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


class Solution(object):
    def leastInterval(self, tasks, n):
        if not tasks:
            return 0

        task_count = defaultdict(int)
        for task in tasks:
            task_count[task] += 1

        sorted_tasks = sorted(task_count.items(), key=lambda x: x[1])

        c = sorted_tasks.pop()[1]
        max_req_for_task = ((c - 1) * (n + 1)) + 1
        total_count = max_req_for_task
        current_count = c

        while sorted_tasks:
            task = sorted_tasks.pop()
            task_count = task[1]
            req = ((task_count - 1) * (n + 1)) + 1
            if req == max_req_for_task:
                total_count += 1
            current_count += task_count

        return max(current_count, total_count)

sol = Solution()
print(sol.leastInterval(["A","A","A","D","D","D","B","B","B","C","C","C","D","D","D"], 4))
print(sol.leastInterval(["A","A","A","B","B","B"], 2))
print(sol.leastInterval(["A","A","A","A","A","A","A","A","D","D","D","D","D","D","D","D","B","B","B","B","B","B","B","B","C","C","C","C","C","C","C"]
, 3))
