n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
answer = [0] * n
seq_enumerated = sorted(enumerate(sequence), key=lambda x: x[1])

for enumerated_idx, (original_idx, value) in enumerate(seq_enumerated):
    answer[original_idx] = str(enumerated_idx + 1)

print(' '.join(answer))