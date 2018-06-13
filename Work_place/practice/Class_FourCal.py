#!/usr/bin/python
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

#a = FourCal()
b = FourCal()
#a.setdata(4, 2)
b.setdata(3, 7)

cal_a = FourCal()
#cal_b = FourCal()
cal_a.setdata(4, 2)
#cal_b.setdata(3, 7)
print (cal_a.sum())
print (cal_a.mul())
print (cal_a.sub())
print (cal_a.div())

print (b.sum())
print (b.mul())
print (b.sub())
print (b.div())