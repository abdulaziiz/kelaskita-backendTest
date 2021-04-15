def deretFibonacci(panjang):
    awal=0                                         
    lanjut=1
    mantap = ""                                         
    if panjang<=0:
        print("Angka Tidak Boleh <= 0",awal)
    else:
        print(awal,lanjut,end=" ")
        for i in range(2,panjang):
            next=awal+lanjut                           
            mantap = print(next,end=" ")
            awal=lanjut
            lanjut=next
            
inputan = int(input("Masukkan Panjang Deret = "))
deretFibonacci(inputan)