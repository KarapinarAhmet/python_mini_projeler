import sys

# Roman rakamı dönüşümü
def to_roman(num):
    roman_dict = {
        1: "I", 4: "IV", 5: "V", 9: "IX",
        10: "X", 40: "XL", 50: "L", 90: "XC",
        100: "C", 400: "CD", 500: "D", 900: "CM",
        1000: "M"
    }
    roman = ''
    for value in sorted(roman_dict.keys(), reverse=True):
        while num >= value:
            roman += roman_dict[value]
            num -= value
    return roman

# Sayı dönüştürme fonksiyonu
def sayi_donustur(sayi, secim):
    if secim == "1":
        return bin(sayi)[2:]
    elif secim == "2":
        return oct(sayi)[2:]
    elif secim == "3":
        return hex(sayi)[2:]
    elif secim == "4":
        return to_roman(sayi)
    else:
        return "Geçersiz seçim"

# Ana fonksiyon
def main():
    print("Sayı Dönüştürücü Uygulamasına Hoş Geldiniz!")
    
    while True:
        try:
            sayi = int(input("\nBir sayı girin: "))
        except ValueError:
            print("Lütfen geçerli bir sayı girin.")
            continue
        
        print("\nDönüşüm Seçenekleri:")
        print("1. Binary")
        print("2. Octal")
        print("3. Hexadecimal")
        print("4. Roman Rakamları")
        print("0. Çıkış")
        
        secim = input("Seçiminiz (0-4): ")
        
        if secim == "0":
            print("Çıkılıyor... Görüşmek üzere!")
            sys.exit()
        
        sonuc = sayi_donustur(sayi, secim)
        print(f"\nSonuç: {sonuc}")

        with open("donusum_gecmisi.txt", "a") as dosya:
            dosya.write(f"Sayı: {sayi}, Dönüşüm Sonucu: {sonuc}\n")

if __name__ == "__main__":
    main()
