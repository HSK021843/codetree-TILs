def find_number(n):
    a, b = n // 10, n % 10
    tmp = a + b

    if tmp % 5 == 0:
        print("Yes")
    else:
        print("No")


n = int(input())
find_number(n)