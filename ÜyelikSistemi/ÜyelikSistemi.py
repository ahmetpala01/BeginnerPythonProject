import json
from random import randint

class ÜyelikSistemi():
    def __init__(self):
        pass
    
    def hesap_varmi_kontrol(self,k_adı,sifre):
        
        try:
            with open("Üyeler.json","r") as file:
                veriler = json.load(file)
                for kullanici in veriler["Kullanicilar"]:
                    if kullanici["Kullanici_adi"] == k_adı and kullanici["Sifre"] == sifre:
                        print("Bu hesap daha önce oluşturulmuş")
                        return True
                    else:
                        return False
        except FileNotFoundError:
            print("Sistemin ilk hesabı oluşturuldu")
            return False
            
           

    def hesap_ekle(self,k_adı,sifre,email):           
        try:
            with open("Üyeler.json","r") as file:
                veriler = json.load(file)
                for kullanici in veriler["Kullanici"]:
                    if kullanici["Kullanici_adi"] == k_adı and kullanici["Sifre"] == sifre and kullanici["E-mail"] == email:
                        print("Bu hesap daha önce oluşturulmuştur")
        except FileNotFoundError:
            with open("Üyeler.json","w") as file:
                file.write("{}")

        with open("Üyeler.json","r") as file:
            veriler = json.load(file)

                
        try:
            veriler["Kullanicilar"].append({"Kullanici_adi":k_adı,"Sifre":sifre,"E-mail":email})
        except KeyError:
            veriler["Kullanicilar"] = []
            veriler["Kullanicilar"].append({"Kullanici_adi":k_adı,"Sifre":sifre,"E-mail":email})

        with open("Üyeler.json","w") as file:
            json.dump(veriler,file)
            print("Hesap eklendi")


    def unuttum(self):
        with open("Üyeler.json","r") as file:
            veriler = json.load(file)
    
        k_adı = input("Kullanıcı adınızı giriniz :")

        for kullanici in veriler["Kullanicilar"]:
            if kullanici["Kullanici_adi"] == k_adı:
                break

            else:
                print("Girdiğiniz kullanıcı adına ait bir hesap bulunamamıştır")
                self.program()


        email = input("e-mail'inizi giriniz :")

        for kullanici in veriler["Kullanicilar"]:
            if kullanici["E-mail"] == email:
                break

            else:
                print("Girdiğiniz e-mail'e ait bir hesap bulunamamıştır")
                self.program()
        
        aktivasyon = self.aktivasyon_kontrol()
        girilen_aktivasyon = int(input("Aktivasyon kodunu giriniz :"))

        if aktivasyon == girilen_aktivasyon:
            print("Aktivasyon kodu onaylandı")
            while True:
                while True:
                    sifre = input("Yeni şifre giriniz :")
                    if len(sifre) > 0:
                        break
                    else:
                        print("Boş girdiniz tekrar giriniz")
                        continue
                sifre_tekrar = input("Yeni şifreyi 2. kez giriniz :")
                if sifre != sifre_tekrar:
                    print("Şifreler uyumsuz tekrar giriniz")
                    continue
                else:
                    print("Şifreler uyumlu")
                    break

            for kullanici in veriler["Kullanicilar"]:
                if kullanici["Kullanici_adi"] == k_adı and kullanici["E-mail"] == email:
                    kullanici["Sifre"] = sifre
                    with open("Üyeler.json","w") as dosya:
                        json.dump(veriler,dosya)
                        print("Şifre değiştirilmiştir")
                    self.program()

        else:
            print("Girdiğiniz aktivasyon kodu yanlış")
            self.program()

    def aktivasyon_kontrol(self):
        uretılen_code = randint(1000,9999)

        with open("AktivasyonKodu.txt","w") as file:
            file.write(str(uretılen_code))

        return uretılen_code

    def girisyap(self):
        while True:
            k_adi = input("Kullanıcı adınızı giriniz :")
            if len(k_adi) > 0:
                break
            else:
                print("Boş girdiniz tekrar giriniz")
                continue
        while True:
            sifre = input("Şifrenizi giriniz :")
            if len(sifre) > 0:
                break
            else:
                print("Boş girdiniz tekrar giriniz")
                continue
        with open("Üyeler.json","r") as file:
            veriler = json.load(file)
            
            for kullanici in veriler["Kullanicilar"]:
                if kullanici["Kullanici_adi"] == k_adi and kullanici["Sifre"] == sifre:
                    aktivasyon = self.aktivasyon_kontrol()
                    girilen_aktivasyon = int(input("Aktivasyon kodunu giriniz :"))
                    if aktivasyon == girilen_aktivasyon:
                        print("'{}' kullanıcı ad'lı,'{}'sifre'li,'{}'e-mail'li hesaba giris yapıldı.".format(kullanici["Kullanici_adi"],kullanici["Sifre"],kullanici["E-mail"]))
                        break
                    else:
                        print("Aktivasyon kodunu yanlış girdiniz")
                        self.program()

        
    def program(self):
        print("""
        1-Giriş yap
        2-Kayıt ol
        3-Şifre mi unuttum
        4-Çıkış
        """)
        while True:
            try:
                girdi = int(input("Bir değer giriniz :"))
                if girdi >= 1 and girdi <= 4:
                    break
                else:
                    print("1-4 arası rakam girmelisin")
                    continue
            except:
                continue
        

        if girdi == 1:
            try:
                with open("Üyeler.json","r") as file:
                    veriler = json.load(file)
                    if len(veriler["Kullanicilar"]):
                        self.girisyap()
            except FileNotFoundError:
                print("Kayıtlı hesap yok")
                self.program()
        
        if girdi == 2:
            while True:
                k_adı = input("Kullanıcı adı giriniz :")
                if len(k_adı) > 0:
                    break
                else:
                    continue
            while True:
                while True:
                    sifre = input("Şifre giriniz :")
                    if len(sifre) > 0:
                        break
                    else:
                        print("Boş girdiniz tekrar giriniz")
                        continue
                if self.hesap_varmi_kontrol(k_adı,sifre):
                    self.program()
                sifre_tekrar = input("Şifreyi 2. kez giriniz :")
                if sifre != sifre_tekrar:
                    print("Şifreler uyumsuz tekrar giriniz")
                    continue
                else:
                    print("Şifreler uyumlu")
                    break
            while True:
                    email = input("Email giriniz :")
                    if len(email) > 0:
                        break
                    else:
                        print("Boş girdiniz tekrar giriniz")
                        continue
            aktivasyon = self.aktivasyon_kontrol()
            girilen_aktivasyon = int(input("Aktivasyon kodunu giriniz :"))
            if aktivasyon == girilen_aktivasyon:
                print("Aktivasyon kodunu doğru girdiniz.")
                self.hesap_ekle(k_adı,sifre,email)
                self.program()
            else:
                print("Aktivasyon kodunu yanlış girdiniz.")
                self.program()


        if girdi == 3:
            try:
                with open("Üyeler.json","r") as file:
                    veriler = json.load(file)
                    if len(veriler["Kullanicilar"]):
                        self.unuttum()
                    else:
                        print("Kayıtlı hesap yok")
                        self.program()
            except FileNotFoundError:
                print("Kayıtlı hesap yok")
                self.program()

        if girdi == 4:
            print("Çıkış yapıldı")
            pass




üyeliksistemi = ÜyelikSistemi()
üyeliksistemi.program()