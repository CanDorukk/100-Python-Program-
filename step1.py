# Step-1 


# 1 - Hello world program

print("Hellow World")

# 2 - Simple Calculator

sayi1 = int(input("1. Sayıyı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))

print(f'Toplama: {sayi1+sayi2}')
print(f'Çıkarma: {sayi1-sayi2}')
print(f'Çarpma: {sayi1*sayi2}')
print(f'Bölme: {sayi1/sayi2}')


# 3 - Bir sayının faktöriyeli

factoriel = int(input("Faktöryelini istediğiniz sayıyı giriniz: "))

if factoriel == 0:
    factoriel =1
elif factoriel<0:
    print("Negatif sayıların faktöriyeli yoktur.")
    
sonuc = 1
for i in range(1,factoriel+1):
    sonuc = sonuc*i 
    

print(sonuc)



# 4 - Fibonacci Sıralaması


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
terms = int(input("Şartınızı giriniz: "))
print("Fibonacci sıralaması:")
for i in range(terms):
    print(fibonacci(i))


# 5 -  Asal sayı kontrolü




asal_Sayi = int(input("Kontrol edeceğiniz sayıyı giriniz: "))

for i in range(2,asal_Sayi):
    if asal_Sayi%i==0:
        print("Sayınız asal değildir.")
        break
else:
    print(f'Sayınız asaldır {asal_Sayi}')
    




# 6 - Tek mi çift mi

tc_sayisi = int(input("Kontrol etmek istediğiniz sayıyı giriniz: "))


if tc_sayisi%2 == 0:
    print(f'Girilen sayı {tc_sayisi} çifttir.')
else:
    print(f'Girilen sayı {tc_sayisi} tektir.')




# 7 - Dairenin alanı

pi = 3.14

daire_yaricap = int(input("Yarıçap değeri giriniz: "))

alan = (pi*(daire_yaricap**2))

print(alan)

# 9 - Liste Anlama

squares = [i ** 2 for i in range(10)]
print("Squares:", squares)

# 10 - Basit Dosya İşleme


f = open('step1.txt',"a")
f.write("Buraya kadar geldiğiniz için teşekkür ederim diğer aşamaları görmek için bu repoyu takip edebilirsiniz. ")
f.close()

f = open('step1.txt',"r")
print(f.read())