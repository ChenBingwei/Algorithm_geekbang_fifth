from queue import Queue
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edge_array = [[] for _ in range(numCourses)]
        in_degree_list = [0 for _ in range(numCourses)]
        for course, pre_course in prerequisites:
            edge_array[pre_course].append(course)
            in_degree_list[course] += 1
        q = Queue()
        # 拓扑排序
        # 第一步：从入度为0的点出发
        for i in range(numCourses):
            if in_degree_list[i] == 0:
                q.put(i)
        lesson = []
        while not q.empty():
            course = q.get()
            lesson.append(course)
            # 第二步：扩展一个点，周围点的入度减1
            for i in edge_array[course]:
                in_degree_list[i] -= 1
                # 第三步：点的入度减为0，表示可以入队了
                if in_degree_list[i] == 0:
                    q.put(i)
        return len(lesson) == numCourses
