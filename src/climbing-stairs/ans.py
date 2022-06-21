class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2

        twobefore = 0
        onebefore = 1
        curr = 2
        for i in range(3, n+1):
            twobefore = onebefore
            onebefore = curr
            curr = twobefore + onebefore

        return curr
