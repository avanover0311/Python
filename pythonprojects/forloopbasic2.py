
array = [-1,2,-3,4,5]
def biggie(array):
	for num in range(len(array)):
		if array[num] > 0:
			array[num] ="Big"
	return array
print(biggie(array))


array = [-1,1,1,1]
def count(array):
	x = 0
	for num in range(len(array)):
		if array[num] > 0:
			x += 1
	array[-1] = x
	return array

print(count(array))

array = [1,2,3,4,5]
def count(array):
	x = 0
	for num in range(len(array)):
		x += array[num]
	return x	
print(count(array))


array = [2,4,6,8]
def average(array):
	x =0
	for num in range(len(array)):
		x += array[num]
	avg = x/(len(array))
	return avg	
print(average(array))	


arr = [1,2,3,4]
def lengt(arr):
	return len(arr)

print(lengt(arr))

array = [1,2,3,-2,5]
def minimum(array):
	x = array[0]
	if len(array) == 0:
		return false
	else:	
		for num in range(len(array)): 
			if array[num] < x:
				x = array[num]
	return x
print(minimum(array))	

array = [1,2,3,-2,5]
def maximum(array):
	x = array[0]
	if len(array) == 0:
		return false
	else:	
		for num in range(len(array)): 
			if array[num] > x:
				x = array[num]
	return x
print(maximum(array))	

array = [1,2,3,-2,5]

def ultimateAnalyze(array):
	dic = {sumTotal:0, averag:0, minimum:0,maximum:0, length:0 }
	return dic
print(ultimateAnalyze(array))	
		

def rev(arr):

	arr.reverse()
	return arr
print(rev([1,2,3,4,5]))

