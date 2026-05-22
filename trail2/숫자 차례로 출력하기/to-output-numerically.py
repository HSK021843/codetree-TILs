n = int(input())

number_list = [i + 1 for i in range(n)]

print(' '.join(map(str, number_list)))
print(' '.join(map(str, reversed(number_list))))