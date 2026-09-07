n, q = map(int, input().split())
val_list = list(map(str, input().split(' ')))

# 1 a -> a번째 원소 출력
# 2 b -> b인 원소의 인덱스(최소 인덱스), 없으면 0
# 3 s e -> s부터 e를 공백으로 구분, 차례로 출력

for _ in range(q):
    query_to_list = list(map(int, input().split(' ')))
    order = query_to_list[0]

    if order == 1:
        target_val = query_to_list[1]

        print(val_list[target_val - 1])

    elif order == 2:
        target_val = query_to_list[1]

        try:
            print(val_list.index(str(target_val)) + 1)
        except:
            print(0)

    elif order == 3:
        st = query_to_list[1]
        ed = query_to_list[2]

        tmp = val_list[st - 1:ed]

        print(' '.join(tmp))