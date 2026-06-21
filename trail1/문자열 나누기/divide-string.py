N = int(input())
tmp = list(map(str, input().split(" ")))
string = "".join(tmp)

i, e = 0, 5
while e <= len(string):
    print(string[i:e])
    i, e = e, e + 5

print(string[i:])