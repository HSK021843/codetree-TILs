def find_min(x, y, z):
    min_value = min(x, y, z)

    return min_value


a, b, c = map(int, input().split())
res = find_min(a, b, c)

print(res)