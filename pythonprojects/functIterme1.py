import random

def randInt(min=0, max=100):
	print(int(random.random()* (max-min)+min))


randInt()
randInt(max= 50)
randInt(min = 50)
randInt(min=50, max=500)
