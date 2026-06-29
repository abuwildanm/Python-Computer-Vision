import cv2
import numpy as np
import pandas as pd
from sklearn.svm import SVC

def make_histogram(mag, angle):
    hist_of_grad = np.zeros(9)
    angle = angle % 180
    # print(mag)
    # print(angle)
    mag = mag.flatten()
    angle = angle.flatten()
    
    for m, a in zip(mag, angle):
        # print(m, np.absolute(a//20))
        hist_of_grad[int(np.absolute(a//20))] += m * (20-(a%20)) / 20
        hist_of_grad[int((a//20 + 1) % 9)] += m * (a%20) / 20
    
    return hist_of_grad


def normalize(block):
    block = block.flatten()
    vector_length = np.sqrt(np.sum(np.square(block)))
    block = block / vector_length
    
    return block


def block_normalization(hog_desc):
    # normalized_desc = [[0 for i in range(hog_desc.shape[1] - 1)] for j in range(hog_desc.shape[0] - 1)]
    normalized_desc = [[0 for i in range(7)] for j in range(15)]
    # print(len(normalized_desc), len(normalized_desc[0]))
    desc = np.array([])
    for i in range(len(normalized_desc)):
        for j in range(len(normalized_desc[0])):
            # print(i,i+2, j,j+2)
            desc = np.concatenate((desc, normalize(hog_desc[i:i+2, j:j+2])))
    
    # print(len(normalized_desc), len(normalized_desc[0]), len(normalized_desc[0][0]))
    # print(type(normalized_desc), type(normalized_desc[0]), type(normalized_desc[0][0]))
    # normalized_desc = np.array(normalized_desc)
    # print(desc.shape)
    return desc


def make_descriptor(mag, angle):
    # hog_desc = np.zeros((mag.shape[0] // 8, mag.shape[1] // 8))
    # print(hog_desc)
    hog_desc = [[0 for i in range(mag.shape[1] // 8)] for j in range(mag.shape[0] // 8)]
    # print(hog_desc)
    for i in range(len(hog_desc)):
        for j in range(len(hog_desc[0])):
            # print(i, j)
            m = mag[i*8 : (i+1)*8 , j*8 : (j+1)*8]
            a = angle[i*8 : (i+1)*8 , j*8 : (j+1)*8]
            hog_desc[i][j] = make_histogram(m, a)
            # print(type(make_histogram(m, a)))
    
    hog_desc = np.array(hog_desc)
    print('non normalized desc', hog_desc.shape)
    hog_desc = block_normalization(hog_desc)
    print('normalized desc', hog_desc.shape)
    # hog_desc = hog_desc.flatten()

    return hog_desc

# Read image
img1 = cv2.imread('../Dataset/train_person1.jpg')
img2 = cv2.imread('../Dataset/train_person2.jpg')
img3 = cv2.imread('../Dataset/train_person3.jpg')
img4 = cv2.imread('../Dataset/train_person4.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img)
img1 = np.float32(img1) / 255
img2 = np.float32(img2) / 255
img3 = np.float32(img3) / 255
img4 = np.float32(img4) / 255

# Calculate gradient
gx1 = cv2.Sobel(img1, cv2.CV_32F, 1, 0, ksize=1)
gx2 = cv2.Sobel(img2, cv2.CV_32F, 1, 0, ksize=1)
gx3 = cv2.Sobel(img3, cv2.CV_32F, 1, 0, ksize=1)
gx4 = cv2.Sobel(img4, cv2.CV_32F, 1, 0, ksize=1)
gy1 = cv2.Sobel(img1, cv2.CV_32F, 0, 1, ksize=1)
gy2 = cv2.Sobel(img2, cv2.CV_32F, 0, 1, ksize=1)
gy3 = cv2.Sobel(img3, cv2.CV_32F, 0, 1, ksize=1)
gy4 = cv2.Sobel(img4, cv2.CV_32F, 0, 1, ksize=1)

# Python Calculate gradient magnitude and direction ( in degrees )
mag1, angle1 = cv2.cartToPolar(gx1, gy1, angleInDegrees=True)
mag2, angle2 = cv2.cartToPolar(gx2, gy2, angleInDegrees=True)
mag3, angle3 = cv2.cartToPolar(gx3, gy3, angleInDegrees=True)
mag4, angle4 = cv2.cartToPolar(gx4, gy4, angleInDegrees=True)

# print(mag.shape, angle.shape)
# make_histogram(np.array([20, 30, 80, 40, 40]), np.array([0, 20, 55, 40, 165]))
# make_histogram(mag[0:8,0:8], angle[0:8,0:8])
# np.savetxt('desc.txt', make_descriptor(mag, angle))
desc1 = make_descriptor(mag1, angle1)
desc1 = np.append(desc1, 'person')
desc2 = make_descriptor(mag2, angle2)
desc2 = np.append(desc2, 'person')
desc3 = make_descriptor(mag3, angle3)
desc3 = np.append(desc3, 'person')
desc4 = make_descriptor(mag4, angle4)
desc4 = np.append(desc4, 'person')

desc = [desc1,desc2,desc3,desc4]

train = pd.DataFrame(data=desc)
x_train = train.iloc[:,:-1]
y_train = train.iloc[:,-1]

svc = SVC()
svc.fit(x_train,y_train)
y_pred = svc.predict(x_train)
acc_svc = round(svc.score(x_train, y_train) * 100, 2)
print(acc_svc)

# print(desc.shape)
# np.savetxt('scratch', desc)
# cv2.imshow('X', gx1)
# cv2.imshow('Y', gy1)
# cv2.waitKey(0)