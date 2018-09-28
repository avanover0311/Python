class User:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed 
        self.miles = 0

    def displayInfo(self):
    	print(self.price)
    	print(self.max_speed)
    	print(self.miles)

    def ride(self):
    	self.miles = self.miles + 10
    	print("Riding")


    def reverse(self):
    	self.miles = self.miles - 5
    	print("Reversing")

bike1= User(100, '20mph')


bike1.ride() 
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()


