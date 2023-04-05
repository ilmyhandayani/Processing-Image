import cv2
import numpy as np

#membaca citra digital dari komputer
citra1 = cv2.imread("chelsea.jpg")
citra2 = cv2.imread("chelsea-red.jpg")

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
citra_multiplication = np.zeros((jum_baris, jum_kolom, 3))

#menghitung nilai pixel grayscale
for i in range(jum_baris):
    for j in range(jum_kolom):
        citra_multiplication[i, j, 0] = int(b1[i, j]) * int(b2[i, j])
        citra_multiplication[i, j, 1] = int(g1[i, j]) * int(g2[i, j])
        citra_multiplication[i, j, 2] = int(r1[i, j]) * int(r2[i, j])

        # revisi nilai pixel jika > 255
        if (citra_multiplication[i, j, 0] > 255): 
            citra_multiplication[i, j, 0] = 255
        
        if (citra_multiplication[i, j, 1] > 255): 
            citra_multiplication[i, j, 1] = 255

        if (citra_multiplication[i, j, 2] > 255): 
            citra_multiplication[i, j, 2] = 255

citra_multiplication = citra_multiplication.astype(np.uint8)

cv2.imshow("chelsea-rgb", citra1)
cv2.imshow("abstract", citra2)
cv2.imshow("multiplication", citra_multiplication)

cv2.waitKey()