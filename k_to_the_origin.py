from heapq import heapify, nsmallest; from math import sqrt
class Solution(object):
    def kClosest(self, points, K):
        dic = []
        for p in points:
            d = sqrt(p[0]**2 + p[1]**2)
            dic.append((d, p))
        heapify(dic)
        return [d[1] for d in nsmallest(K, dic)]
