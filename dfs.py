class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def dfs(root):
    if root is None:
        return
    print(root.data,end="")
    dfs(root.left)
    dfs(root.right)



root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.right.right=Node(7)
root.left.right=Node(4)
root.left.right.left=Node(5)
root.left.right.right=Node(6)


dfs(root)