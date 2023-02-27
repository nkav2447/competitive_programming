class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        col_num = 0
        for c in columnTitle:
            n = ord(c) - 64
            col_num = col_num * 26 + n
        return col_num
