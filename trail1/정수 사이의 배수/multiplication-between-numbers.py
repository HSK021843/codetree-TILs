a, b = map(int, input().split())

num_lst = []
for n in range(a, b + 1):
    if n % 5 == 0 or n % 7 == 0:
        num_lst.append(n)

print(sum(num_lst), round(sum(num_lst) / len(num_lst), 1))