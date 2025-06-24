n=int(input("enter number"))
original=n
rev=0
while(n>0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
if(original==rev):
      print("given number is a palindrome")
else:
      print("given number is not a palindrome")
          
