class product:
	def __init__(self,price,name, weight, brand):
		self.status = "for sale"
		self.price = price
		self.name = name
		self.weight = weight
		self.brand = brand


	def displayAll(self):
		print(self.price)
		print(self.name)
		print(self.weight)
		print(self.brand)
		return self

	def sell(self):
		self.status = "sold"
		print (self.status)
		return self

	def tax(self):
		if(self.status == "sold"):
			self.price = self.price + self.price * .07
		print (self.price)
		return self



	def retItem(self,reason_for_return):
		if reason_for_return == 'defective':
			self.status = 'defective'
		return self

product1 = product(2, 'apple', '2lbs', 'brayburn')
product1.displayAll()
