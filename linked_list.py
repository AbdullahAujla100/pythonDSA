class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        new_Node= Node(data)


        if self.head is None:
            self.head=new_Node

        else:
            current=self.head

            while current.next:
                current=current.next
            current.next=new_Node


    def insert_in_beginning(self,data):
        new_Node= Node(data)

        if self.head is None:
            self.head=new_Node

        else:
            new_Node.next=self.head
            self.head=new_Node

    def insert_at_position(self,data,pos):
        new_Node= Node(data)


        if pos == 0:
            self.insert_in_beginning(data)
            return

        
        current=self.head
        index=0

        while current and index < pos-1:
            current=current.next
            index+=1

        if current is None:
            print("position out of linked-list")
            return

        new_Node.next=current.next
        current.next=new_Node

    def deletion_at_beginning(self):
        if self.head is None:
            print("No element to remove")
        else:
            self.head=self.head.next

    def deletion_at_end(self):
        if self.head is None:
            print("No element to remove")
        elif self.head.next is None:
            self.head=None
        else:
            current =self.head
            while current.next.next:
                current=current.next
            current.next=None   

    def deletion_at_specific_pos(self,pos):

        if pos==0:
            self.deletion_at_beginning()
            return
        
        current=self.head
        index=0

        while current.next and index < pos -1:
            current=current.next
            index +=1

        if current.next is None:
            print("Position out of bounds")
            return
        
        current.next=current.next.next
    

            
    

    def display(self):
        current=self.head

        while current:
            print(current.data,end="->")
            current=current.next

        print("None")

ll = LinkedList()
print("===INSERTING-AT-END===")
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

ll.display()

print("====INSERT-IN_START====")
ll.insert_in_beginning(5)
ll.insert_in_beginning(1)

ll.display()

print("====INSERT-AT_SPECIFIC-POS====")
ll.insert_at_position(15,3)
ll.insert_at_position(25,5)
ll.display()

print("===DELETION-FROM-BEGINNING===")
ll.deletion_at_beginning()
ll.display()

print("===DELETION-FROM-END===")
ll.deletion_at_end()
ll.display()

print("===DELETION-AT-SPECIFIC-POSITION===")
ll.deletion_at_specific_pos(2)  
ll.display()
