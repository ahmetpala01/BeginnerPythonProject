import random

class Mp3Calar():

    def sarkiSec(self):
       
        with open("Sarkılar.txt","r") as file:
            
            music_list = file.readlines()
            
            for x in range(0,len(music_list),1):
                
                print("{}".format(music_list[x]))
            
            secilecek_girilen = int(input("\n\nSeçilecek şarkının id'sini giriniz :"))
            if secilecek_girilen >= 1 and secilecek_girilen <= len(music_list):
               calan_sarki = music_list[secilecek_girilen-1].split(")")[1]
               return calan_sarki


            else:
                print("Olmayan bir değer girdiniz lobiye aktarılıyorsunuz . . .\n")
                return "Şuan birşey çalmıyor"

    def sesArttır(self,ses):
        if ses < 100:
            ses = ses + 1
            return ses
        else:
            print("Ses seviyesi zaten maksimum")
            return ses

    def sesAzalt(self,ses):
        if ses > 0:
            ses = ses - 1
            return ses
        else:
            print("Ses seviyesi zaten minimum")
            return ses

    def rasgeleSarkiSec(self):
        with open("Sarkılar.txt","r") as file:
            music_list = file.readlines()
        if len(music_list) > 0:
            rasgele_music = random.randint(0,len(music_list)-1)
            calan_sarki = music_list[rasgele_music].split(")")[1]
            return calan_sarki


    def sarkiEkle(self):
        id = 1
        sarkiad = input("Eklemek istediğiniz şarkı adı giriniz :")

        with open("Sarkılar.txt","r") as file:
            music_list = file.readlines()

            if len(music_list) == 0:
                id = 1

            else:
                with open("Sarkılar.txt","r") as file:
                    id = int(file.readlines()[-1].split(")")[0]) + 1

        with open("Sarkılar.txt","a+") as file:
            file.write("{}){}\n".format(id,sarkiad))
            print("'{}' ID'li '{}' isimli şarkı listeye eklendi".format(id,sarkiad))
            


    def sarkiSil(self):

        with open("Sarkılar.txt","r") as file:
            
            music_list = file.readlines()
            
            for x in range(0,len(music_list),1):
                
                print("{}".format(music_list[x]))
            
            silinecek_girilen = int(input("\n\nSilinecek şarkının id'sini giriniz :"))
            if silinecek_girilen >= 1 and silinecek_girilen <= len(music_list):
                music_list.pop(silinecek_girilen-1)
                yeni_music_list = list()
                yeni_id = 1

                for music in music_list:
                    yeni_music_list.append(str(yeni_id)+")"+music.split(")")[1])
                    yeni_id += 1
                
                with open("Sarkılar.txt","w") as file:
                    file.writelines(yeni_music_list)
                    

            else:
                print("Olmayan bir değer girdiniz lobiye aktarılıyorsunuz . . .\n")
          

    def ıslemSec(self):    
        
        with open("Sarkılar.txt","r") as file:
            sarki_listesi = music_list = file.readlines()
            if len(music_list) == 0:
                sarki_listesi = "Boş"
            else:
                sarki_listesi = music_list
                    
                    

        


        while True:
            print(""""
            Şarkı Listesi :
            """,end="")
            for music in sarki_listesi:
                print("""
                {}""".format(music),end="")
            print(""""
            Şuan Çalan Şarkı : {}
            Ses : {}

            1-Şarkı seç
            2-Sesi 1 arttır
            3-Sesi 1 azalt
            4-Rasgele şarkı seç
            5-Şarkı ekle
            6-Şarkı sil
            7-Kapat
            \n
            """.format(calan_sarki,ses))
            girilen_deger = int(input("Bir değer giriniz :"))
            while True:
                if girilen_deger >= 1 and girilen_deger <= 7:
                    return girilen_deger
            
                else:
                    girilen_deger = int(input("Lütfen 1-7 arası bir değer giriniz :"))
                    continue

                


mp3calar = Mp3Calar()
calan_sarki = "Şuan birşey çalmıyor"
ses = 100

while True:

    girilen_deger = mp3calar.ıslemSec()

    if girilen_deger == 1:
        with open("Sarkılar.txt","r") as file:
            music_list = file.readlines()
            if len(music_list) != 0:
                calan_sarki = mp3calar.sarkiSec()
                continue
            else:
                print("Lütfen ilk olarak şarkı ekleyin.")
                continue
    

    if girilen_deger == 2:
        ses = mp3calar.sesArttır(ses)
        continue

    if girilen_deger == 3:
        ses = mp3calar.sesAzalt(ses)
        continue

    if girilen_deger == 4:
        with open("Sarkılar.txt","r") as file:
            music_list = file.readlines()
            if len(music_list) != 0:
                calan_sarki = mp3calar.rasgeleSarkiSec()
                continue
            else:
                print("Lütfen ilk olarak şarkı ekleyin.")
                continue

    if girilen_deger == 5:
        mp3calar.sarkiEkle()
        continue

    if girilen_deger == 6:
        with open("Sarkılar.txt","r") as file:
            music_list = file.readlines()
            if len(music_list) != 0:
                mp3calar.sarkiSil()
                continue
            else:
                print("Lütfen ilk olarak şarkı ekleyin.")
                continue

    if girilen_deger == 7:
        print("Çıkış yapıldı")
        break