n = int(input())

def printer(n):
    if n == 0:
        return

    print("HelloWorld")
    printer(n - 1)

printer(n)