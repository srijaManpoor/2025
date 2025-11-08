rows=int(input("enter the no.of rows"))
col=int(input("enter the no.of columns"))
Mat=[]
for i in range(rows):
        lst=list(map(int,input().split()))
        Mat.append(lst)
print(Mat)
