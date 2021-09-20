# 標準入力を受け付ける。
X = list(input())
N = int(input())

# 新しい辞書順を作成する。
alphaDict = {}
for i in range(0, len(X)):
    alphaDict[X[i]] = i + 1

SList = []
for i in range(0, N):
    name = input()
    nameNum = []
    for j in range(0, len(name)):
        # 新しい辞書順を元に、名前の英小文字に対応する番号を格納する。
        nameNum.append(alphaDict[name[j]])

    SList.append([nameNum, name])

# 名前の英小文字に対応する番号をソートする。
SList.sort()

for i in range(0, N):
    print(SList[i][1])
