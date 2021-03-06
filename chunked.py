def chunked(count, old):
	new_list = []
	index = count
	while index <= len(old) + count:
		print('in')
		start = index - count
		stop = index
		new_list.append(old[start:stop:])
		index += count
	return new_list

print(chunked(3, 'stri'))