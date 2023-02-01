class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = [chalk[0]]
        for i in range(1,len(chalk)):
             prefix_sum.append(prefix_sum[i-1]+chalk[i])
        left = k % prefix_sum[len(prefix_sum)-1]
        s , e = 0 , len(prefix_sum)-1 
        while(s<=e):
            ret_idx = s+(e-s)//2
            if prefix_sum[ret_idx] == left:
                return ret_idx+1
            if prefix_sum[ret_idx-1] <= left and left < prefix_sum[ret_idx]:
                return ret_idx
            elif prefix_sum[ret_idx-1] < left and left > prefix_sum[ret_idx]:
                s = ret_idx+1
            else:
                e=ret_idx-1
        return ret_idx
