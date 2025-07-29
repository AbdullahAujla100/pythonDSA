class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Que:
    def __init__(self):
        self.head=None

    def insert_at_end(self,data):
        new_Node= Node(data)
        if self.head is None:
            self.head = new_Node

        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_Node   


    def deletionBegining(self):
        if self.head is None:
            print("No elements available to remove")
            return
        
        else:
            self.head=self.head.next           

    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next

        print('None')    


qu= Que()

qu.insert_at_end(10)        
qu.insert_at_end(20)        
qu.insert_at_end(30)        
qu.insert_at_end(40)        
qu.insert_at_end(50)

qu.display()

print("Now poping")

qu.deletionBegining()
qu.deletionBegining()

qu.display()