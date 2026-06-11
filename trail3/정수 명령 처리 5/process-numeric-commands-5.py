N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
num_list = []

for i in range(N):
    k = command[i]
    v = num[i]
    
    if k == 'push_back':
        num_list.append(v)
    elif k == 'pop_back':
        num_list.pop(v - 1)
    elif k == 'size':
        size = len(num_list)
        print(size)
    elif k == 'get':
        value = num_list[v - 1]
        print(value)