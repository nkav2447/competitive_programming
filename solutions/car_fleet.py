class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        ans, s = 0, {position[i]: speed[i] for i in range(len(position))}
        position.sort()
        while position:
            cur = position.pop()
            ans += 1
            while position and (s[position[-1]] - s[cur]) * (target - cur) / s[cur] >= cur - position[-1]:
                position.pop()
        return ans
