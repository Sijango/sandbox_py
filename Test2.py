from math import log


def is_power_of_three(number):
    if number:
        result = log(number, 3)
        return isinstance(result, int)

print(is_power_of_three(3))
print(isinstance(1, int))
print(log(3, 3))
print(round(3.2))