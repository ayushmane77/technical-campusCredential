# class LinkedList:
#     def __init(self):
#         self.head=None
#         self.tail=None
#         self.length=0

#     def append(self,value):
#         new_node=Node(value)
#             if self.head is None:
#                 self.head=new_node  
#                 self.tall=new_node
#             else:
#                 self.tail.next=new_node
#                 self.tail=new_node

#             self.length=1

# new_linked_list=LinkedList()
# new_linked_list.append(10)
# new_linked_list.append(20)                  


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)  
        if self.head is None:
            self.head = new_node  
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1  

    def insert(self, index, value):
        new_node = Node(value)
        if self.head is None:
                self.head = new_node
                self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
        for i in range(index - 1):
            if temp_node.next is None:
                raise IndexError("Index out of range")
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1     

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)  
new_linked_list.prepend(5)
new_li = LinkedList()
current_node = new_linked_list.head
while current_node:
    print(current_node.data)
    current_node = current_node.next

