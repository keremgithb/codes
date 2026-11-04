while (True):
    try:
        int(input("Bir sayı giriniz: "))
        break
    except ValueError:
        print("Lütfen geçerli bir sayı giriniz")
