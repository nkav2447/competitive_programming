class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        max_vowel=0
        ans =0
        for i in range(0,len(s)):
            if i>=k :
                if s[i-k] in ['a','e','i','o','u']:
                    ans -=1
            if s[i] in['a','e','i','o','u']:
                ans+=1
            max_vowel = max(max_vowel,ans)
            if max_vowel ==k:
                return max_vowel
        return max_vowel
