# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_fahrenheit(0))    # Output: 32.0
# print(celcius_ke_fahrenheit(100))  # Output: 212.0

print('---- mencari celcius ke fahrenheit ----')
def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit (0))
print(celcius_ke_fahrenheit (100))

#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.

print('\n---- mencari bilangan genap ----')
def is_genap(bil_genap):
    return bil_genap %2 == 0
# Untuk memasukan value
print(is_genap(4))
print(is_genap(7))

# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal

# rata" nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
        return 'Lulus'
    else :
        return 'Gagal'
    
# untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))


#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
bilangan(20) # 1,3,5,7,9,11,13,15,17,19

print('\n---- Cetak Bilngan Ganjil ---- ')
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i, end=" ")
# untuk memasukan value
bil_ganjil(20)        