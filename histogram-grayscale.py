import cv2
import numpy as np
import matplotlib.pyplot as plt

#inisialisasi direktori penyimpanan image
image_dir = 'toystory.jpg'

#membaca data image
citra = cv2.imread(image_dir)

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])
tot_pixel = jum_baris * jum_kolom

#menyiapkan citra baru dengan nilai 0
citra_gray = np.zeros((jum_baris, jum_kolom))

#menghitung nilai pixel grayscale
hist_gray = np.zeros((256))    #buat histogram
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_gray[i, j] = round(0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j])

        # hitung kemunculan pixel
        pixel = int(citra_gray[i,j])
        hist_gray[pixel] += 1 / tot_pixel

citra_gray = citra_gray.astype(np.uint8)

#########################################

#ekualisasi histogram
new_pixel = np.zeros((256))     #buat histogram untuk hasil ekualisasi
sum_p = 0
for i in range(256):
    sum_p += hist_gray[i]
    new_pixel[i] = round(255 * sum_p)

#konversi float pada array numpy menjadi integer
new_pixel = new_pixel.astype(np.uint8)

#update citra dan hitung kemunculan tiap warna
hist_gray_eq = np.zeros((256))    #buat histogram ekualisasi baru
citra_gray_eq = np.zeros((jum_baris, jum_kolom)) #buat citra baru hasil ekualisasi
for i in range(jum_baris):
    for j in range(jum_kolom):
        #ganti pixel lama ke new_pixel hasil ekualisasi
        pixel = citra_gray[i][j]    #baca pixel yg lama
        pixel = new_pixel[pixel]    #isi dengan pixel baru

        # mengisi pixel baru ke dalam citra baris ke-i, kolom ke-j        
        citra_gray_eq[i, j] = pixel 

        #hitung kemunculan pixel
        hist_gray_eq[pixel] += 1 / tot_pixel   #dinormalisasi

citra_gray_eq = citra_gray_eq.astype(np.uint8)

cv2.imshow("grayscale awal", citra_gray)
cv2.imshow("grayscale eq", citra_gray_eq)            

#tampilkan histogram
plt.bar(range(256), hist_gray)
plt.bar(range(256), hist_gray_eq)

#tutup histogram ketika user menekan sembarang tombol
plt.waitforbuttonpress()

#pakai library cv2
#hist = cv2.calcHist([img_gray], [0], None, [256], [0,256])
#plt.plot(hist)

