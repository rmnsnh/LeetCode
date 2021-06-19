class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        return Solution.recurse(n, k)

        # if (dp[n][k] != -1) return dp[n][k];
        # if (k == 0) return dp[n][k] = 1;
        # if (n == 0) return dp[n][k] = 0;
        # int j = 0, val = 0;
        # for (j = 0; j < n && k-j >= 0; j++)
        #     val += inversions(n-1, k-j);
        # return dp[n][k] = val;
    def recurse(n, k):
        if k == 0:
            return 0
        if n == 0:
            return 0
        ret = 0
        i = 0
        while i < n and k-i >= 0:
            ret += Solution.recurse(n-1, k-i)
            i += 1
        return ret

s = Solution()
print(s.kInversePairs(3, 0))
print(s.kInversePairs(3, 1))