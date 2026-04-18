n = int(input())
count = 0
for i in range(1, n + 1):
    if n % 12 == 0 or n % 5 == 0:
        count += 1
print(count)
# TL - time limited exceeded
# n // 5 + n // 12 - n // 60
# n = 60
# 60 // 5 = 12
# 60 // 12 = 5
# 60 // 60 = 1
# 12 + 5 - 1 = 16

print(n // 5 + n // 12 - n // 60)