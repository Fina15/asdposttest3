# asdposttest3

Pertama-tama, kita mengimpor modul pretty table untuk dapat menampilkan data dalam bentuk tabel yang rapi.

Selanjutnya, kita mendefinisikan kelas node yang berisi data dan pointer ke node berikutnya.

Kemudian kita mendefinisikan kelas linkedlist yang berisi head node dan beberapa metode, diantaranya adalah metode add untuk menambahkan data ke linkedlist, metode delete untuk menghapus data yang ada pada linkedlist, dan metode display untuk isi linkedlist dalam bentuk tabel yang rapi.

Method "add":
1. Membuat instance baru dari class Node dengan parameter data yang diteruskan. Node merupakan class untuk merepresentasikan sebuah simpul dalam linked list.
2. Memeriksa apakah linked list kosong (head-nya belum ada nilai). Jika iya, maka node baru yang telah dibuat akan menjadi head (pertama) dari linked list.
3. Jika linked list tidak kosong, maka kita harus menelusuri linked list dari head sampai ke simpul terakhir (simpul yang tidak memiliki next). Hal ini dilakukan dengan membuat variabel current yang diinisialisasi dengan head, lalu melakukan perulangan while sampai current.next bernilai None. Setiap iterasi, nilai current diganti dengan simpul berikutnya sampai sampul terakhir ditemukan.
4. Setelah sampul terakhir ditemukan, simpul baru (node) akan ditambahkan ke simpul terakhir tersebut dengan membuat simpul terakhir tersebut menunjuk ke simpul baru menggunakan atribut next.

Method "delete":
1. Memeriksa apakah linked list kosong (head-nya belum ada nilai). Jika iya, maka pesan "List is empty" akan dicetak.
2. Memeriksa apakah simpul yang akan dihapus berada pada posisi pertama (num == 1). Jika iya, maka head akan diubah menjadi simpul berikutnya sehingga simpul pertama akan terhapus.
3. Jika simpul yang akan dihapus tidak berada pada posisi pertama, maka kita harus menelusuri linked list untuk menemukan simpul yang akan dihapus. 
4. Variabel current diinisialisasi dengan head, prev diinisialisasi dengan None, dan count diinisialisasi dengan 1 (untuk menghitung posisi simpul saat ini). 
5. Kemudian, dilakukan perulangan while sampai current bernilai None (artinya simpul yang dicari tidak ditemukan) atau count sama dengan num (artinya simpul yang dicari sudah ditemukan). 
6. Setiap iterasi, nilai current diganti dengan simpul berikutnya, dan nilai prev diganti dengan current sebelumnya. 
7. Pada akhir perulangan, jika count sama dengan num, simpul yang dicari sudah ditemukan, dan simpul tersebut akan dihapus dengan membuat simpul sebelumnya (prev) menunjuk ke simpul berikutnya (current.next).

Method "display":
1. Pembuatan objek PrettyTable() dari library prettytable dengan nama variabel table.
2. Mendefinisikan field_names dari tabel dengan atribut "No.", "Merk", dan "Harga".
3. Inisialisasi variabel current dengan node pertama (head) dari linked list dan variabel count dengan 1.
4. Selama current bukan None, maka akan dilakukan perulangan while.
4. Pada setiap iterasi, akan menambahkan row baru ke tabel yang berisi nomor urut (count), merk (current.data["merk"]), dan harga (current.data["harga"]).
Kemudian pointer current diupdate ke node selanjutnya, dan variabel count ditambahkan 1.
6. Setelah perulangan selesai, tabel akan ditampilkan dengan menggunakan fungsi print(table).

Menu utama: 
Setiap kali program dijalankan, program akan menampilkan menu dengan opsi pilihan untuk menambahkan sepatu baru, menghapus sepatu, menampilkan daftar sepatu, atau keluar dari program. Program akan terus mengulang menu dan menunggu input dari pengguna sampai pengguna memilih untuk keluar dari program.

Ketika pengguna memilih untuk menambahkan sepatu baru (pilihan 1), program akan meminta pengguna untuk memasukkan merk dan harga sepatu baru yang akan ditambahkan. Kemudian, program akan menambahkan sepatu baru tersebut ke dalam daftar sepatu dan mencetak pesan bahwa sepatu berhasil ditambahkan.

Ketika pengguna memilih untuk menghapus sepatu (pilihan 2), program akan meminta pengguna untuk memasukkan nomor urut sepatu yang ingin dihapus. Kemudian, program akan menghapus sepatu dengan nomor urut tersebut dari daftar sepatu dan mencetak pesan bahwa sepatu berhasil dihapus.

Ketika pengguna memilih untuk menampilkan daftar sepatu (pilihan 3), program akan mencetak daftar sepatu yang telah ditambahkan sebelumnya.

Ketika pengguna memilih untuk keluar dari program (pilihan 4), program akan keluar dari loop while dan program selesai.

Jika pengguna memilih nomor selain 1, 2, 3, atau 4, program akan mencetak pesan bahwa menu tidak tersedia.
