class BankaHesabi:
    def __init__(self,hesap_sahibi,bakiye=0):
        self.hesap_sahibi=hesap_sahibi
        self.bakiye=bakiye
    def para_yatir(self):
        miktar=int(input("Yatıracağınız para miktarını giriniz:"))
        self.bakiye+=miktar
        print("Bakiyeniz:",self.bakiye)
    def para_cek(self):
        miktar=int(input("Çekeceğiniz para miktarını giriniz:"))
        if miktar<=self.bakiye:
            self.bakiye-=miktar
            print("Bakiyeniz:",self.bakiye)
        else:
            print("Yetersiz Bakiye!")

hesap1=BankaHesabi("Ahmet")
while True:
    hesap1.para_yatir()
    hesap1.para_cek()
