from collections import Counter
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        pair = Counter(n1+n2 for n1 in nums1 for n2 in nums2)
        return sum(pair[-n4-n3] for n3 in nums3 for n4 in nums4)
