import os
import os.path
from random import choice


print("KCS PasswCreater Version 1.1")
print("Şifre Karakterlerini Manuel Yazmak İçin : 1")
print("Şifre Karakterlerini Otomatik Yapması İçin : 2")
print("Yazılımın Hakkında Kısmına Bakmak İçin : 3")
print("Ayarlamalar Yapmak İçin : 4")
secenek = input("")
if secenek == "4":
   print("Oluşturulan Son Şifre Kayıt Edilsin Bir Önceki Silinsin         : 1")
   print("Oluşturulan Şifreler Yeni Metin Belgesine Satırca Kayıt Edilsin : 2")
   print("Ayarları Sıfırla : 3")

   ayar = input("")
   if ayar == "3":
      os.remove("ayar1.txt")
      print("ayarlar başarıyla sıfırlandı! Oluşturulan sife dosyaları silinsin mi? evet \ hayır")
      secenek2 = input("")
      if secenek2 == "evet":
        os.remove("sifreler.txt")
        os.remove("sifre.txt")
        print("işlem başarıyla uygulandı.")
   if ayar == "2":
      with open("ayar1.txt", "w") as f:
        print("sifreler.txt varsa silinsin mi? : evet \ hayır")
        silit = input("")
        if silit == "evet":
         os.remove("sifreler.txt")
         f.write(ayar)
         print("ayar1.txt başarıyla kayıt edildi.")
         os.system("exit")
        else:
          f.write(ayar)
          print("ayar1.txt başarıyla kayıt edildi.")
          os.system("exit")
   if ayar == "1":
      with open("ayar1.txt", "w") as f:
         print("sifre.txt varsa silinsin mi? : evet \ hayır")
         silinsinmi = input("")
         if silinsinmi == "evet":
          os.remove("sifre.txt")
          f.write(ayar)
          print("ayar1.txt başarıyla kayıt edildi.")
          os.system("exit")
         else:
          f.write(ayar)
          print("ayar1.txt başarıyla kayıt edildi.")
          os.system("exit")

     
  
if secenek == "3":
 print("Bu yazılım Arda KC Tarafından Yapılmıştır.")

 

if secenek == "2":



 dosyavarmı = os.path.isfile("ayar1.txt")
 PATH='./ayar1.txt'
 if os.path.isfile(PATH) and os.access(PATH, os.R_OK):



     with open("ayar1.txt", "r") as f:
        
       open("ayar1.txt","r")
      
       ayar = f.read()
       print(ayar)
          
     if ayar == "1":

        with open("sifre.txt", "w") as f:
          sifre = ""

          karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
          print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
          sifreuzunluk = int(input())

      
          for i in range(sifreuzunluk):
          
            sifre += str(choice(karakterler1))
          pass
          
          f.write(sifre)
          print(sifre)
          print("oluşturulan şifre sifre.txt dosyasına kayıt edildi.")
          os.system("exit")


     else:
        if ayar == "2":
          sifre = ""
          karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
          print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
          sifreuzunluk = int(input())
          for i in range(sifreuzunluk):
          
            sifre += str(choice(karakterler1))
          pass
          print(sifre)

          with open("sifreler.txt", "a") as f:
            
          
            f.write("\n"+sifre)
            
          
            print("oluşturulan şifre sifreler.txt dosyasına kayıt edildi.")
        
            os.system("exit")
          pass
        else:
         sifre = ""
         karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
         print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
         sifreuzunluk = int(input())

 
         for i in range(sifreuzunluk):
    
           sifre += str(choice(karakterler1))
         pass
     
      
         print(sifre)
     
   
         os.system("exit")
 else:



    karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
    print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
    sifreuzunluk = int(input())
    sifre = ""
    for i in range(sifreuzunluk):
    
        sifre += str(choice(karakterler1))
    pass
     
      
    print(sifre)
     
   
    os.system("exit")
      
       

 
if secenek == "1":

    with open("ayar1.txt", "r") as f:

        open("ayar1.txt", "r")

        ayar = f.read()
        print(ayar)

    if ayar == "1":

        with open("sifre.txt", "w") as f:
            sifre = ""

            karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
            print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
            sifreuzunluk = int(input())

            for i in range(sifreuzunluk):
                sifre += str(choice(karakterler1))
            pass

            f.write(sifre)
            print(sifre)
            print("oluşturulan şifre sifre.txt dosyasına kayıt edildi.")
            os.system("exit")


    else:
        if ayar == "2":
            sifre = ""
            print("Şifrenizde olmasını istediğiniz karakterleri girin.")
            karakterler = input("")
            print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
            sifreuzunluk = int(input())

            for i in range(sifreuzunluk):
                sifre += str(choice(karakterler))
            pass
            print(sifre)

            with open("sifreler.txt", "a") as f:

                f.write("\n" + sifre)

                print("oluşturulan şifre sifreler.txt dosyasına kayıt edildi.")

                os.system("exit")
            pass
        else:
            sifre = ""
            print("Şifrenizde olmasını istediğiniz karakterleri girin.")
            karakterler = input("")
            print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
            sifreuzunluk = int(input())


            for i in range(sifreuzunluk):
                sifre += str(choice(karakterler))
            pass

            print(sifre)
            os.system("exit")



