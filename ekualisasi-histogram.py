import cv2
import matplotlib.pyplot as plt
import numpy as np

#inisialisasi direktori penyimpanan image
image_dir = 'toystory.jpg'

#membaca data image
image = cv2.imread(image_dir)

#mengkonversi citra RGB menjadi citra grayscale dengan openCV
img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("gambar sebelum ekualisasi", img_gray)

#hitung tinggi dan lebar image
height = len(image)
width = len(image[0])
tot_pixel = height * width

#hitung kemunculan tiap nilai warna
hist_gray = np.zeros((256))    #buat histogram untuk grayscale
for i in range(height):
    for j in range(width):
        #proses matrix
        pixel = img_gray[i][j]
        hist_gray[pixel] += 1 / tot_pixel   #dinormalisasi

#tampilkan histogram sebelum ekualisasi
plt.bar(range(len(hist_gray)), hist_gray, color=[0,0,1])

#ekualisasi histogram
new_pixel = np.zeros((256))     #buat histogram untuk hasil ekualisasi
temp_sum = 0
for i in range(256):
    temp_sum += hist_gray[i]
    new_pixel[i] = round(255 * temp_sum)

#konversi float pada array numpy menjadi integer
new_pixel = new_pixel.astype(int)

#update citra dan hitung kemunculan tiap warna
hist_gray_eq = np.zeros((256))    #buat histogram ekualisasi baru
img_gray_eq = np.zeros((height, width)) #buat citra baru hasil ekualisasi
for i in range(height):
    for j in range(width):
        #ganti pixel lama ke new_pixel hasil ekualisasi
        pixel = img_gray[i][j]
        pixel = new_pixel[pixel]
        #print(pixel)
        img_gray_eq[i][j] = pixel

        #hitung kemunculan pixel
        hist_gray[pixel] += 1 / tot_pixel   #dinormalisasi

#tampilkan histogram setelah ekualisasi
#plt.bar(range(len(hist_gray)), hist_gray, color=[0,0,1])

#tampilkan gambar hasil ekualisasi
img_gray_eq = img_gray_eq.astype(np.uint8)      #konversi int ke uint8
cv2.imshow("gambar hasil ekualisasi", img_gray_eq)

#tutup histogram ketika user menekan sembarang tombol
plt.waitforbuttonpress()