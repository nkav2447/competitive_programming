class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        curr=0
        beg=0
        trips=sorted(trips,key=lambda t:t[1])
        stack=[]
        for i in range(len(trips)):            
            beg=0
            while stack and beg<len(stack):
                if stack[beg][2]<=trips[i][1]:
                    curr-=stack[beg][0]
                    stack.pop(beg)
                else:
                    beg+=1
            curr+=trips[i][0]           
            stack.append(trips[i])            
            if curr>capacity:
                return False      
        return True
