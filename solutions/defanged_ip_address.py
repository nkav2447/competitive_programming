class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged_ip = ""
        for c in address:
            if c != ".":
                defanged_ip += c
            else:
                defanged_ip += "[.]"
        return defanged_ip
