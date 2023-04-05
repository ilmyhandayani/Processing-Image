import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("highway-empty.jpg")
citra2 = cv2.imread("highway-1car.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b1 = citra1[:,:,0]
g1 = citra1[:,:,1]
r1 = citra1[:,:,2]

b2 = citra2[:,:,0]
g2 = citra2[:,:,1]
r2 = citra2[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_gray1 = np.zeros((jum_baris, jum_kolom))
citra_gray2 = np.zeros((jum_baris, jum_kolom))
citra_subtraction = np.zeros((jum_baris, jum_kolom))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        # Konversi citra RGB ke grayscale
        citra_gray1[i, j] = round(0.299 * r1[i, j] + 0.587 * g1[i, j] + 0.114 * b1[i, j])
        citra_gray2[i, j] = round(0.299 * r2[i, j] + 0.587 * g2[i, j] + 0.114 * b2[i, j])

        citra_subtraction[i, j] = citra_gray1[i, j] - citra_gray2[i, j]

        # Thresholding agar citra menjadi hitam putih (biner)
        if (citra_subtraction[i, j] < 50):
            citra_subtraction[i, j] = 0
        else:
            citra_subtraction[i, j] = 255

citra_gray1 = citra_gray1.astype(np.uint8)
citra_gray2 = citra_gray2.astype(np.uint8)
citra_subtraction = citra_subtraction.astype(np.uint8)

cv2.imshow("empty car", citra_gray1)
cv2.imshow("1 car", citra_gray2)
cv2.imshow("subtract", citra_subtraction)

print(citra_gray1)
print(citra_gray2)
print(citra_subtraction)

cv2.waitKey()