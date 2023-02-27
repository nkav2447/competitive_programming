#another solution
def canPermutePalindrome(s):
    rem_chars = set()
    for c in s:
        if c in rem_chars:
            rem_chars.remove(c)
        else:
            rem_chars.add(c)
    return len(rem_chars) <= 1
#another solution
def canPermutePalindrome(s: str) -> bool:
    return sum(v % 2 for v in Counter(s).values()) <= 1
