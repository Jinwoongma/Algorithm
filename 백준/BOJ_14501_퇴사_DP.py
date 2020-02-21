N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)
value = [0] * (N + 2)

for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

for i in range(1, N + 2):
    for j in range(1, i):
        # 1) j 번째 날에서 일을 안하고 i 번째 날까지 온 경우(j < i)
        value[i] = max(value[i], value[j])

        # 2) j 번째 날에서 t[j] 기간 동안 일을하고 보상을 p[j] 받은 경우
        # 그 보상은 j + t[j] 날 받는다.
        if j + T[j] == i:
            value[i] = max(value[i], value[j] + P[j])

print(value)
print(max(value))

