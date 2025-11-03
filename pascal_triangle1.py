row=int(input("enter row number"))
col=int(input("enter column number"))
n=row-1
r=col-1
ans=1
for i in range(r):
    ans=ans*(n-i)
    ans=ans//(i+1)
print(ans)
