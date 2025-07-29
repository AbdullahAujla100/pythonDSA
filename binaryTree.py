class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def inOrdertraversal(node):
    if node is None:
        return
    inOrdertraversal(node.left)
    print(node.data, end=' ')
    inOrdertraversal(node.right)

def preOrdertraversal(node):
    if node is None:
        return
    print(node.data, end=' ')
    preOrdertraversal(node.left)
    preOrdertraversal(node.right)
        
def postOrdertraversal(node):
    if node is None:
        return
    postOrdertraversal(node.left)
    postOrdertraversal(node.right)
    print(node.data, end=' ')

def search(node,target):
    if node is None:
        return None
    elif node.data == target:
        return node
    elif target< node.data:
        return search(node.left,target)
    else:
        return search(node.right,target)
    
def insert(node,data):
    if node is None:
        return Tree(data)
    else:
        if data < node.data:
            node.left= insert(node.left,data)
        elif data > node.data:
            node.right=insert(node.right,data)

    return node        

def findMin(node):
    current=node
    while current.left is not None:
        current=current.left
    return current

def deleteNode(node,data):
    if not node:
        return None
    if data < node.data:
        node.left=deleteNode(node.left,data)
    elif  data > node.data:
        node.right=deleteNode(node.right,data)

    else:

        if not node.left:
            temp = node.right
            node=None
            return temp
        elif not node.right:
            temp= node.left
            node=None
            return temp
        
        
        node.data= findMin(node.right).data
        node.right=deleteNode(node.right,node.data)
    return node    



root=Tree(13)
nodeA=Tree(7)
nodeB=Tree(15)
nodeC=Tree(3)
nodeD=Tree(8)
nodeE=Tree(14)
nodeF=Tree(19)
nodeG=Tree(18)

root.left=nodeA
root.right=nodeB
nodeA.left=nodeC
nodeA.right=nodeD
nodeB.left=nodeE
nodeB.right=nodeF
nodeF.left=nodeG


print("===InOrderTraversal===")
inOrdertraversal(root)
print("\n===PreOrderTraversal===")
preOrdertraversal(root)
print("\n===PostOrderTraversal===")
postOrdertraversal(root)
print("\n")

result=search(root,13)
if result:
    print(f"found the number :{result.data}")
else:
    print("number not found")    

