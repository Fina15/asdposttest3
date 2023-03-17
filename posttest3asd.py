import os
os.system('cls')
from prettytable import PrettyTable

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def display(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        x = PrettyTable()
        x.field_names = ["ID", "Brand", "Type", "Color", "Size", "Price"]
        curr_node = self.head
        while curr_node is not None:
            x.add_row(curr_node.data)
            curr_node = curr_node.next
        print(x)

# Contoh penggunaan
ll = LinkedList()
ll.add([1, "Nike", "Running Shoes", "Black", "9", 1500000])
ll.add([2, "Adidas", "Sneakers", "White", "8", 1200000])
ll.add([3, "Puma", "Football Shoes", "Red", "10", 2000000])
ll.display()
