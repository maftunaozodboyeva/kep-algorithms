n = int(input())
a = list(map(int, input().split()))
min_qiymat = min(a)
index = a.index(min_qiymat) + 1
print(index)
