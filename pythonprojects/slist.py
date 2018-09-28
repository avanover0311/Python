class Node:
	def __init__(self, value):
		self.value= value
		self.next = None

class SList:
	def __init__(self, value):
		node = Node(value)
		self.head = node

	def addNode(self, value):
		node = Node(value)
		runner = self.head
		while(runner.next != None):
			runner = runner.next
		runner.next = node

	def removeNode(self, value):
		node = Node(value)
		runner = self.head
		


	def printAllValues(self, msg=""):
		runner = self.head
		print("\n\nhead points to ", id(self.head))
		print("printing the value in the list ---", msg,"----")
		while (runner.next != None):
			print(id(runner), runner.value, id(runner.next))
			runner = runner.next
		print(id(runner), runner.value, id(runner.next))
print

list= SList(5)
list.addNode(10)
list.addNode(7)
list.addNode(9)
list.addNode(1)

list.printAllValues('Attempt 1')