class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        k , coins = 0, 0
        for i in range(len(piles)-2, -1, -2):
            coins += piles[i]
            k += 1
            if k == len(piles)/3:
                return coins
