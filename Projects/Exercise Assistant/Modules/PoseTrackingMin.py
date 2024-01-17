import cv2
import mediapipe as mp
import time

class PoseDetector():
    def __init__(self, static_image_mode=False, smooth_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode = static_image_mode
        self.smooth_landmarks = smooth_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            static_image_mode=self.static_image_mode,
            smooth_landmarks=self.smooth_landmarks,
            min_detection_confidence=self.min_detection_confidence,
            min_tracking_confidence=self.min_tracking_confidence
        )
        self.mpDraw = mp.solutions.drawing_utils
    
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        
        return img

    def findPosition(self, img, draw = True):
        landmarkList = []
        if self.results.pose_landmarks:
            for id, landmark in enumerate(self.results.pose_landmarks.landmark):
                height, weight, channels = img.shape
                cx, cy = int(landmark.x * weight), int(landmark.y * height)
                landmarkList.append([id, cx, cy])
                #if draw:
                #    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        return landmarkList