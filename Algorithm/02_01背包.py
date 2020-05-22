n, v = map(int, input().split())
goods = []
for i in range(n):
    goods.append([int(i) for i in input().split()])

dp = [0 for i in range(v + 1)]

for i in range(n):
    for j in range(v, -1, -1):  # 从后往前
        if j >= goods[i][0]:
            dp[j] = max(dp[j], dp[j - goods[i][0]] + goods[i][1])

print(dp[-1])
