def hamming_weight(number):
    binary_number = bin(number).replace('0b', '')
    print(binary_number)
    count = 0
    for item in binary_number:
    	print(item)
    	if int(item) > 0:
    		count += 1
    return count

print(hamming_weight(101))