import os
os.system('cls')
from prettytable import PrettyTable

# Membuat kelas Node untuk Linked List
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Membuat kelas LinkedList untuk toko sepatu
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan sepatu ke Linked List
    def add(self, data):
        node = Node(data)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    # Menghapus sepatu dari Linked List berdasarkan nomor urut pada tabel
    def delete(self, num):
        if not self.head:
            print("List is empty")
        elif num == 1:
            self.head = self.head.next
        else:
            current = self.head
            prev = None
            count = 1
            while current and count != num:
                prev = current
                current = current.next
                count += 1
            if count == num:
                prev.next = current.next
            else:
                print("Invalid node number")

    # Menampilkan daftar sepatu dengan menggunakan prettytable
    def display(self):
        table = PrettyTable()
        table.field_names = ["No.", "Merk", "Harga"]
        current = self.head
        count = 1
        while current:
            table.add_row([count, current.data["merk"], current.data["harga"]])
            current = current.next
            count += 1
        print(table)

# Inisialisasi Linked List dengan beberapa data sepatu
shoe_list = LinkedList()
shoe_list.add({"merk": "Nike", "harga": 500000})
shoe_list.add({"merk": "Adidas", "harga": 700000})
shoe_list.add({"merk": "Puma", "harga": 600000})

# Menu utama
while True:
    print("\nMenu:")
    print("1. Tambah sepatu")
    print("2. Hapus sepatu")
    print("3. Tampilkan daftar sepatu")
    print("4. Keluar")
    choice = input("Pilih menu (1/2/3/4): ")

    if choice == "1":
        merk = input("Masukkan merk sepatu: ")
        harga = int(input("Masukkan harga sepatu: "))
        shoe_list.add({"merk": merk, "harga": harga})
        print("Sepatu berhasil ditambahkan")

    elif choice == "2":
        num = int(input("Masukkan nomor urut sepatu yang ingin dihapus: "))
        shoe_list.delete(num)
        print("Sepatu berhasil dihapus")

    elif choice == "3":
        shoe_list.display()

    elif choice == "4":
        break

    else:
        print("Menu tidak tersedia")
