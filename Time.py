class Time:
    # parameters are in the normal range
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def getHour (self):
        return self.hour
    def getMinute(self):
        return self.minute
    def getSecond(self):
        return self.second

    # formats time object into a string hour:min:sec
    # return the field as a string
    def tostring (self):
        return str(self.hour)  + ":" + str(self.minute) + ":" + str(self.second)

    # converts the time into int seconds
    # returns an int
    def timeinseconds(self):
        return ((self.hour * 3600) + (self.minute * 60) + (self.second))

    # mutator method and changes current time with another
    # precondition: all parameters are within bounds
    def changethetime(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    # Time will be converted from 24 hour clock to 12 hour clock
    # returns a string
    def twelvehourclock(self):
        if self.hour > 12: # past noon
            t = Time(self.hour - 12, self.minute, self.second)
            return t.tostring() + "pm"
        else: # before or at noon
            return self.tostring() + "am"

    # based on time, retuns morning, evening, afternoon, or nighttime
    # returns time of day
    def whattimeisit(self):
        if self.hour >= 6 and self.hour < 12:  # hour is between 6 and 12
            return "morning"
        elif self.hour >= 12 and self.hour < 17:  # hour is between 12 and 17
            return "afternoon"
        elif self.hour >= 17 and self.hour < 22:  # hour is between 17 and 22
            return "evening"
        else:  # hour >= 22 or hour < 6  # hour is between 22 and 6
            return "nighttime"

    # compares two time objects based on seconds
    # returns difference of seconds
    def compareto(self, t):
        return self.timeinseconds() - t.timeinseconds()

    # t : represents a time in the future
    # returns a time object to show time till t
    def timetill(self, t):
        h = 0
        m = 0
        s = 0
        if self.hour < t.hour: # same day
            h = t.hour - self.hour
        else:  # different day
          h = t.hour + (24 - self.hour)
        if self.minute < t.minute:  # same hour
            m = t.minute - self.minute
        else:  # different hour
            m = t.minute + (60-self.minute)
        if self.second < t.second:  # same minute
            s = t.second - self.second
        else:  # different minute
            s = t.second + (60 - self.second)
        t1 = Time(h, m, s)
        return t1



