class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_start, max_length, max_repeat_letter_count = 0, 0, 0
        char_freq = {}
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            char_freq[right_char] = char_freq.get(right_char, 0) + 1
            max_repeat_letter_count = max(
                max_repeat_letter_count, char_freq[right_char])
                
            if (window_end - window_start + 1 - max_repeat_letter_count) > k:
                left_char = s[window_start]
                char_freq[left_char] -= 1
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)
        return max_length
