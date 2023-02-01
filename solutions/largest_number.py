class Solution(object):
    def largestNumber(self, nums):
        class Comp(str):
            def __lt__(x, y):
                return x+y < y+x

        res = ''.join(map(str, sorted(nums, key=Comp, reverse=True)))
        return '0' if res[0] == '0' else res
