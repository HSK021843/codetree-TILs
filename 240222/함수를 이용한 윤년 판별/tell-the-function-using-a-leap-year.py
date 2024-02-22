def find_year(year):
    if year % 4 == 0 or (year % 100 == 0 and year % 400 != 0):
        print("true")
    else:
        print("false")

y = int(input())
res = find_year(y)