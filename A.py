# 標準入力を受け付ける。
X = int(input())

# Xの値が90点以上の場合、expertを返す。
if X >= 90:
    print('expert')
    exit()

score = 0
# Xの値が0点以上~39点以内の場合、40 - Xの値を返す。
if X >= 0 and X <= 39:
    score = 40 - X
# Xの値が40点以上~69点以内の場合、70 - Xの値を返す。
elif X >= 40 and X <= 69:
    score = 70 - X
# Xの値が70点以上~89点以内の場合、90 - Xの値を返す。
elif X >= 70 and X <= 89:
    score = 90 - X

print(score)
