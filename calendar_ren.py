"""renpy
init -99 python:
"""

class Calendar(object):
    def __init__(self, Hours, Minutes, Month, Days, Day, Year):
        self.Hours = Hours
        self.Months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        self.Month = (Month - 1)
        self.Days = Days
        self.Day = Day
        self.Year = Year
        self.Minutes = Minutes
        self.Weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        if(self.Year % 4 == 0 and self.Year % 100 != 0) or self.Year % 400 == 0:
            self.MonthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @property
    def set_MonthDays(self):
        if(self.Year % 4 == 0 and self.Year % 100 != 0) or self.Year % 400 == 0:
            self.MonthDays = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.MonthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    @property
    def check_time(self):
        return self.Hours

    @property
    def Output(self):
        return self.Weekdays[self.Day] + " " + self.Months[self.Month] + " " + str(self.Days) + ", " + str (self.Year) + " " + str(self.Hours).zfill(2) + ":" + str(self.Minutes).zfill(2) + ":00"

    def current_datetime(self, x):
        if x == 0:
            return self.Year
        elif x == 1:
            return (self.Month + 1)
        elif x == 2:
            return self.Day
        elif x == 3:
            return self.Hours
        elif x == 4:
            return self.Days
        elif x == 5:
            return self.Minutes

    def AddTime(self, Minutes):
        temp = 0

        if Minutes > 60:
            self.Hours += Minutes // 60
            self.Minutes = Minutes % 60
        else:
            self.Minutes += Minutes
            
        if self.Minutes >= 60:
            temp = self.Minutes
            self.Minutes = temp % 60
            self.Hours += temp // 60

        if self.Hours >= 24:
            temp = self.Hours
            self.Hours = temp % 24
            self.Days += temp // 24
            self.Day += temp // 24

        if self.Day >= 7:
            self.Day -= 7

        if self.Days > self.MonthDays[self.Month]:
            self.Days = 1
            self.Month += 1

        if self.Month >= 12:
            self.Month -= 12
            self.Year += 1
            self.set_MonthDays()
