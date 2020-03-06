


class Rectangle:

	def __init__(self, sideA=0, sideB=0):
		self.sideA = sideA
		self.sideB = sideB

	def getArea(self):
		return self.sideA * self.sideB
	
	def getPerimeter(self):
		return 2 * (self.sideA + self.sideB)





class Circle:

	def __init__(self, radius, PI = 3.141592653589793):
		self.radius = radius
		self.PI = PI
	
	def getArea(self):
		return self.PI * self.radius ** 2
	
	def getPerimeter(self):
		return 2 * self.PI * self.radius








# Test Case

circy = Circle(11)
print(circy.getArea())

# Should return 380.132711084365

circy = Circle(4.44)
print(circy.getPerimeter())

# Should return 27.897342763877365
