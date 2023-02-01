class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        length, last, first = len(cardPoints), k, 0
        maximum = score = sum(cardPoints[:k])
        while last > 0:
            last -= 1
            score = score - cardPoints[last] + cardPoints[length-1-first]
            maximum = max(maximum, score)
            first += 1
        return maximum
