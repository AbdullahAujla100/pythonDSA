class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularList:
    def __init__(self):
        self.head=None
        self.tail=None
        
        
    def insertEnd(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head=self.tail=new_node
            new_node.next=self.head

        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
           

    def insertBegining(self,data):
        new_node= Node(data)
        if self.head is None:
            self.head=self.tail=new_node
            new_node.next=self.head

        else:
            self.tail.next=new_node
            new_node.next=self.head
            self.head=new_node  
    
    def insertatIndex(self,data,pos):
        new_node= Node(data)
        if pos==1:
            self.insertBegining(data)

        current=self.head
        index = 0
        while current.next!=self.head and index < pos -1:
            current = current.next
            count += 1
        
        if current.next == self.head:
            self.insertEnd(data)
        else:
            new_node.next = current.next
            current.next = new_node

    def deletionStart(self):
        if self.head is None:
            print("No elements availabe to remove")

        elif self.head.next is self.head:
            self.head = self.tail= None

        else:
            self.head =self.head.next
            self.tail.next= self.head
            

    def deletionEnd(self):
        if self.head is None:
            print("No elements availabe to remove")

        elif self.head.next is self.head:
            self.head = self.tail= None

        else:
            current = self.head
            while current.next.next != self.head:
                current= current.next

           
            self.tail=current
            self.tail.next=self.head    


    def display(self):
        if self.head is None:
            print("Nothing to display")
        else:
            current= self.head
            while current.next != self.head:
                print(current.data,end="->")
                current=current.next 
            print(current.data,end="->") 
            print(self.head.data)      

cl=CircularList()
print("===INSERT-AT-END")
cl.insertEnd(10)                           
cl.insertEnd(20)                           
cl.insertEnd(30)                           
cl.insertEnd(40)
cl.display()
print("===INSERT-AT-START")
cl.insertBegining(5)
cl.insertBegining(1)


cl.display()
