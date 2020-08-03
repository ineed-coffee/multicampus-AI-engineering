n= 5000
Gen = [False]*(n+1)
for i in range(n+1):
    generated=i
    div=sum(list(map(int,str(i))))
    generated+=div
    if generated<=n:
        Gen[generated]=True

Ans=0
for i in range(1,n+1):
    if not Gen[i]:
        Ans+=i

print(Ans)
