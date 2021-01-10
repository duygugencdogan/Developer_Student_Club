#Fonksiyon Oluşturma

def maildogrulama(a, b):
    if a <= 3 & a > 0:
        print(a)
        print(b)
        print("Mail adresiniz doğrudur.")
        return True
    else:
        print("Mail adresiniz doğru değildir.")
        return False

    
uzantıUzunlugu = int(input("Lütfen mail adresinizin uzantısının uzunluğunu giriniz:"))
mailadresi = input("Lütfen mail adresinizi giriniz:")

maildogrulama(uzantıUzunlugu,mailadresi)