class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        for i in range(len(bookings)):
            first, last = bookings[i][0], bookings[i][1]
            ans[first] += bookings[i][2]
            if last < n:
                ans[last+1] += -bookings[i][2]
        for i in range(1,n+1):
            ans[i] += ans[i-1]
        ans.pop(0)
        return ans
