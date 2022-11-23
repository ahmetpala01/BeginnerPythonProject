import random

akılda_tutulan_sayi = random.randint(1,100)
deneme_hakkı = 7

while True:
    if deneme_hakkı == 0:
        print("\n{} hakkınız kaldığı için kaybettiniz\n".format(deneme_hakkı))
        if int(input("Yeniden denemek istiyorsanız 1'e basınız.")) == 1:
            deneme_hakkı = 7
            akılda_tutulan_sayi = random.randint(1,100)
            continue

        else:
            print("Game Over")
            break

    else:

        print("\n1-100 arası bir sayı akılda tutulmuştur tahmin etmek için {} hakkın kaldı\n".format(deneme_hakkı))
        girilen_sayi = int(input("Tahmininiz: "))

        if girilen_sayi == akılda_tutulan_sayi:
            print("\nTebrikler doğru tahmin ettiniz akılda tutulan say = {}\n".format(akılda_tutulan_sayi))
            break
        else:
            if girilen_sayi > akılda_tutulan_sayi:
                print("\nDaha aşağıda\n")
            else:
                print("\nDaha yukarıda\n")
            deneme_hakkı -= 1
            continue


