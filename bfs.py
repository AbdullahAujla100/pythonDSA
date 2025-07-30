class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def bfs(root):
    if root is None:
        return 
    queue =[root]

    while queue:
        current= queue.pop(0)
        print(current.data,end="")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.right.right=Node(6)

bfs(root)