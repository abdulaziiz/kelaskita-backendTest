# FUNGSI MEMBALIKKAN KATA
def balikKata(kalimat):
    
    # Ubah semua kalimat menjadi huruf kecil
    # Fungsinya untuk menyamakan huruf pada kalimat
    kalimat = kalimat.lower()

    # Potong kalimat menjadi kata per kata
    kataKata = kalimat.split(" ")

    # Rubah posisi huruf tiap kata sesuai susunan huruf  
    balikKata = [kata[::-1] for kata in kataKata]
      
    # Gabungkan kembali kata yang sudah dibalik menjadi kalimat baru  
    kalimatBalik = " ".join(balikKata)
  
    return kalimatBalik

inputan = input("Masukkan Kalimat Dengan Susunan Huruf Terbalik : ")
print("Kalimat Dengan Susunan Huruf Yang Benar : "+balikKata(inputan))