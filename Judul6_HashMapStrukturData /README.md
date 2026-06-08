Sistem Pencarian Nama Menggunakan Nomor Absen

<img width="374" height="438" alt="Screenshot 2026-06-08 233626" src="https://github.com/user-attachments/assets/5b07c0e0-fe0d-4cbc-a773-0f32df29c1cb" />
<img width="341" height="440" alt="Screenshot 2026-06-08 233636" src="https://github.com/user-attachments/assets/94766fa7-902c-4ecd-a804-2667d18ddbe4" />
<img width="310" height="214" alt="Screenshot 2026-06-08 233643" src="https://github.com/user-attachments/assets/633dff27-e4c5-4b04-bdf9-30c6f9b2490d" />
<img width="343" height="295" alt="Screenshot 2026-06-08 233657" src="https://github.com/user-attachments/assets/673475a5-72ab-49e3-9503-6c66e70ff773" />

link yt : https://youtu.be/g9BZ3LD9ASc?si=4wpblCRkK_IYuV1X

penjelasan:
Kode ini mengimplementasikan tabel pencarian cepat (Hash Map) menggunakan metode Open Addressing dan Linear Probing untuk mengatur posisi data jika terjadi tabrakan indeks. Keunikan dari sistem ini terletak pada manajemen tiga status slot, yaitu EMPTY, OCCUPIED yaitu terisi, dan DELETED (pernah terisi namun sudah dihapus). Status DELETED ini berfungsi agar proses pencarian data lain tidak terputus di tengah jalan akibat adanya celah kosong pasca-penghapusan. Di dalam program, fungsi insert bertugas memasukkan data baru ke slot yang tersedia atau mengisi ulang slot bekas hapusan, sementara fungsi search dan remove_key bekerja berdampingan untuk mencari dan menghapus data berdasarkan nomor absen secara runtut. Melalui fungsi main(), program memperagakan seluruh simulasi ini secara nyata—mulai dari mendaftarkan enam nama siswa, menampilkan kondisi tabel, menghapus salah satu absen, hingga membuktikan bahwa sistem masih bisa menemukan data siswa lain dengan tepat meskipun struktur tabelnya baru saja berubah.
