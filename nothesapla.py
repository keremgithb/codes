def harf_notu_hesapla():
    vize=int(input("Vize notunuzu giriniz: "))
    final=int(input("Final notunuzu giriniz: "))
    ortalama=vize*40/100+final*60/100
    print(f"Ortalamanız:{ortalama}.")
    if ortalama >= 90:
        print("Harf Notunuz: AA")
    elif ortalama >= 80:
        print("Harf Notunuz: BA")
    elif ortalama >= 70:
        print("Harf Notunuz: BB")
    elif ortalama >= 60:
        print("Harf Notunuz: CB")
    elif ortalama >= 50:
        print("Harf Notunuz: CC")
    elif ortalama >= 40:
        print("Harf Notunuz: DC")
    elif ortalama >= 30:
        print("Harf Notunuz: DD")
    elif ortalama >= 20:
        print("Harf Notunuz: FD")
    else:
        print("Harf Notunuz: FF")
harf_notu_hesapla()