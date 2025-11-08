n,m=4,3
edges=[[0,1],[0,2],[1,3]]
adjMat=[]
for i in range(n):
    lst=[ ]*n
    adjMat.append(lst)
for i,j in edges:
    adjMat[i][j]=1
    adjMat[j][i]=1
print(adjMat)

