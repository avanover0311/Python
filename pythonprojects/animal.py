class Animal:
	def __init__(self, name, health):
		self.name =name
		self.health =health

	def displayAll(self):
		print(self.name)
		print(self.health)
		return self


	def walk(self):
		self.health -= 1
		return self


	def run(self):
		self.health -= 5
		return self

class Dog(Animal):
	def __init__(self, name):
		super().__init__(name, 150)

	def pet(self):
		self.health +=5
		return self


class Dragon(Animal):
	def __init__(self, name):
		super().__init__(name, 170)

	def fly(self):
		self.health -= 10
		return self

cat1= Animal("biggles", 10)
dog1 = Dog("Fido")
dragon1 = Dragon("toothless")

for i in range(3):
	dog1.walk()
	cat1.walk()

for i in range (2):
	dog1.run()
	cat1.run()

dog1.pet().displayAll()
cat1.displayAll()
dragon1.displayAll().fly().displayAll()
