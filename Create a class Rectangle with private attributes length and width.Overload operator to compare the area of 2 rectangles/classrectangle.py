
class rectangle:
	area = 0
	perimeter = 0
def init(self,length,width):
  self.length = length
self.width = widthdef calc_area(self):
  self.area = self.length*self.width
print("Area is:",self.	area)
def	lt(self,second):
if self.area < second.area:
return True
 
else:
return False

length1= int(input("Enter length of the rectangle 1 : "))
width1 = int(input("Enter width of the rectangle1 : "))
length2 = int(input("Enter length of the rectangle2: "))
width2 = int(input("Enter width of the rectangle2 : "))
obj1 = rectangle(length1,width1)
obj2 = rectangle(length2,width2)obj1.calc_area()
obj2.calc_area()if obj1 < obj2:
print("Rectangle two is large")
else:
print("Rectangle one is large or these are equal")




