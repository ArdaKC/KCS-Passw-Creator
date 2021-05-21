import os

from random import choice
print("KCS PasswCreater Version 1.0")
print("Şifre Karakterlerini Manuel Yazmak İçin 1 Yazın. Şifre Karakterlerini Otomatik Yapması İçin 2 Yazın. Yazılımın Hakkında Kısmına Bakmak İçin 3 Yazın.")

secenek = input("")
if secenek == "3":
 print("yapımcı : Arda KC")
 print("Emeği Geçenler Arda KC + Furkan Karasu.")
 

if secenek == "2":

 karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
 print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
 sifreuzunluk =int(input())
 sifre = ""

 for i in range(sifreuzunluk):
    
    sifre += str(choice(karakterler1))
 pass
 print(sifre)

 os.system("exit")

if secenek == "1":
     

 print("Şifrenizde olmasını istediğiniz karakterleri girin.")
 karakterler = input("")
 print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
 sifreuzunluk =int(input())
 sifre = ""
 for i in range(sifreuzunluk):
    sifre += str(choice(karakterler))
 pass

 print(sifre)
 os.system("exit")
