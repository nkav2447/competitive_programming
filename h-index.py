class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        for c in range(len(citations)):
            if len(citations) - c <= citations[c]: 
                return len(citations) - c
        return 0
