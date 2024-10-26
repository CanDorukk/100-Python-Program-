#1 - Anagram Kontrolü

ilk_kelime = input("İlk Kelimenizi giriniz: ").lower()
ikinci_kelime = input("İkinci Kelimenizi giriniz: ").lower()


# List ile girilen kelimeyi harflere böleriz sonrasında sorted ile alfabetik sıralama uygularız.

x=list(sorted(ilk_kelime))
y=list(sorted(ikinci_kelime))


if x == y:
    print("Anagramdır.")
else:
    print("Anagram değildir.")

#2 - Rastgele Sayı Üretme

import random

print(f'Rastgele sayı: {random.randint(0,100)}')


#3 - İkili(binary) Arama algoritması

def ikili_arama(dizi, x):
    en_dusuk = 0
    en_yuksek= len(dizi) - 1
    while en_dusuk <= en_yuksek:
        ortanca = (en_dusuk + en_yuksek) // 2
        if dizi[ortanca] < x:
            en_dusuk = ortanca + 1
        elif dizi[ortanca] > x:
            en_yuksek= ortanca - 1
        else:
            return ortanca
    return -1

dizi = [2, 3, 4, 10, 40]
x = 10
sonuc = ikili_arama(dizi, x)
if sonuc != -1:
    print(f"Aranan eleman {sonuc}. indekste")
else:
    print("Aranan elaman bulunamadı.")


#4 - Çok Mükemmel Sayı Kontrolü


sum = 0
number = int(input("Bir Sayı Girin: "))

numb = []
while number != 0:
    digit = number % 10
    digit = digit**3
    numb.append(digit)
    sum+=digit
    number = number // 10
    
total = 0
for i in numb:
    total+=i

if sum == total:
    print(f'Girdiğiniz sayı Çok Mükemmel sayıdır.')
else:
    print(f'Girilen Sayı Çok Mükemmel sayı değildir.')
print("Rakamların Toplamı:", sum)
print(numb)


#5-  Basit örüntü oluşturma

n = 5
for i in range(n):
    print('* ' * (i + 1))

#6 - Doğrusal Arama Algoritması



def dogrusal_arama(liste,aranan):
    for i in range(len(liste)):
        if liste[i] == aranan:
            return i
        
    return -1
                

liste = [10, 23, 45, 70, 11, 15]
aranan = 70

sonuc = dogrusal_arama(liste,aranan)
if sonuc != -1:
    print(f'Aranan elemanın değerin indeksi {sonuc}')
else:
    print('Aranan eleman dizide bulunamadı')



#7 - Bir Sayının Kuvvetini Hesaplama


kuvveti_alinacak_Sayi = int(input("Kuvvetini almak istediğiniz sayıyı giriniz: "))
sayinin_kacinci_kuvveti = int(input("Kacinci kuvvetini almak istediğinizi giriniz: "))

islem = kuvveti_alinacak_Sayi**sayinin_kacinci_kuvveti
print(islem)



#8- Fibonacci serisini yazdırma


def fibonacci_serisi(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b


terim_sayisi = int(input("Kaç terim istiyorsunuz: "))
print("Serisi:")
fibonacci_serisi(terim_sayisi)


#9 - İki Listeyi Birleştirme ve Sıralama


liste_1 = [1, 3, 5, 7]
liste_2 = [2, 4, 6, 8]
birlestirilmis_liste = sorted(liste_1 + liste_2)
print("Birleştirilmiş ve Sıralanmış liste:", birlestirilmis_liste)


#10- Basit Bir Piramit Deseni Oluşturma


n = 5
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))