def subset_sum(nums, target, i=0):
    if target == 0:
        return True
    if i >= len(nums):
        return False
    if target < 0:
        return False
    
    return subset_sum(nums, target - nums[i], i + 1) or subset_sum(nums, target, i + 1)

if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9
    
    resultado = subset_sum(nums, target)

    print(f"Conjunto: {nums}")
    print(f"Alvo: {target}")
    print(f"Existe subconjunto com soma {target}? {resultado}")
    
    print("\n" + "-"*50 + "\n")
    
    nums2 = [1, 2, 3]
    target2 = 10
    
    resultado2 = subset_sum(nums2, target2)
    print(f"Conjunto: {nums2}")
    print(f"Alvo: {target2}")
    print(f"Existe subconjunto com soma {target2}? {resultado2}")