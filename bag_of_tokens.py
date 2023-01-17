class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        left, score = 0, 0
        right = len(tokens)-1
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
            elif score and left != right:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return score
