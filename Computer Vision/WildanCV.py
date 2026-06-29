import numpy as np
import matplotlib.pyplot as plt
import cv2

# Image Stitching Implementation
class Stitcher():

    def __init__(self, images):
        self.images = images
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.surf = cv2.xfeatures2d.SURF_create()


    def detectAndCompute(self, image, featureExtractor='SIFT'):
        """
        Untuk mendeteksi keypoint menggunakan Difference of Gaussian ==> detect
        Untuk menghitung descriptor yang akan dijadikan sebagai fitur suatu gambar ==> compute

        :param image: gambar RGB
        :param featureExtractor: ekstraksi fitur yang ingin dipilih, SIFT atau SURF
        :return: keypoint dan descriptor dari satu gambar
        """

        if featureExtractor is not 'SIFT':
            (keypoints, descriptor) = self.surf.detectAndCompute(image, None)
        else:
            (keypoints, descriptor) = self.sift.detectAndCompute(image, None)

        # konversi setiap point dari keypoint menjadi numpy array
        keypoint = np.array([kp.pt for kp in keypoints])

        return (keypoint, descriptor)

    def matchKeypoints(self, kpsLeft, kpsRight, featureLeft, featureRight):
        matcher = cv2.DescriptorMatcher_create('BruteForce')
        featureMatch = matcher.knnMatch(featureLeft, featureRight, 2)
        match = []

        for m in featureMatch:
            pass

    def homography(self):
        pass

    def stich(self):
        pass