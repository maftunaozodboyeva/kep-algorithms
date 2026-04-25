n = int(input())
nums = list(int, input().split())
max_i = nums.index(max(nums))
min_i = nums.index(max(nums))
masofa = abs(max_i - min_i) - 1
natija = max(0, masofa)
print(natija)