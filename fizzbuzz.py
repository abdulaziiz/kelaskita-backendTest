def fizzBuzz(panjang):

    for num in range(1,panjang+1):
        
        if ((num % 3 == 0) and (num % 5 == 0)):
            print(num, end = " FizzBuzz\n")    
        elif num % 3 == 0:
            print(num, end = " Fizz\n")
        elif num % 5 == 0:
            print(num, end = " Buzz\n")
        else:    
            print(num, end="\n")

inputan = int(input("Masukkan Panjang Inputan = "))
fizzBuzz(inputan)