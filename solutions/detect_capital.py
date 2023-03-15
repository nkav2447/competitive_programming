#another solution
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        if word[0].isupper() and word[1].isupper():
            for i in range(2, len(word)):
                if word[i].islower():
                    return False
        else:
            for i in range(1, len(word)):
                if word[i].isupper():
                    return False
        return True
#another solution
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) < 2:
            return True
        elif word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
