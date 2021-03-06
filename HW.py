print("Hallo, world!")
print(str(bin(8)))
def countBits(n):
    bit_string = list(bin(n))
    counter = 0
    for item in bit_string:
        print(item)
        if int(item) == 1:
            counter += 1
    return counter
            
print(countBits(28))