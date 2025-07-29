class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
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


    def deletion_from_end(self):
        if self.head is None:
            print("No elements available to remove")
            return
        
        elif self.head.next is None:
            self.head=None

        else:
            current =self.head
            while current.next.next:
                current=current.next

            current.next=None

    def display(self):
        current=self.head
        while current:
            print(current.data,end='->')
            current=current.next

        print('None')    


st= Stack()

st.insert_at_end(10)        
st.insert_at_end(20)        
st.insert_at_end(30)        
st.insert_at_end(40)        
st.insert_at_end(50)

st.display()

print("Now poping")

st.deletion_from_end()
st.deletion_from_end()

st.display()