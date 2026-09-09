string = input()

for _ in range(len(string)):
    print(string)

    to_head = string[-1]
    else_string = string[0:-1]
    string = to_head + else_string

print(string)