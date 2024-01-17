from Modules.PoseTrackingMin import PoseDetector 
from Modules.HandTrackingMin import HandDetector
from Modules.Brain import Brain
import cv2
import time


def main():
    cap = cv2.VideoCapture(0)
    previousTime = 0
    poseDetector = PoseDetector()
    handDetector = HandDetector()
    brain = Brain()

    while True:
        success, img = cap.read()
        img = poseDetector.findPose(img)
        img = handDetector.findHand(img)
        landmarkList = poseDetector.findPosition(img)

        if landmarkList:
            brain.update(landmarkList, img)

        currentTime = time.time()
        fps = 1/(currentTime - previousTime)
        previousTime = currentTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        

if __name__ == "__main__":
    main()
    