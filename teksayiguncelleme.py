#ilk olarak kullanıcıdan liste girişi alalım.

myList = [] #boş bir liste oluşturuldu.
mySingleList = [] # tek sayılar listesi

for index in range(0,10):  #0 1 2 3 ..... 9
    myList.append(int(input("Lütfen {}. değeri giriniz:".format(index+1))))
           
print(myList)

for i in range(0, len(myList)):
    if myList[i] %2 != 0: 
        mySingleList.append(myList[i])
print(mySingleList)

for i in range(0, len(mySingleList)):
    if mySingleList[i] > mySingleList[i+1]:
        biggestValue  = mySingleList[i]
    else:
        biggestValue = mySingleList[i+1]

print(biggestValue)