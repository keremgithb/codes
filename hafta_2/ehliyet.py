dy=int(input("Doğum yılınızı giriniz: "))
yas=2026-dy
if yas>=18:
    print(f"Yaşınız:{yas}. Ehliyet alabilirsiniz.")
else:
    print(f"Yaşınız:{yas}. Ehliyet alabilmek için {18-yas} yıl beklemeniz lazım.")
