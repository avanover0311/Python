class Car:

	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage

	def display_all(self):
		display = {
		'Price' : self.price,
		'Speed' : self.speed,
		'Fuel' : self.fuel,
		'Mileage' : self.mileage
		}

		print(display)

	def tax(self):

		self.tax = .15
		if (self.price <10000):
			self.price * self.tax
		else:
			self.tax = .12
			self.price * self.tax
	print(tax)





car1 = Car(2000, '35mpg', 'Full', '15mpg')
car2 = Car(2000, '5mph', 'Not Full', '105mpg')
car3 = Car(2000, '15mph', 'Kind of Full', '105mpg')
car4 = Car(2000, '25mph', 'Full', '105mpg')
car5 = Car(2000, '45mph', 'Empty', '105mpg')
car6 = Car(20000000, '35mph', 'Empty', '15mpg')
car1.tax()
car1.display_all()