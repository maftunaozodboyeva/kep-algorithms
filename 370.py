# n = int(input())
# a = list(map(int, input().split()))
# result = a[0::2]
# print(*result)

n = int(input())
lst = list(map(int, input().split()))
for index in range(n):
    if (index + 1) % 2 != 0:
        print(lst[index], end = " ")