class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        added = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while carry > 0 or i >= 0 or j >= 0:
            if i >= 0:
                carry += int(num1[i])
                i -= 1
            if j >= 0:
                carry += int(num2[j])
                j -= 1
            added += str(carry % 10)
            carry = carry // 10
        return added[::-1]
