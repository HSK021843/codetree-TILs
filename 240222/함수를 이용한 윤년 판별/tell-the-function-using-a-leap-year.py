def find_year(year):
    if year % 4 == 0:
        if (year % 100 == 0 and year % 400 != 0):
            print("false")
        else:
            print("true")
    else:
        print("false")

y = int(input())
res = find_year(y)