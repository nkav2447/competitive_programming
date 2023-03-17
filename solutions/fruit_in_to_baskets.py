#another solution
class Solution:
            def totalFruit(self, fruits: List[int]) -> int:
                max_length, window_start = 0, 0
                char_frequency = {}
                for window_end in range(len(fruits)):
                    right_char = fruits[window_end]
                    if right_char not in char_frequency:
                        char_frequency[right_char] = 0
                    char_frequency[right_char] += 1
                    while len(char_frequency) > 2:
                        left_char = fruits[window_start]
                        char_frequency[left_char] -= 1
                        if char_frequency[left_char] == 0:
                            del char_frequency[left_char]
                        window_start += 1  
                    max_length = max(max_length, window_end - window_start + 1)
                return max_length
#another solution
class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import defaultdict
        ans = i = 0
        last = defaultdict(int)
        for idx, value in enumerate(fruits):
            if len(last) == 2 and value not in last:
                pre = min(last.values())
                i = pre + 1
                last.pop(fruits[pre])
            last[value] = idx
            ans = max(ans, idx - i + 1)
        return ans
