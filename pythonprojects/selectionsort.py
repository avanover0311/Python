arr = [8,1,5,3,2,0]



def selectionSort(arr):
	for j in range (len(arr)-1):
		for i in range(len(arr)-1):
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] =arr[i+1], arr[i]
	return arr
print (selectionSort(arr))