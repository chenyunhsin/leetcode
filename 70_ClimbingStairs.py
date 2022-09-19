# DP 費波那契數列
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=3:
            return n
        n1,n2 = 2,3
        for i in range(4,n+1):
            now = n1+n2
            n1 = n2
            n2 = now
        return now
