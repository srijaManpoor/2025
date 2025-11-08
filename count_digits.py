n=int(input("enter number"))
def count_numbers(n):
    count=0
    if(n==0):
        return 1
    if(n<0):
        n=-n
    while(n>0):
        n=n//10
        count+=1
    return count
print(count_numbers(n))
