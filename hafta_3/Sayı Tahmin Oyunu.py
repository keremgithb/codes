import random
sayi=random.randint(1,100)
tahmin=0
deneme=0
while (True):
    try:
        deneme+=1
        tahmin=int(input("Bir sayı giriniz (1-100):"))
    except:
        print("Lütfen geçerli bir değer giriniz!")
    if tahmin==sayi:
        print(f"Doğru sayıyı buldunuz. Toplam deneme sayınız: {deneme}")
        break
    elif tahmin<sayi:
        print("Daha büyük bir sayı giriniz!")
    else:
        print("Daha küçük bir sayı giriniz!")
