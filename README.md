# asdposttest3

Dalam contoh di atas, Node merepresentasikan sebuah data sepatu dengan atribut merk dan harga serta pointer next yang menunjukkan ke node berikutnya dalam linked list. LinkedList merepresentasikan kumpulan dari node-node tersebut, dengan head sebagai node pertama dalam linked list.

Metode add_node digunakan untuk menambahkan node baru ke linked list. Pertama, membuat objek new_node dengan nilai atribut merk dan harga yang diberikan. Jika linked list masih kosong, maka new_node menjadi head. Jika tidak, maka iterasi ke node terakhir dalam linked list (while current.next is not None) dan menambahkan new_node sebagai node berikutnya.

Metode display_list digunakan untuk menampilkan semua node dalam linked list. Jika linked list masih kosong, maka menampilkan pesan "List kosong". Jika tidak, maka iterasi ke setiap node dalam linked list dan menampilkan nilai atribut merk dan harga dari setiap node.
