import os 
os.system('cls')

class Node:
    def __init__(self, merk, harga):
        self.merk = merk
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, merk, harga):
        new_node = Node(merk, harga)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display_list(self):
        if self.head is None:
            print("List kosong")
        else:
            current = self.head
            while current is not None:
                print("Merk: ", current.merk, ">>>", "Harga: ", current.harga)
                current = current.next

# contoh penggunaan linked list untuk toko sepatu
sepatu_list = LinkedList()
sepatu_list.add_node("Adidas", 800000)
sepatu_list.add_node("Nike", 700000)
sepatu_list.add_node("Puma", 600000)

sepatu_list.display_list()