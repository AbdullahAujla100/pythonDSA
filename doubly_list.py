class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class DoublyList:
    def __init__(self):
        self.head=None
        self.tail=None


    def insertEnd(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head= self.tail =new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node    

    def insertStart(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head= self.tail =new_node

        else:
            self.head.prev=new_node
            new_node.next=self.head
            self.head=new_node

    def insertAtPos(self,data,pos):
        new_node=Node(data)

        if pos ==0:
            self.insertStart(data)

        else:
            current=self.head
            index=0
            while current and index < pos -1:
                current=current.next
                index+=1
            if current is None:
                print("Position out of range")
                return
            
            if current.next is None:
                self.insertEnd(data)
            
            else:
                 new_node.next=current.next
                 current.next.prev=new_node
                 current.next=new_node
                 new_node.prev=current  
                




    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current:
                print(current.data, end="<->")
                current=current.next

            print("None")                


dl=DoublyList()
print("===INSERTION-AT-END===")
dl.insertEnd(10)
dl.insertEnd(15)
dl.insertEnd(20)
dl.display()
print("===INSERTION-AT-START===")
dl.insertStart(1)
dl.insertStart(5)
dl.display()
print("===INSERT-AT-SPECIFIC-POS===")
dl.insertAtPos(13,3)
dl.display()