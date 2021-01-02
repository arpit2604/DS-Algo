def quickSort(array):
	quickSortHelper(array,0,len(array)-1)
	return array

def quickSortHelper(array,start_index,end_index):
	if start_index >= end_index:
		return
	pivot_index = start_index
	left_index = start_index + 1
	right_index = end_index
	while left_index<=right_index:
		if array[left_index] > array[pivot_index] and array[right_index] < array[pivot_index]:
			array[left_index],array[right_index] = array[right_index],array[left_index]
			
		if array[left_index] <= array[pivot_index]:  
			left_index+=1
		if array[right_index] >= array[pivot_index]:
			right_index-=1
	array[pivot_index],array[right_index] = array[right_index],array[pivot_index]
	rightarray = end_index-right_index+ 1
	leftarray = right_index-1 - start_index
	if leftarray>=rightarray:
		quickSortHelper(array,right_index+ 1,end_index)
		quickSortHelper(array,start_index,right_index-1)
	else:
		quickSortHelper(array,start_index,right_index-1)
		quickSortHelper(array,right_index+ 1,end_index)
	
