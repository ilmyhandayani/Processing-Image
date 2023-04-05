import cv2
import numpy as np

#membaca citra digital dari komputer
citra = cv2.imread("chelsea.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra)
jum_kolom = len(citra[0])

#menyiapkan citra baru dengan nilai 0
citra_gray = np.zeros((jum_baris, jum_kolom))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_gray[i, j] = round(0.299 * r[i, j] + 0.587 * g[i, j] + 0.114 * b[i, j])

citra_gray = citra_gray.astype(np.uint8)

citra_negatif = np.zeros((jum_baris, jum_kolom))

cv2.imshow("chelsea gray", citra_gray)
print(citra_gray)

cv2.waitKey()