string = input()

for _ in range(len(string) - 1):
    del_idx = int(input())

    if del_idx >= len(string):
        string = string[:-1]

    string = string[:del_idx] + string[del_idx + 1:]
    print(string)