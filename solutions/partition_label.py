class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        size = []
        while s:
            i = 1
            while set(s[:i]) & set(s[i:]):
                i += 1
            size.append(i)
            s= s[i:]
        return size
