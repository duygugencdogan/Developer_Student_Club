#ilk olarak class'ları oluşturalım.

class Öğretmen():
    def __init__(self,ad,soyad,branş,maaş):
        self.ad = ad
        self.soyad = soyad
        self.branş = branş
        self.maaş = maaş

    def eğitimver(self):
        print("{} {} adlı öğretmen {} alanında eğitim verir.".format(self.ad,self.soyad,self.branş))

    def maaşal(self):
        print("{} {} adlı öğretmen {} tl maaş alır.".format(self.ad,self.soyad,self.maaş))

class Öğrenci():
    def __init__(self,ad,soyad,sınıf,şube):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.şube = şube

    def eğitimal(self):
        print("{} {} adlı öğrenci {}-{} sınıfında eğitim alır.".format(self.ad,self.soyad,self.sınıf,self.şube))
        
    def mezunol(self):
        print("{} {} adlı öğrenci mezun olur".format(self.ad,self.soyad))

class Okul():
    def __init__(self,okulunadı,şubesayısı,öğretmensayısı,öğrencisayısı):
        self.okulunadı = okulunadı
        self.şubesayısı = şubesayısı
        self.öğretmensayısı = öğretmensayısı
        self.öğrencisayısı = öğrencisayısı
        print("{} Okulu'na Hoş Geldiniz...Okulumuzda {} öğretmen {} tane şube ile {} öğrenciye eğitim vermektedir.".format(self.okulunadı,self.öğretmensayısı,self.şubesayısı,self.öğrencisayısı))

    """def __init__(self,okulunadı,Çalışan,Öğrenci,şubesayısı,öğretmensayısı,öğrencisayısı):
        print("{} Okulu'na Hoş Geldiniz...")
        self.okulunadı = okulunadı
        self.Öğretmen = Öğretmen
        self.Öğrenci = Öğrenci
        self.şubesayısı = şubesayısı
        self.öğretmensayısı = öğretmensayısı
        self.öğrencisayısı = öğrencisayısı"""

    def eğitimver(self):
        print("{} Okulu 2019-2020 Bahar Dönemine Hoş Geldiniz.".format(self.okulunadı))

    def mezunet(self):
        print("{} Okulu mezuniyetine Hoş Geldiniz...".format(self.okulunadı))

#Inheritance -> Miras alma 

class OkulA(Okul):
    pass
class OkulB(Okul):
    pass
class OkulC(Okul):
    pass

#alt class miras alınmış class tan farklı bir özellik ekleme
class SayısalÖğrencisi(Öğrenci):
    def __init__(self,ad,soyad,sınıf,şube,bolum):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.şube = şube
        self.bolum = bolum
        print("{}-{} sınıfından {} {} adlı öğrenci {}cıdır.".format(self.sınıf,self.şube,self.ad,self.soyad,self.bolum))

class SozelÖğrencisi(Öğrenci):
    def __init__(self,ad,soyad,sınıf,şube,bolum):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.şube = şube
        self.bolum = bolum
        print("{}-{} sınıfından {} {} adlı öğrenci {}cidir.".format(self.sınıf,self.şube,self.ad,self.soyad,self.bolum))

class EşitAğırlıkÖğrencisi(Öğrenci):
    def __init__(self,ad,soyad,sınıf,şube,bolum):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.şube = şube
        self.bolum = bolum
        print("{}-{} sınıfından {} {} adlı öğrenci {} Öğrencisidir.".format(self.sınıf,self.şube,self.ad,self.soyad,self.bolum))    

class DilÖğrencisi(Öğrenci):
    def __init__(self,ad,soyad,sınıf,şube,bolum):
        self.ad = ad
        self.soyad = soyad
        self.sınıf = sınıf
        self.şube = şube
        self.bolum = bolum
        print("{}-{} sınıfından {} {} adlı öğrenci {}cidir.".format(self.sınıf,self.şube,self.ad,self.soyad,self.bolum))


#nesne oluşturup ekrana print etme
print("-"*25+"OKUL"+"-"*25)

okul1 = OkulA("Piri Reis Anadolu Lisesi",5,35,600)
okul1.eğitimver()
okul1.mezunet()

print("-"*25+"ÖĞRENCİ"+"-"*25)

öğrenci1 = SayısalÖğrencisi("Duygu","Gençdoğan","12","C","Sayısal")
öğrenci1.eğitimal()
öğrenci1.mezunol()

print("-"*25+"ÖĞRETMEN"+"-"*25)

öğretmen1 = Öğretmen("Mehmet","Özen","Fizik","4000")
öğretmen1.eğitimver()
öğretmen1.maaşal()