import cv2
import numpy as np

#baca image
citra = cv2.imread('toystory.jpg')

#baca ukuran citra
jum_baris = len(citra[:])
jum_kolom = len(citra[0,:])

#tampilkan citra awal
cv2.imshow('citra awal', citra)

#-----PENSKALAAN-----
#inisialisasi faktor penskalaan
faktor_skala = 1.7      #faktor skala > 1: zoom in, faktor skala < 1: zoom out
#buat matrix zero untuk menampung gambar hasil translasi
jum_baris_baru = round(faktor_skala * jum_baris)
jum_kolom_baru = round(faktor_skala * jum_kolom)
citra_skala = np.zeros((jum_baris_baru, jum_kolom_baru, 3))      #angka 3 menyatakan 3 channel RGB
print(jum_kolom_baru)
print(jum_baris_baru)

#-----FLIPPING-----
#buat matrix zero untuk menampung gambar hasil flipping
citra_flipping = np.zeros((jum_baris, jum_kolom, 3))        #angka 3 menyatakan 3 channel RGB
#lakukan flipping
flip_horizontal = 1     #jika 1: lakukan flip horizontal, jika 0: tidak melakukan apa2
flip_vertikal = 0       #jika 1: lakukan flip vertikal, jika 0: tidak melakukan apa2

#-----TRANSLASI-----
#buat matrix zero untuk menampung gambar hasil translasi
citra_translasi = np.zeros((jum_baris, jum_kolom, 3))       #angka 3 menyatakan 3 channel RGB
#lakukan translasi
geser_horizontal = -30        #negatif berarti ke kiri, positif berarti ke kanan
geser_vertikal = 0         #negatif berarti ke atas, positif berarti ke bawah

#-----ROTASI-----
#buat matrix zero untuk menampung gambar hasil translasi
citra_rotasi = np.zeros((jum_baris, jum_kolom, 3))      #angka 3 menyatakan 3 channel RGB
#lakukan rotasi
sudut_rotasi = 50 
#konversi sudut_rotasi menjadi radian
sudut_radian = 3.14 * sudut_rotasi / 180


for brs in range(jum_baris):
    for klm in range(jum_kolom):

        # ---------- FLIPPING -----------
        #hitung posisi kolom yang baru jika flip_horizontal = 1
        if (flip_horizontal == 1):
            klm_baru = (jum_kolom - 1) - klm
        else:
            klm_baru = klm
        
        #hitung posisi baris yang baru jika flip_vertikal = 1
        if (flip_vertikal == 1):
            brs_baru = (jum_baris - 1) - brs
        else:
            brs_baru = brs

        #isi pixel pada citra_flipping dengan posisi baris dan kolom baru
        citra_flipping[brs_baru, klm_baru] = citra[brs, klm]

        # ---------- PENSKALAAN -----------
        #hitung baris baru dan kolom baru pada gamabr hasil penskalaan
        brs_baru = round(faktor_skala * brs)
        klm_baru = round(faktor_skala * klm)

        #isi pixel pada citra baru (citra skala)
        if (brs_baru < jum_baris_baru and klm_baru < jum_kolom_baru):
            citra_skala[brs_baru, klm_baru] = citra[brs, klm]

        # ---------- ROTASI -----------
        #hitung posisi baris dan kolom yang baru
        brs_baru = round(brs * np.cos(sudut_radian) - klm * np.sin(sudut_radian))
        klm_baru = round(brs * np.sin(sudut_radian) + klm * np.cos(sudut_radian))

        #isi pixel pada citra_rotasi dengan posisi baris dan kolom baru
        if (brs_baru < jum_baris and brs_baru >= 0):
            if (klm_baru < jum_kolom and klm_baru >= 0):
                citra_rotasi[brs, klm] = citra[brs_baru, klm_baru]

        # ---------- TRANSLASI ----------- 
        #hitung posisi baris dan kolom yang baru
        brs_baru = brs + geser_vertikal
        klm_baru = klm + geser_horizontal

        #isi pixel pada citra_translasi dengan posisi baris dan kolom baru
        if (brs_baru < jum_baris and brs_baru >= 0):
            if (klm_baru < jum_kolom and klm_baru >= 0):
                citra_translasi[brs_baru, klm_baru] = citra[brs, klm]

#konversi citra menjadi uint8
citra_flipping = citra_flipping.astype(np.uint8) #flipping
citra_skala = citra_skala.astype(np.uint8) #skala
citra_rotasi = citra_rotasi.astype(np.uint8) #rotasi
citra_translasi = citra_translasi.astype(np.uint8) #translasi

#tampilkan citra hasil : 
cv2.imshow("citra setelah pencerminan", citra_flipping) #flipping
cv2.waitKey()
cv2.imshow("citra setelah penskalaan", citra_skala) #penskalaan
cv2.waitKey()
cv2.imshow("citra setelah rotasi", citra_rotasi) #rotasi
cv2.waitKey()
cv2.imshow("citra setelah translasi", citra_translasi) #translasi
cv2.waitKey()

