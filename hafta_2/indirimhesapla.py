def indirim_hesapla():
    indsizTutar=float(input("İndirimsiz tutarı giriniz: "))
    indOrani=float(input("İndirim oranını giriniz (%): "))
    indMiktari=indsizTutar*(indOrani/100)
    print("İndirim miktarı:",indMiktari)
    print("İndirimli fiyat: ",indsizTutar-indMiktari)
indirim_hesapla()
