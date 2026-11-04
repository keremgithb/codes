import random
sayi=random.randint(1,100)
tahmin=0
deneme=0
while (True):
    try:
        tahmin=int(input("Bir sayı giriniz (1-100):"))
        if tahmin<0 or tahmin>100:
            print("Lütfen geçerli bir değer giriniz!")
            continue
        deneme+=1
    except:
        print("Lütfen geçerli bir değer giriniz!")
        continue
    if tahmin==sayi:
        print(f"Doğru sayıyı buldunuz. Toplam deneme sayınız: {deneme}")
        break
    elif tahmin<sayi:
        print("Daha büyük bir sayı giriniz!")
    else:
        print("Daha küçük bir sayı giriniz!")
