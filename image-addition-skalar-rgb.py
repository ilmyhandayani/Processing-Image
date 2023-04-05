import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("chelsea.jpg")

#membaca channel warna BGR dan menyimpannya ke dalam variabel terpisah
b = citra1[:,:,0]
g = citra1[:,:,1]
r = citra1[:,:,2]

#menyimpan jumlah baris dan jumlah kolom dari citra
jum_baris = len(citra1)
jum_kolom = len(citra1[0])

#menyiapkan citra baru dengan nilai 0
citra_addition = np.zeros((jum_baris, jum_kolom, 3))
add_value = 50

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_addition[i, j, 0] = b[i, j] + add_value
        citra_addition[i, j, 1] = g[i, j] + add_value
        citra_addition[i, j, 2] = r[i, j] + add_value

        # revisi nilai pixel jika > 255
        if (citra_addition[i, j, 0] > 255): 
            citra_addition[i, j, 0] = 255
        
        if (citra_addition[i, j, 1] > 255): 
            citra_addition[i, j, 1] = 255

        if (citra_addition[i, j, 2] > 255): 
            citra_addition[i, j, 2] = 255

citra_addition = citra_addition.astype(np.uint8)

cv2.imshow("chelsea-rgb", citra1)
cv2.imshow("addition", citra_addition)

cv2.waitKey()