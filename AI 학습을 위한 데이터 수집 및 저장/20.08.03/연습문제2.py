import sys

input = sys.stdin.readline

String_in = input().rstrip()
S,idx,flag = len(String_in),0,True
while idx<len(String_in):
    if String_in[idx]!=String_in[(S-1)-idx]:
        flag=False
        break
    idx+=1
print("YES" if flag else 'NO')
