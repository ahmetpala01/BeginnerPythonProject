class Minigame():

    def __init__(self):
        self.tablo = [["1-1","1-2","1-3"],["2-1","2-2","2-3"],["3-1","3-2","3-3"]]
        self.sıra = 1
        self.finish = False
        
    def Restart(self):
        self.tablo = [["1-1","1-2","1-3"],["2-1","2-2","2-3"],["3-1","3-2","3-3"]]
        self.sıra = 1
        self.finish = False

    def tabloGoster(self):
        for i in range(0,3,1):
            for j in range(0,3,1):
                print(self.tablo[i][j]," ",end="")
            print("\n")

    def p1play(self):
        self.tabloGoster()
        print("1.Oyuncunun sırası")
        self.hamle(isaret="X ")

    def p2play(self):
        self.tabloGoster()
        print("2.Oyuncunun sırası")
        self.hamle(isaret="O ")

    def kontrol(self): # Oyunun bitip bitmediğini kontrol aşaması
            if self.tablo[0][0] == self.tablo[1][1] == self.tablo[2][2] or self.tablo[0][2] == self.tablo[1][1] == self.tablo[2][0]: #çaprazların kontrolü
                self.finish = True
            for x in range (0,3,1): #yatay ve dikey kontrol
                if self.tablo[x][0] == self.tablo[x][1] == self.tablo[x][2]: #yatay
                    self.finish = True
                    break
                if self.tablo[0][x] == self.tablo[1][x] == self.tablo[2][x]: #dikey
                    self.finish = True
                    break 
            
        


    def hamle(self,isaret = "-"):
        sutun = int(input("Sütun numarasını giriniz(1-3) :"))-1  
        satır = int(input("Satır numarasını giriniz(1-3) :"))-1

        if self.tablo[sutun][satır] == "X" or self.tablo[sutun][satır] == "O": #girilen yerde X veya O var mı ?
            print("Daha önce doldurulmuş bir yeri seçtiniz tekrar giriniz . . .")
            if isaret == "X":
                self.p1play()
            else:
                self.p2play()
        else:
            self.tablo[sutun][satır] = isaret

        self.kontrol()
        
       
        
        

    

    def program(self):
        self.Restart()
        for tur in range(1,10,1):   #max 9 tur oynanıcak.Erken biterse break ile çıkıcaz.
            if self.sıra % 2 == 1:  #1.oyuncunun sırası
                self.sıra += 1
                self.p1play()
                if self.finish == True:
                    print("1.Oyuncu kazandı.\n")
                    break
                
            else:                   #2.oyuncunun sırası
                self.sıra += 1
                self.p2play()
                if self.finish == True:
                    print("2.Oyuncu kazandı.\n")
                    break
        if self.finish == False: #beraberlik ?
            print("Beraberlik")

        girilen = input("Tekrar oynamak için P'yi tuşlayınız aksi halde oyun kapanıcaktır :") # restart ?

        if girilen == "P" or girilen == "p":
            self.program()

            





minigame = Minigame()
minigame.program()