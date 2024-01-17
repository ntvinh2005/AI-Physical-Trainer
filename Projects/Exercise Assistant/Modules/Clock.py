import time

class Clock:
    def __init__(self):
        self.previous_time = time.time()
        self.resting_time = time.time() - self.previous_time
        self.stop_inform_moment = time.time()
        self.stop_confirm_time = time.time() - self.stop_inform_moment
    
    def check_resting_time(self):
        self.resting_time = time.time() - self.previous_time
        if self.resting_time >=5:
            return True
        else:
            return False

    def set_previous_time(self):
        self.previous_time = time.time()
    
    def check_confirm_stop(self, confirm_time_limit):
        self.stop_confirm_time = time.time() - self.stop_inform_moment
        if self.stop_confirm_time >= confirm_time_limit:
            return True
        else:
            return False
    
    def set_stop_moment(self):
        self.stop_inform_moment = time.time()
    