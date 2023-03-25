#another solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_arr = []
        window_start = max_length = 0
        for window_end in range(len(s)):
            while s[window_end] in char_arr:
                char_arr.remove(s[window_start])
                window_start += 1
            char_arr.append(s[window_end])
            max_length = max(max_length, window_end-window_start+1)
        return max_length

#another solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length, window_start = 0, 0
        char_frequency = {}
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in char_frequency:
                char_frequency[right_char] = 0
            char_frequency[right_char] += 1
            while char_frequency[right_char] > 1:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1 
            max_length = max(max_length, window_end - window_start + 1)
        return max_length
#another solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == None or len(s) == 0:
            return 0
        i, j, maximum = 0, 0, 0
        chr_set = set()
        while i < len(s):
            while s[i] in chr_set:
                chr_set.remove(s[j])
                j += 1
            chr_set.add(s[i])
            maximum = max(maximum, i-j+1)
            i += 1
        return maximum
#another solution
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        collection = set()
        left , res = 0, 0
        for right in range(len(s)):
            while s[right] in collection:
                collection.remove(s[left])
                left += 1
            collection.add(s[right])
            res = max(res, right - left + 1)
        return res
