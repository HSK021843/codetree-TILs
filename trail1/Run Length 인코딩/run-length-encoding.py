def update_answer_list(before, count):
    answer.append(before)
    answer.append(str(count))


A = input()
answer = []

# Please write your code here.
before = A[0]
count = 1

for i in range(1, len(A)):
    tmp = A[i]
    
    if tmp != before:
        update_answer_list(before, count)
        before = tmp
        count = 0
    
    count += 1

update_answer_list(before, count)
tmp = ''.join(answer)

print(len(tmp))
print(tmp)