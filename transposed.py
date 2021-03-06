# Транспонирование матриц
def transposed(matrix):
	len_of_x = len(matrix)
	len_of_y = len(matrix[0])
	trans_matrix = []
	for y_items in range(len_of_y):
		temp = []
		for x_items in range(len_of_x):
			temp.append(matrix[x_items][y_items])
		trans_matrix.append(temp)
	return trans_matrix

print(transposed([[1, 2], [3, 4], [5, 6]]))