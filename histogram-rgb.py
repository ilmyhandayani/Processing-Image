import cv2
import matplotlib.pyplot as plt
import numpy as np

#inisialisasi direktori penyimpanan image
image_dir = 'toystory.jpg'

#membaca data image
image = cv2.imread(image_dir)

#memisahkan matriks B, G, dan R (openCV menggunakan model BGR, bukan RGB)
B, G, R = cv2.split(image)

#hitung tinggi dan lebar image
height = len(image)
width = len(image[0])
tot_pixel = height * width

#hitung kemunculan tiap nilai pixel pada matrix B, G, dan R
hist_B = np.zeros((256))    #buat histogram untuk B
hist_G = np.zeros((256))    #buat histogram untuk G
hist_R = np.zeros((256))    #buat histogram untuk R
for i in range(height):
    for j in range(width):
        #proses matrix B
        pixel = B[i][j]
        hist_B[pixel] += 1

        #proses matrix G
        pixel = G[i][j]
        hist_G[pixel] += 1

        #proses matrix R
        pixel = R[i][j]
        hist_R[pixel] += 1

#tampilkan histogram
plt.bar(range(len(hist_R)), hist_R, color=[1,0,0])
plt.bar(range(len(hist_G)), hist_G, color=[0,1,0])
plt.bar(range(len(hist_B)), hist_B, color=[0,0,1])

#tutup histogram ketika user menekan sembarang tombol
plt.waitforbuttonpress()



