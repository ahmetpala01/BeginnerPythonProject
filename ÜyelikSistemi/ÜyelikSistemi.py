import json

class ÜyelikSistemi():
    def __init__(self):
        pass
        
    def giris(self):
        k_adı = input("Kullanıcı adı giriniz :")
        sifre = input("Şifre giriniz :")
    
        with open("Üyeler.json","r") as file:
            veriler = json.load(file)
            for kullanici  in veriler["Kullanicilar"]:
                if k_adı == kullanici["kullanici_adi"] and sifre == kullanici["sifre"]:
                    print("Giriş yapıldı")
                else:
                    print("İşlem başarısız")


    def kayıt(self):
        k_adı = input("Kullanıcı adı giriniz :")
        sifre = input("Şifre giriniz :")
        email = input("e-mail giriniz :")
        

        eklenecek_hesap = dict()
        eklenecek_hesap["Kullanicilar"] = list()
        eklenecek_hesap["Kullanicilar"].append({"kullanici_adi":"{}".format(k_adı),"sifre":"{}".format(sifre),"e-mail":"{}".format(email),})

        with open("Üyeler.json","a") as file:
            json.dump(eklenecek_hesap["Kullanicilar"],file)
            
    def s_unuttum(self):
        pass

    def cıkıs(self):
        pass

    def program(self):
        self.kayıt()
        self.giris()



üyeliksistemi = ÜyelikSistemi()
üyeliksistemi.program()