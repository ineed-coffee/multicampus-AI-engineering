# 연습문제1 : Gravity

n,m = 9,9
gravity = [7,4,2,0,0,6,0,7,0]

Board = [[0]*m for _ in range(n)]

for j in range(len(gravity)):
    h = gravity[j]
    for i in range(n-1,n-1-h,-1):
        Board[i][j]=1


dp=[[0]*m for _ in range(n)]

for i in range(n):
    fall_acc=0
    for j in range(m-1,-1,-1):
        if Board[i][j]:
            dp[i][j]=fall_acc
        else:
            fall_acc+=1
Ans = max([max(i) for i in dp])
print(Ans)
