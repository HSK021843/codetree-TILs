def find_number(a, b):
    total = 0

    for i in range(a, b + 1):
        str_i = str(i)
        
        if "3" in str_i or "6" in str_i or "9" in str_i or i % 3 == 0:
            total += 1

    return total

a, b = map(int, input().split())
res = find_number(a, b)

print(res)