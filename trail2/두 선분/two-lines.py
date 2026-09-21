x1, x2, x3, x4 = map(int, input().split())

# Please write your code here.
line = [0] * 101

for i in range(x1, x2 + 1):
    line[i] += 1

for i in range(x3, x4 + 1):
    line[i] += 1

state = "nonintersecting"
for idx in range(101):
    if line[idx] >= 2:
        state = "intersecting"
        break
    
print(state)