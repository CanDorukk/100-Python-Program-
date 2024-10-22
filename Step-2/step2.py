# 1- Palindrome Kontrolü ("Yazılış olarak 'level' baz alırsak hem düz hem tersten okunuşu aynıdır bu kelimelere Palindrome denir.")

def palindrome(p):
    p = p.lower().replace(" ","")
    return p == p[::-1]



kelime = input("Kontrol edilecek kelimeyi giriniz: ")
if palindrome(kelime):
    print("Kelimeniz palindrome kelimedir.")
else:
    print("Kelimeniz palindrome kelime değildir.")



#2 - Üç Sayı Arasında En Büyüğünü Bulma


a = float(input("İlk Sayıyı Giriniz: "))
b = float(input("İkinci Sayıyı Giriniz: "))
c = float(input("Üçüncü Sayıyı Giriniz: "))

en_buyuk_sayi = max(a, b, c)
print("En büyük sayı:", en_buyuk_sayi)


#3 - Çarpım Tablosunu Yazdırma

sayi = int(input("Sayı Giriniz: "))
for i in range(1, 11):
    print(f"{sayi} x {i} = {sayi * i}")
    
#4 - Celsius'u Fahrenheit'e dönüştürme


celcius_input = int(input("Dereceyi(C*) giriniz"))
islem = ((celcius_input * 1.8) + 32)

print(f'Girdiğiniz Derecenin Fahrenheit değeri = {round(islem,1)}') 


#5 - Basit string işlemleri 

string_kelime = input("Kelimeyi giriniz: ")

print(f'İlk harfi büyütme {string_kelime.capitalize()}')
print(f'Bütün harfleri küçülme: {string_kelime.lower()}')
print(f'Kelime içindeki karakter sayısı: {len(string_kelime)}')
print(f'Kelimeyi ters çevirme: {string_kelime[::-1]}')

#6 - Buble Sıralama Algoritması

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print("Sıralanmış Dizi:", arr)

#7 - Artık yıl kontrolü 

year = int(input("Kontrol edilecek yılı giriniz: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Artık yıldır.")
else:
    print("Artık yıl değildir.")

#8 - String Ünlü Harfleri Sayma


tr_unlu_harfler = ['a','e','ı','i','o','ö','u','ü']


kelime = input("Kelimeyi giriniz: ").lower()

sayac = 0
for i in tr_unlu_harfler:
    print(i)
    for j in kelime:
        if i==j:
            sayac+=1
print(sayac)


#9 - İki sayının EBOB EKOK'unu bulma

def ebob_ekok(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if greater % x == 0 and greater % y == 0:
            lcm = greater
            break
        greater += 1
        return lcm
sayi1 = int(input("1. Sayıyı giriniz: "))
sayi2 = int(input("2. Sayıyı giriniz: "))
print("Sonuç:", ebob_ekok(sayi, sayi2))


#10 - Basit sınıf ve nesneler

class Rectangle:
    def __init__(self, uzunluk, genislik):
        self.uzunluk = uzunluk
        self.genislik = genislik
    def alan(self):
        return self.length * self.width
uzunluk = float(input("Enter length of the rectangle: "))
genislik = float(input("Enter width of the rectangle: "))
dikdortgen = Rectangle(uzunluk, genislik)
print("Area of the rectangle:", dikdortgen.alan())