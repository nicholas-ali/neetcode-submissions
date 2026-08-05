class Solution:
    def climbStairs(self, n: int) -> int:
        res = [0, 1, 1]
        for i in range(2,n+1):
            res.append(res[-1] + res[-2])
        print(res)
        return res[-1]


