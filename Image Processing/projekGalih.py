# import opencv
import cv2

# import numpy tapi namanya diubah pemanggiannya menjadi np, numpy itu biasanya dipakai untuk operasi" yang berbentuk
# array, image kan pixel ada width dan height nah itu jadi sebuah array nantinya, jadi butuh numpy untuk operasinya
# kalau dalam program ini numpy dibuat untuk membuat kernel atau masking
import numpy as np

# import skimage
import skimage

# memanggil image
img = cv2.imread("Dataset/pool.png")
resize = cv2.resize(img, (480,480), fx=0.5, fy=0.5)
cv2.imshow("Original Image",resize)


# convert RGB ke Grayscale
img_gray = cv2.cvtColor(resize,cv2.COLOR_RGB2GRAY)
height, width = img_gray.shape

# proses invers
for y in range(height):
    for x in range(width):
        img_gray[y][x] = 255 - img_gray[y][x] # invers

# menampilkan hasil
cv2.imshow("Grayscale",img_gray)

#gaussian filtering
noise_removal = cv2.GaussianBlur(img_gray, (7, 7), 0)

# menampilkan hasil
cv2.imshow("Noise Removal",noise_removal)

# metode Histogram Equalization
equal_histogram = cv2.equalizeHist(noise_removal)
cv2.imshow("Histogram Equalization",equal_histogram)

# membuat kernel ukuran 7 x 7
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(15,15))

# metode Morfology
morph_image = cv2.morphologyEx(equal_histogram,cv2.MORPH_OPEN,kernel,iterations=15)
cv2.imshow("Morfologi Opening",morph_image)

# metode subtraction
#sub_morp_image = cv2.subtract(equal_histogram,morph_image)
sub_morp_image = equal_histogram - morph_image
cv2.imshow("Subtraction", sub_morp_image)

# metode thresholding dengan menggunakan OTSU
ret,thresh_image = cv2.threshold(sub_morp_image,0,255,cv2.THRESH_OTSU)
cv2.imshow("Thresholding",thresh_image)

# metode detksi tepi  dengan Canny
canny_image = cv2.Canny(thresh_image,250,255)
cv2.imshow("Edge Detection",canny_image)

# membuat kernel ukuran 3 x 3
kernel = np.ones((3,3), np.uint8)

# metode dilasi
dilated_image = cv2.dilate(canny_image,kernel,iterations=1)
cv2.imshow("Dilation", dilated_image)

# baris 63 - 77 membuat kotak
new,contours, hierarchy = cv2.findContours(dilated_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours= sorted(contours, key = cv2.contourArea, reverse = True)[:10]
screenCnt = None
for c in contours:
 peri = cv2.arcLength(c, True)
 approx = cv2.approxPolyDP(c, 0.09 * peri, True)  # Approximating with 9% error
 if len(approx) == 4:
  screenCnt = approx
  break
final = cv2.drawContours(resize, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Contour",final)
mask = np.zeros(img_gray.shape,np.uint8)
new_image = cv2.drawContours(mask,[screenCnt],0,255,-1,)
new_image = cv2.bitwise_and(resize,resize,mask=mask)
cv2.imshow("Final Image",new_image)

# waktu tunggu hasil, jika dikasi 0 nanti program tidak akan langsung ke close, dia baru close ketika ditekan stop
cv2.waitKey(0)

# memhapus semua data semacam cache tp bukan cache
cv2.destroyAllWindows()

# NB : Kalau ketemu nama cv2.blablabla, blablabla itu fungsi pada opencv