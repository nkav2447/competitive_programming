class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def find_idx(curr_idx, steps, length):
            fnd_idx = curr_idx + steps - 1
            if fnd_idx >= length:
                fnd_idx = fnd_idx%length
            return fnd_idx
        def find_sol(lst, idx):
            length = len(lst)
            if length == 1:
                return lst[0]
            else:
                lst.pop(idx)
                return find_sol(lst, find_idx(idx, k, length - 1))

        return find_sol([i for i in range(1, n+1)],  find_idx(0, k, n))
