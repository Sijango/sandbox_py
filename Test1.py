def fib(number):
	first = 0
	second = 1
	index = 2
	if number and index <= number:
		while index <= number:
			result = first + second
			first = second
			second = result
			index += 1
		return result
	elif number == 1:
		return 1
	else:
		return 0

print(fib(3))
print(int('1000', 2))
result = format(8, 'b')
print(result)