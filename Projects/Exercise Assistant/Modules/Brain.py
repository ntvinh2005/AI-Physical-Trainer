import cv2
import random
from .Clock import Clock
from .Count import Count
from .Speaker import Speaker
from .Control import Control
import numpy as np

class Brain():
    def __init__(self):
        self.count = Count()
        self.speaker = Speaker()
        self.clock = Clock()
        self.reminded = True
        self.motivated = True
        self.control = Control()
        self.isStop = False
    
    def motivate(self):
        congratulation_content = ""
        motivating_array = [
            [
            "One more rep! Push",
            "Don't rest until you finish the set",
            "Try harder!"
            ],[
            "Good job!",
            "You have great form",
            "You are the greatest",
            "You have come a long way"
            ]]
        if self.count.current_counting >= 5:
            congratulation_content = random.choice(motivating_array[1])
        
        content = "Already got " + str(int(self.count.current_counting)) + " shot. " + congratulation_content + random.choice(motivating_array[0]) 
        print(content)
        self.speaker.set_speed(speed = 150)
        self.speaker.speak(content)
    
    def remind(self):
        if self.clock.check_resting_time() == True and self.reminded == False:
            self.motivate()
            self.reminded = True
    
    def update(self, landmarkList, img):
        left_shoulder = landmarkList[11]
        right_shoulder = landmarkList[12]
        left_elbow = landmarkList[13]
        right_elbow = landmarkList[14]
        left_wrist = landmarkList[15]
        right_wrist = landmarkList[16]
        left_angle = int(angleMeasure(left_elbow, left_shoulder, left_wrist))
        right_angle = int(angleMeasure(right_elbow, right_shoulder, right_wrist))
        cv2.putText(img, str(left_angle), (left_elbow[1], left_elbow[2]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 4)
        cv2.putText(img, str(right_angle), (right_elbow[1], right_elbow[2]), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 4)

        if self.isStop == False:
            self.isStop = self.control.detect_stop_gesture(self,left_wrist, right_wrist, left_elbow, right_elbow)
            self.count.countCurl(left_angle, self)
            self.remind()
        else:
            self.isStop = self.control.detect_continue_gesture(self, left_wrist, right_wrist, left_elbow, right_elbow)
        
        cv2.putText(img, str(int(self.count.current_counting)), (250, 70), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 4)

def angleMeasure(A, B, C):
    A, B, C = np.array(A), np.array(B), np.array(C)
    vector_AB = B - A
    vector_AC = C - A

    dot_product_AB_AC = np.dot(vector_AB, vector_AC)
    magnitude_AB = np.linalg.norm(vector_AB)
    magnitude_AC = np.linalg.norm(vector_AC)

    if magnitude_AB == 0 or magnitude_AC == 0:
        return 0

    angle_radians = np.arccos(dot_product_AB_AC / (magnitude_AB * magnitude_AC))
    angle = np.degrees(angle_radians)

    return angle
