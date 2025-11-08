n,m=4,3
edges=[[0,1],[0,2],[1,3]]
adjList=[]
for i in range(n):
    adjList.append([])
for n,m in edges:
    adjList[n].append(m)
    adjList[m].append(n)
print(adjList)
