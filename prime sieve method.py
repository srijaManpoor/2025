n=int(input("enter the number to get prime numbers count below that number"))
prime=[1]*n
for i in range(2,int(n**0.5)+1):
    if(prime[i]==1):
        for j in range(i*i,n,i):
            prime[j]=0
count=0
for i  in range(2,n):
    if(prime[i]==1):
        count=count+1
print(count)
