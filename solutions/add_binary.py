class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            total = carry
            if i >= 0:
                total += ord(a[i]) - ord("0")
            if j >= 0:
                total += ord(b[j]) - ord("0")
            i -= 1
            j -= 1
            carry = 1 if total > 1 else 0
            result += str(total % 2)
        if carry != 0:
            result += str(carry)
        return result[::-1]
