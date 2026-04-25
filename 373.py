n = int(input())
a = list(map(int, input().split()))

mx = a[0]
for i in a:
    if i > mx:
        mx = i
print(mx)

min_value = a[0]
for i in a:
    if i < min_value:
        min_value = i
print(min_value)