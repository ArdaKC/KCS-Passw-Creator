import os

from random import choice
print("KCS PasswCreater 1.0 By Arda KC")
print("Şifre Karakterlerini Manuel Yazmak İçin 1 Yazın. Şifre Karakterlerini Otomatik Yapması İçin 2 Yazın. ")

manuelorautomatic = input("")
if manuelorautomatic == "2":

 karakterler1 = "qwertyuoopasdfghklizxcvbnm1234567890?-+?=%&/()'^!"
 print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
 sifreuzunluk =int(input())
 sifre = ""

 for i in range(sifreuzunluk):
    
    sifre += str(choice(karakterler1))
print(sifre)
os.system("exit")



if manuelorautomatic == "1":
     

 print("Şifrenizde olmasını istediğiniz karakterleri girin.")
 karakterler = input("")
 print("Şifrenizin Uzunluğu Kaç Karakter Olsun")
 sifreuzunluk =int(input())
 sifre = ""
 for i in range(sifreuzunluk):
    sifre += str(choice(karakterler))
     
print(sifre)
os.system("exit")
