row=int(input("enter row number"))
for col in range(1,row+1):
    n=row-1
    r=col-1
    ans=1
    for i in range(r): #time complexity is O(N**2) so we need to optimize
        ans=ans*(n-i) #numerator
        ans=ans//(i+1) #denominator
    print(ans,end=" ")
