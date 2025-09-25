class Node:
    def __init__(self,val):
        self.left=None
        self.data=val
        self.right=None
root=Node(6)
root.left=Node(5)
root.right=Node(7)
root.left.right=Node(8)
root.right.left=Node(9)
def levelorder(root):
    if(root==None):
        return []
    ans=[]
    queue=[root]
    while(len(queue)>0):
        level=[]
        for i in range(len(queue)):
            popNode=queue.pop(0)
            if (popNode.left!=None):
                queue.append(popNode.left)
            if (popNode.right!=None):
                queue.append(popNode.right)
            level.append(popNode.data)
        ans.append(level)
    return ans
print(levelorder(root))

