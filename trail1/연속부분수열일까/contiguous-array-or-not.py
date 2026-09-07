n_one, n_two = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

s, e = 0, n_two

flag = 'No'
while e <= n_one + 1:
    if a[s:e] == b:
        flag = 'Yes'
        break
    else:
        s += 1
        e += 1

print(flag)