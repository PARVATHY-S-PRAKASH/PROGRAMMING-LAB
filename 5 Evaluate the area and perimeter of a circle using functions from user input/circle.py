
import math



def Area(radius):
    
	return math.pi * radius * radius
 
   

def Perimeter(radius):
    
	return 2 * math.pi * radius




r = int(input(' enter the radius of a circle: '))

area = Area(r)
perimeter = Perimeter(r)




print("\n Area Of a Circle =" ,area)
print(" Perimeter Of a Circle =" ,perimeter)

