class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_start = matched = 0
        char_freq = {}

        for c in s1:
            char_freq[c] = char_freq.get(c, 0) + 1

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in char_freq:
                char_freq[right_char] -= 1
                if char_freq[right_char] == 0:
                    matched += 1
            if matched == len(char_freq):
                return True
            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                window_start += 1
                if left_char in char_freq:
                    if char_freq[left_char] == 0:
                        matched -= 1
                    char_freq[left_char] += 1
        return False
