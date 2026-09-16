n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for q in queries:
    a, b = q[0], q[1]
    answer = sum(arr[a - 1:b])

    print(answer)    