class Count:
    def __init__(self, isOn = False, current_counting = 0):
        self.isOn = isOn
        self.current_counting = current_counting
    
    def countCurl(self, angle, brain, max_amplitude = 180):
        speaker = brain.speaker
        clock = brain.clock
        if self.isOn == False:
            if max_amplitude - angle > 160:
                self.current_counting += 0.5
                self.isOn = True
        if self.isOn == True:
            if max_amplitude - angle < 20:
                self.current_counting += 0.5
                clock.set_previous_time()
                speaker.set_speed(speed = 250)
                speaker.speak(str(int(self.current_counting)))
                brain.reminded = False
                brain.motivated = False
                self.isOn = False