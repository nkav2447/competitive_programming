class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        left, ctr = 0, 0
        right = len(people) - 1
        while left <= right:
            if left != right and people[left] + people[right] > limit: left -= 1
            left += 1
            right -= 1
            ctr += 1
        return ctr
