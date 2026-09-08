N = int(input())
arr = [int(input()) for _ in range(N)]

# Please write your code here.
st_v = 0
ed_v = 0
mx_length = -1

while ed_v < N:
    if arr[st_v] * arr[ed_v] > 0:
        ed_v += 1
    elif arr[st_v] * arr[ed_v] <0:
        mx_length = max(ed_v - st_v, mx_length)
        st_v = ed_v

mx_length = max(ed_v - st_v, mx_length)
print(mx_length)