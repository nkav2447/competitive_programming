def canPermutePalindrome(s):
    rem_chars = set()
    for c in s:
        if c in rem_chars:
            rem_chars.remove(c)
        else:
            rem_chars.add(c)
    return len(rem_chars) <= 1
