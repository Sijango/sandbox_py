def expanded_form(num):
	num = list(str(num))
	print(num)
	len_num = len(num)
	result_string = ''
	temp_list = []
	for item in num:
		len_num -= 1
		temp_num = int(item) * 10 ** len_num
		if temp_num != 0:
			temp_list.append(str(temp_num))
	return ' + '.join(item for item in temp_list)


print(expanded_form(103))