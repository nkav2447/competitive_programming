class Solution:
    def makeGood(self, s: str) -> str:
        s_arr = []
        res = ""
        for i in range(len(s)):
            if s_arr == []:
                s_arr.append(s[i])
            elif s_arr!=[] and abs(ord(s[i])-ord(s_arr[-1]))==32:
                s_arr.pop() 
            else:
                s_arr.append(s[i])
        if s_arr == []:
            return ""
        res = res.join(s_arr)
        return res
        
