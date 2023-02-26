class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        elif len(strs) == 1:
            return strs[0]
        else:
            curr_prefix = strs[0]
            len_prefix = len(curr_prefix)
            for i in range(1, len(strs)):
                while curr_prefix != strs[i][:len_prefix]:
                    curr_prefix = curr_prefix[: len_prefix - 1]
                    len_prefix -= 1
                    if len_prefix == 0:
                        return ""
        return curr_prefix
