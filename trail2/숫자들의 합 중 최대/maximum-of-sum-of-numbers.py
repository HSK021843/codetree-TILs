X, Y = map(int, input().split())

# Please write your code here.
mx = float('-inf')
for n in range(X, Y + 1):
    val_to_list = list(map(int, str(n)))
    
    tmp = sum(val_to_list)
    mx = max(mx, tmp)

print(mx)