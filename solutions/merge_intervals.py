class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda k: k[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last = res[-1][1]
            if start <= last:
                res[-1][1] = max(last, end)
            else:
                res.append([start, end])
        return res
