# # Review for Test


# # 세 정수의 최대값 구하는 알고리즘
# def g_comp(a,b):
#     if a>b:
#         return a
#     return b

# a,b,c = map(int,input().split())
# print(g_comp(a,g_comp(b,c)))


# # 입력 받은 정수의 부호 출력
# num = int(input())
# if num>0:
#     print('+')
# elif not num:
#     print('0')
# else:
#     print('-')


# # 1~n 까지의 합
# n = int(input())
# a=0
# for i in range(1,n+1):
#     a+=i
# print(a)

# a=0
# i=1
# while i<=n:
#     a+=i
#     i+=1
# print(a)

# # a~b 까지의 합
# a,b = map(int,input().split())
# if a>b:
#     s_idx=b
#     e_idx=a+1
# else:
#     s_idx=a
#     e_idx=b+1

# S=0
# for i in range(s_idx,e_idx):
#     S+=i
# print(S)

# S=0;i=s_idx
# while i<e_idx:
#     S+=i
#     i+=1
# print(S)


# # 별 찍기
# n = int(input())

# L = 2*n-1
# for i in range(n):
#     center = 2*i-1
#     part = (L-center)//2
#     s = ' '*(part)+'*'*(center)+' '*(part)
#     print(s)


# 중앙값 찾기
a,b,c = map(int,input().split())
mid = a
if b<mid and c<mid:
    if b<c:
        mid=c
    else:
        mid=b
elif b>mid and c>mid:
    if b>c:
        mid=c
    else:
        mid=b

print(mid)