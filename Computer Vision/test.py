import numpy as np
import cv2

imgLeft = cv2.imread('../Dataset/rektorat1.jpg')
imgRight = cv2.imread('../Dataset/rektorat2.jpg')

# Feature Extraction
sift = cv2.xfeatures2d.SIFT_create()
(kpsLeft, featureLeft) = sift.detectAndCompute(imgLeft, None)
kpsLeft = np.array([kp.pt for kp in kpsLeft])
(kpsRight, featureRight) = sift.detectAndCompute(imgRight, None)
kpsRight = np.array([kp.pt for kp in kpsRight])
print(len(featureRight))

# Feature Matching
matcher = cv2.DescriptorMatcher_create('BruteForce')
rawMatches = matcher.knnMatch(featureLeft, featureRight, 2)
print(rawMatches[0])


# cv2.imshow('Rektorat', imgLeft)
# cv2.waitKey(0)