from queue import Queue
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edge_array = [[] for _ in range(numCourses)]
        in_degree_list = [0] * numCourses
        lesson_order = []
        for course, pre_course in prerequisites:
            edge_array[pre_course].append(course)
            in_degree_list[course] += 1
        q = Queue()
        for i, degree in enumerate(in_degree_list):
            if degree == 0:
                q.put(i)
        while not q.empty():
            a = q.get()
            lesson_order.append(a)
            for i in edge_array[a]:
                in_degree_list[i] -= 1
                if in_degree_list[i] == 0:
                    q.put(i)
        if len(lesson_order) == numCourses:
            return lesson_order
        else:
            return []
