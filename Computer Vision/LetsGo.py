import numpy as np
import cv2

class Stitcher:
    def __init__(self, images):
        self.images = images
        
        # convert to grayscale
        left_gray = cv2.cvtColor(self.images[0], cv2.COLOR_BGR2GRAY)
        right_gray = cv2.cvtColor(self.images[1], cv2.COLOR_BGR2GRAY)
        self.gray = (left_gray, right_gray)

    def detect_features(self):
        sift = cv2.xfeatures2d.SIFT_create()
        
        # SIFT keypoints and descriptors
        left_kps, left_des = sift.detectAndCompute(self.gray[0], None)
        right_kps, right_des = sift.detectAndCompute(self.gray[1], None)
        
        return ((left_kps, left_des), (right_kps, right_des))
    
    def match_keypoints(self, sift_features, ratio):
        matcher = cv2.DescriptorMatcher_create("BruteForce")
        # take best 2 matches for each features
        all_matches = matcher.knnMatch(sift_features[0][1], sift_features[1][1], 2)
        
        matches = []
        for match in all_matches:
            # distance from both best match features should be lower than given ratio
            if match[0].distance < match[1].distance * ratio:
                # save index of matching features
                matches.append(match[0])

        # draw match keypoints
        self.show_matches(matches, sift_features[0][0], sift_features[1][0])

        # construct the two sets of points
        match_points = np.array([(sift_features[1][0][match.trainIdx].pt, sift_features[0][0][match.queryIdx].pt) for match in matches])
        left_points = match_points[:,0]
        right_points = match_points[:,1]

        # ptsA = np.float32([kpsA[i] for (_, i) in matches])
        # ptsB = np.float32([kpsB[i] for (i, _) in matches])

        # find homography between points in both image
        if len(matches) >= 4:
            (H, status) = cv2.findHomography(left_points, right_points, cv2.RANSAC)
            print(H)
        else:
            raise AssertionError('Can’t find enough keypoints.')
        return (matches, H)

    def show_matches(self, matches, left_kps, right_kps):
        # get best matching feature
        matches.sort(key=lambda x: x.distance, reverse=False)
        matches = matches[:int(len(matches) * 0.5)]

        # Draw top matches
        vis_matches = cv2.drawMatches(self.images[0], left_kps, self.images[1], right_kps, matches, None)
        
        cv2.imshow("matches.jpg", vis_matches)

    def stitch(self):
        sift_features = self.detect_features()
        matches, H = self.match_keypoints(sift_features, 0.75)
        
        stitched = cv2.warpPerspective(self.images[1], H, (self.images[1].shape[1] + self.images[0].shape[1], self.images[0].shape[0]))
        cv2.imshow('result', stitched)
        cv2.waitKey(0)
        stitched[0:self.images[0].shape[0], 0:self.images[0].shape[1]] = self.images[0]

        return stitched


left_img = cv2.imread('../Dataset/rektorat1.jpg')
right_img = cv2.imread('../Dataset/rektorat2.jpg')

width, height = left_img.shape[1]/3, left_img.shape[0]/3
left_img = cv2.resize(left_img, (int(width), int(height)))
right_img = cv2.resize(right_img, (int(width), int(height)))

# cv2.imshow('right', right_img)
# cv2.waitKey(0)

stitcher = Stitcher([left_img, right_img])
result = stitcher.stitch()
cv2.imshow('Panorama', result)
cv2.waitKey(0)