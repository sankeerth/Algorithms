"""
210. Course Schedule II

There are a total of n courses you have to take labelled from 0 to n - 1.
Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] 
this means you must take the course bi before the course ai.
Given the total number of courses numCourses and a list of the prerequisite pairs, 
return the ordering of courses you should take to finish all courses.
If there are many valid answers, return any of them. 
If it is impossible to finish all courses, return an empty array.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:
Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""
from typing import List
from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses-1, -1, -1)]

        res = []
        graph = defaultdict(list)
        
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        
        for node in range(numCourses):
            if not graph[node]: # to add at least an empty list to each course if not present in prerequisites
                pass

        def detectCycle(src, seen):
            visited.add(src)
            seen.add(src)
            for dest in graph[src]:
                if dest in seen:
                    return True
                if detectCycle(dest, seen):
                    return True
            seen.remove(src)
            return False

        def topologicalSort(src, visited):
            visited.add(src)
            for dest in graph[src]:
                if dest not in visited:
                    topologicalSort(dest, visited)
            res.append(src)

        visited = set()
        for node in graph:
            if node not in visited:
                if detectCycle(node, set()):
                    return res

        visited = set()
        for node in graph:
            if node not in visited:
                topologicalSort(node, visited)

        return res[::-1]


s = Solution()
print(s.findOrder(6, [[1,0],[2,0],[4,3],[5,4],[3,5]]))
print(s.findOrder(2, [[1,0]]))
print(s.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))
print(s.findOrder(6, [[1,0],[2,0],[2,1],[4,3],[5,4]]))


"""
My other topological sort solution using indegree of courses/nodes:

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses-1, -1, -1)]

        graph, inDegree = defaultdict(list), defaultdict(int)
        res, queue = list(), list()

        # to make sure courses whose pre-prequisites are not defined are present in graph with 0 indegree
        # this will ensure that all courses are filled before the next for loop in prerequesites without the need to add [] to certain courses
        for course in range(numCourses):
            inDegree[course] += 0
            if not graph[course]:
                pass

        for course1, course2 in prerequisites:
            graph[course2].append(course1)
            inDegree[course1] += 1
        
        for course in inDegree:
            if not inDegree[course]:
                queue.append(course)

        while queue:
            course = queue.pop(0)
            res.append(course)
            for prereq in graph[course]:
                inDegree[prereq] -= 1
                if not inDegree[prereq]:
                    queue.append(prereq)

        # cycle if not all courses are present in res
        # another way to check there isn't a cycle is if indegree value of each course is 0
        # or just delete the course from indegree each time it is popped from queue and check if indegree is empty dict
        return res if len(res) == numCourses else []
"""
