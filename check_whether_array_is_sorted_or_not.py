def checksorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if(lst[i]<lst[i+1]):
            continue
        else:
            return False
    return True
lst=list(map(int,input().split()))
print(checksorted(lst))
