#it is optimized code
#time complexity is O(N)
row=int(input())
ans=1
print(ans,end=" ")
for col in range(1,row):
    #already 0th index(1) is printed so we are taking range from 1st index
    ans=ans*(row-col)
    ans=ans//col
    print(ans,end=" ")
