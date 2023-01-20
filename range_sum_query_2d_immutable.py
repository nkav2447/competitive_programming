class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.pre_sum = [ [ 0 for i in range(len(matrix[0])+1) ] for j in range(len(matrix)+1) ]
        for i in range(1,len(self.pre_sum)):
            for j in range(1,len(self.pre_sum[0])):
                self.pre_sum[i][j] = matrix[i-1][j-1] + self.pre_sum[i][j-1] + self.pre_sum[i-1][j] - self.pre_sum[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1 == 0 and col1 == 0:
            return self.pre_sum[row2+1][col2+1]
        res = self.pre_sum[row2+1][col2+1] - self.pre_sum[row2+1][col1] - self.pre_sum[row1][col2+1] + self.pre_sum[row1][col1]
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
