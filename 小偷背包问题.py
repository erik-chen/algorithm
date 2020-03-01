def bag(wgt, val, cap):
    m = len(wgt)
    print(m)
    dp = [[0] * (cap + 1) for _ in range(m + 1)]
    for i in range(1, m+1):
        for j in range(1, cap+1):
            if j >= wgt[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wgt[i-1]] + val[i-1])
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp)



if __name__ == '__main__':
    bag(wgt=[2, 3, 4, 5], val=[3, 4, 5, 6], cap=8)