n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
mx_cnt = 0
cur_cnt = 0
before_val = -1

for idx in range(n):
    tmp_val = arr[idx]
    
    if tmp_val != before_val:
        before_val = tmp_val
        mx_cnt = max(mx_cnt, cur_cnt)
        cur_cnt = 0

    cur_cnt += 1

mx_cnt = max(mx_cnt, cur_cnt)
print(mx_cnt)