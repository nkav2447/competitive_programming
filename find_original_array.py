from collections import deque
class Solution(object):
    def findOriginalArray(self, changed):
        ans = []
        q = deque()
        for n in sorted(changed):
            if q and n == q[0]:
                q.popleft()
            else:
                q.append(n * 2)
                ans.append(n)

        return [] if q else ans
