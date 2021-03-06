def move_zeros(array):
	index = 0
	while index < len(array):
		if array[index] == 0:
			array.pop(index)
			array.append(0)
		else:
			index += 1
	return array


print(move_zeros([1,2,0,1,0,1,0,3,0,1]))
print(move_zeros([9,0.0,0,9,1,2,0,1,0,1,0.0,3,0,1,9,0,0,0,0,False,9]))