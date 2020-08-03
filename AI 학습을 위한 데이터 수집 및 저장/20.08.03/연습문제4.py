n = 10000
ans=0
for i in range(1,16):
    status=bin(i)
    status = status[2:]
    ones = status.count('1')
    ans+=ones*(9**(4-ones))
print(ans)
