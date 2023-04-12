#another solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        if len(num1) > len(num2):
            for i in range(len(num1) - len(num2)):
                num2.insert(0,"0")
        elif len(num1) < len(num2):
            for i in range(len(num2) - len(num1)):
                num1.insert(0,"0")
        res = 0 
        for i in range(len(num1)):
            temp = (ord(num1.pop()) + ord(num2.pop()))%48
            res += temp * 10**i
        return str(res)
#another solution
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
