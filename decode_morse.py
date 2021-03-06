MORSE_CODE = {
	'....': 'H',
	'.': 'E',
	'-.--': 'Y',
	'.---': 'J',
	'..-': 'U',
	'-..': 'D'
}


def decode_Morse(morse_code):
	temp = ''
	counter_space = 0
	result = []
	# print(f'len = {len(morse_code)}')
	for index, _ in enumerate(morse_code):
		if morse_code[index] != ' ':
			temp += morse_code[index]
			counter_space = 0
			if (index + 1) == len(morse_code):
				# print('yes')
				result.append(temp.replace(temp, MORSE_CODE[temp]))
		elif temp in MORSE_CODE:
			result.append(temp.replace(temp, MORSE_CODE[temp]))
			# print(f'temp = {temp}, index = {index}, counter_space = {counter_space}')
			temp = ''
		else:
			counter_space += 1
			if counter_space == 2 and index >= 2:
				result.append(' ')
	return ''.join(result)


print(decode_Morse(' .... . -.--   .--- ..- -.. .'))