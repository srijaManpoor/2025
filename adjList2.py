n=int(input("enter n value"))
m=int(input("enter m value"))
edges=list(map(int,input().split( )))
adjList=[]
for i in range(n):
    adjList.append([])
for n,m in edges:
    adjList[n].append(m)
    adjList[m].append(n)
print(adjList)
