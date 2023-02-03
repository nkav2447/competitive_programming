class Solution:
    def calculate_sum(self, x):
        return ((x*(x+1)) / 2)
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n+1):
            sum1 = self.calculate_sum(i)
            sum2 = self.calculate_sum(n) - self.calculate_sum(i-1)
            if sum1 == sum2: return i
        return -1
