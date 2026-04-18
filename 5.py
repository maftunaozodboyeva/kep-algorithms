# import math

# n = int(input())
# summa = 0

# for i in range(1, n + 1):
#     summa += int(math.isqrt(i))

# print(summa)
import math

n = int(input())
s = 0

for i in range(1, n + 1):
    s += int(math.sqrt(i))

print(s)

