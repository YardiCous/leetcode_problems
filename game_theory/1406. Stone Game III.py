class Solution:
    def stoneGameIII(self, nums: List[int]) -> str:
        N = len(nums)
        INF = 10 ** 20
        @cache 
        def dp(index):
            if index >= N:
                return 0
            res = -INF
            a = nums[index] - dp(index + 1)
            res = max(res,a)
            if index + 1 < N:
                b = nums[index + 1] + nums[index] - dp(index + 2)
                res = max(res,b)
            if index + 2 < N:
                c = nums[index + 2] + nums[index + 1] + nums[index] - dp(index + 3)
                res = max(res,c)
            return res
        # return dp(0)
        r = dp(0)
        if r < 0:
            return "Bob"
        elif r > 0:
            return "Alice"
        return "Tie"

