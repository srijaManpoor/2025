n=int(input())
for row in range(n):
    for col in range(row):
        print(" ",end=" ")
    for col in range(2*(n-row)-1):
        print("*",end=" ")
    print()
