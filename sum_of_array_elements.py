n=int(input())
arr=list(map(int,input().split()))
if len(arr)!=n:
    print("error no.of elements in array is not equal to n")
else:
    i=sum(arr)
    print(i)
    
