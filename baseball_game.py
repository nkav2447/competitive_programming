class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        total = []
        for item in operations:
            try:
                if type(int(item)) is int:
                    total.append(int(item))
            except:
                if item == "C":
                    total.pop()
                if item == "D":
                    total.append(2*(total[-1]))
                if item == "+":
                    total.append(total[-1]+total[-2])
        return sum(total)
