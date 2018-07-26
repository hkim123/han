class FourCal:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def multi(self):
        result = self.first * self.second
        return result

a=FourCal()

a.setdata(4,2)
print (a.sum())
print (a.multi())