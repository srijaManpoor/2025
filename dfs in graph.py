def dfs(startNode,visited,ans,adjList):
    ans.append(startNode)
    for i in adjList[startNode]:
        if(visited[i]==0):
            visited[i]=1
            dfs(i,visited,ans,adjList)
def depthFirstSearch(adjList):
    v=len(adjList)
    visited=[0]*v
    ans=[]
    StartNode=0
    if(visited[StartNode]==0):
        visited[StartNode]=1
        dfs(StartNode,visited,ans,adjList)
        return ans
v,p=4,3
edges=[[0,1],[0,2],[1,3]]
adjList=[]
for i in range (v):
    adjList.append([])
for n,m in edges:
    adjList[n].append(m)
    adjList[m].append(n)
print(depthFirstSearch(adjList))



      
