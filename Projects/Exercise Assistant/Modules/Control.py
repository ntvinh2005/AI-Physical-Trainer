class Control:
    def __init__(self):
        self.stopped = False
        self.stop_informed = False
        self.stop_inform_moment = 0
        self.stop_confirm_time = 0
    
    def detect_stop_gesture(self, brain, left_wrist, right_wrist, left_elbow, right_elbow):
        clock = brain.clock
        speaker = brain.speaker
        #body part [1] is horozontal index, body part[2] is vertical index 
        #detect stop hand gesture
        if (left_wrist[1] - right_wrist[1])*(left_elbow[1] - right_elbow[1]) < 0 and (left_wrist[2] - left_elbow[2])*(right_wrist[2] - right_elbow[2]) > 0 :
            if self.stop_informed == False:
                clock.set_stop_moment()
            self.stop_informed = True
        else:
            clock.set_stop_moment()
        if self.stop_informed == True and clock.check_confirm_stop(3):
            speaker.speak("Ok I will stop counting")
            self.stopped = True
            self.stop_informed = False
        return (self.stopped)

    def detect_continue_gesture(self, brain, left_wrist, right_wrist, left_elbow, right_elbow):
        #body part [1] is horozontal index, body part[2] is vertical index 
        #detect continue hand gesture
        clock = brain.clock
        speaker = brain.speaker
        if (left_wrist[1] - left_elbow[1])*(right_wrist[1] - right_elbow[1]) < 0 and (left_wrist[2] - right_wrist[2])*(left_elbow[2] - right_elbow[2]) > 0 :
            if self.stop_informed == False:
                clock.set_stop_moment()
            self.stop_informed = True
        else:
            clock.set_stop_moment()
        if self.stop_informed == True and clock.check_confirm_stop(5):
            speaker.speak("Ok I will continue counting")
            self.stopped = False
            self.stop_informed = False
        return (self.stopped)