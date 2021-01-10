#3'e tam bölünüyorsa -> Fizz
#5'e tambölünüyorsa -> Buzz
#3 ve 5'e tam bölünüyorsa ->FizzBuzz
#0-100 aralığındaki sayılar

cikti = ""
for i in range(1, 100):
    if i%3 == 0:
        sonuc = "Fizz"
    elif i%5 == 0:
        sonuc = "Buzz"
    elif i%15 == 0:
        sonuc = "FizzBuzz" 
    else:
        sonuc = str(i) 
    cikti += sonuc + ","
print(cikti + "...")
