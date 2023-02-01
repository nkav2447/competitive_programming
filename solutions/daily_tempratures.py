class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack1, stack2nd = stack.pop()
                res[stack2nd] = i - stack2nd
            stack.append((temp, i))
        return res
