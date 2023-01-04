class Solution(object):
  #######  Iterative Approach #######
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: 
            return 1
        if n < 0: 
            div = True; n = -n
        else:  
            div = False
        shelf = []
        while n != 1 and n != -1:
            if n % 2 == 0: 
                shelf.append(1)
            else: 
                shelf.append(x)
            n //= 2
        result = x
        while len(shelf) != 0:
            result = result * result * shelf.pop()
        if div:
            return 1.0 / result
        else:
            return result
        ###### Recursive Approach ########
        def pow(self, x, n):
        if n == 0:         
            return 1                     
        elif n < 0:         
            return 1.0 / self.pow(x, -n)
        elif n == 1:        
            return x                   
        else:
            if n % 2 == 0:  
                return self.pow(x*x, n//2)
            else:           
                return self.pow(x*x, n//2)*x
