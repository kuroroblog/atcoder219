# 標準入力を受け付ける。
s1 = input()
s2 = input()
s3 = input()
# Tの文字列を1文字単位に分解して、リストへ入れる。
T = list(input())

ans = ''

# Tの文字数だけループを回す。
for i in range(0, len(T)):
    # Tのある文字が1の場合にS1, 2の場合にS2, 3の場合にS3を選択して、文字列連結する。
    if T[i] == '1':
        ans = ans + s1
    elif T[i] == '2':
        ans = ans + s2
    elif T[i] == '3':
        ans = ans + s3

print(ans)
