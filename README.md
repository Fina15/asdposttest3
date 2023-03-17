# asdposttest3

Pertama-tama, kita mengimpor modul prettytable untuk dapat menampilkan data dalam bentuk tabel yang rapi.
Selanjutnya, kita mendefinisikan kelas Node yang berisi data dan pointer ke node berikutnya.
Kemudian, kita mendefinisikan kelas LinkedList yang berisi head node dan beberapa metode, di antaranya adalah metode add untuk menambahkan data ke linked list, dan metode display untuk menampilkan isi linked list dalam bentuk tabel yang rapi.
Pada metode add, kita membuat sebuah node baru dan menambahkannya ke akhir linked list dengan mengiterasi dari head node sampai ke node terakhir, dan menambahkan node baru tersebut sebagai node berikutnya dari node terakhir.
Pada metode display, kita menggunakan modul prettytable untuk membuat tabel dengan header dan data yang disimpan di linked list. Pertama-tama, kita memeriksa apakah linked list kosong. Jika tidak, kita membuat objek PrettyTable dan menentukan nama-nama kolom dengan field_names. Selanjutnya, kita mengiterasi dari head node sampai ke node terakhir dan menambahkan data dari setiap node ke tabel menggunakan metode add_row. Terakhir, kita mencetak tabel tersebut dengan metode print.
Pada contoh penggunaan, kita membuat objek LinkedList, menambahkan beberapa data ke linked list, dan menampilkan isi linked list dalam bentuk tabel.
