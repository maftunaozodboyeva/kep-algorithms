n = int(input())
lst = list(map(int, input().split()))
s = 0
# for son in lst:
#     if son < 30 and son % 3 == 0:
#         print(son, end=" ")
#     else:
#         s += son 
# print()
# print(s)

for index in range(len(lst)):
    print(index, lst[index])