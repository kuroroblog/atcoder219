INF = 1000

# 標準入力を受け付ける。
N = int(input())
X, Y = map(int, input().split())

# i番目の弁当を食べた場合に、X, Yの目標に到達しているのか記録する。
# 途中経過も取得できるように動的計画法を利用する。
dp = [[[INF] * (Y + 1) for _ in range(X + 1)] for _ in range(N + 1)]

bentoList = []
for _ in range(N):
    a, b = map(int, input().split())
    bentoList.append((a, b))

# 初期設定を行う。
dp[0][0][0] = 0

for i in range(N):
    x, y = bentoList[i]
    for j in range(X + 1):
        # X以上の配列Indexを参照しないように、minを実行する。
        jj = min(j + x, X)
        for k in range(Y + 1):
            # 弁当を食べない場合、i番目の状態をi + 1番目へ引き継ぐ。
            # 下のコードにより、弁当を食べていて、i + 1番目が更新されている場合に、数値がずれないようにminをとる。
            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

            # Y以上の配列Indexを参照しないように、minを実行する。
            kk = min(k + y, Y)

            dp[i + 1][jj][kk] = min(dp[i + 1][jj][kk], dp[i][j][k] + 1)

print(dp[N][X][Y] if dp[N][X][Y] < INF else -1)
