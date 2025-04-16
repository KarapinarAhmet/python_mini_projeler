print("Sayı Dönüştürücü Uygulamasına Hoş Geldiniz!")

sayi = int(input("Lütfen bir sayı giriniz: "))

print("\nDönüştürmek istediğiniz türü seçin:")
print("1. Binary (ikilik)")
print("2. Octal (sekizlik)")
print("3. Hexadecimal (onaltılık)")

secim = input("Seçiminiz: ")

if secim == "1":
    print("Binary karşılığı:", bin(sayi)[2:])
elif secim == "2":
    print("Octal karşılığı:", oct(sayi)[2:])
elif secim == "3":
    print("Hexadecimal karşılığı:", hex(sayi)[2:])
else:
    print("Geçersiz seçim.")
