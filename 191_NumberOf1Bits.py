class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n>0:
            cnt += n%2
            n//=2
        return cnt
