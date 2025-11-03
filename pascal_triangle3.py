total_rows=int(input())
for row in range(1,total_rows+1):
    ans=1
    print(ans,end=" ")
    for col in range(1,row): 
            ans=ans*(row-col) #numerator
            ans=ans//(col) #denominator
            'print(ans,end=" ")
    print()
