class Bike:
	def __init__(self, price, max_speed):
		self.max_speed = max_speed 
		self.price= price
		self.miles = 0

	def displayInfo(self):
		self.price = price
		self.max_speed = max_speed
		self.miles = miles

	def ride(self):
		self.miles = self.miles + 10
		print ("Riding")


	def reverse(self):
		self.miles = self.miles - 5
		print ("Reversing")

Bike1 = Bike("200","150")
Bike1.ride()
Bike1.reverse()
Bike1.reverse()
Bike1.displayInfo()