def subset_sum_dp(nums, target):
    n = len(nums)
    dp = [[False] * (target + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if nums[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][target]

if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2] 
    target = 9
    
    resultado = subset_sum_dp(nums, target)
    print(f"Conjunto: {nums}")
    print(f"Alvo: {target}")
    print(f"Existe subconjunto com soma {target}? {resultado}")
    
    print("\n" + "-"*50 + "\n")
    
    nums2 = [1, 2, 3]
    target2 = 10
    
    resultado2 = subset_sum_dp(nums2, target2)
    print(f"Conjunto: {nums2}")
    print(f"Alvo: {target2}")
    print(f"Existe subconjunto com soma {target2}? {resultado2}")