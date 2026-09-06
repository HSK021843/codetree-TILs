n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
tmp = []
for s in str:
    if s[0:len(t)] == t:
        tmp.append(s)

tmp.sort()
print(tmp[k - 1])