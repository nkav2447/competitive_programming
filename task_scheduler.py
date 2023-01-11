class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter, deque
        from heapq import heapify, heappop, heappush
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapify(maxHeap)
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1
            if not maxHeap:
                time = q[0][1]
            else:
                cnt = 1 + heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heappush(maxHeap, q.popleft()[0])
        return time
