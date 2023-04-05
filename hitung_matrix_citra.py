import cv2

#membaca citra digital dari komputer
citra = cv2.imread("chelsea.jpg")

#menampilkan citra digital yang sudah dibaca
cv2.imshow("chelsea - blue", citra[:,:,0])
cv2.imshow("chelsea - green", citra[:,:,1])
cv2.imshow("chelsea - red", citra[:,:,2])

#menampilkan matriks dari citra
print(citra)        #print semua channel warna
print(citra[:,:,0]) #print channel warna biru
print(citra[:,:,1]) #print channel warna hijau
print(citra[:,:,2]) #print channel warna merah

#menunggu sampai user menekan sembarang tombol
cv2.waitKey()