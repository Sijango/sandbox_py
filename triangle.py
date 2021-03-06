def triangle(number):
	items = [1, ]
	result_items = []
	while (len(items) - 1) < number:
		for index, _ in enumerate(items):
			if index != 0:
				result_items.append(items[index] + items[index - 1])
			else:
				result_items.append(1)				
		items = result_items
		items.append(1)
		result_items = []
	return items


print(triangle(4))	
