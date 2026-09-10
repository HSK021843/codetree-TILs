text = input()
pattern = input()

# Please write your code here.
st = 0
ed = st + len(pattern)

flag = 'No'
while ed <= len(text):
    if text[st:ed] == pattern:
        print(st)
        flag = "Yes"
        break

    st += 1
    ed += 1

if flag == 'No':
    print(-1)