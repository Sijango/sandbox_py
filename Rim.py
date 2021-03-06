# Данная программа переводит римские цивфры в обычные (:


def pars(Rim):
	Result = 0
	for i, item in enumerate(Rim):
		if (i < len(Rim) - 1) and (Rims[Rim[i]] < Rims[Rim[i+1]]):
			Result -= Rims[Rim[i]]
		else:
			Result += Rims[Rim[i]]
	return Result

def to_roman(number):
	result = ''
	stop_sum = 0
	for key, values in NUMERALS.items():
		if number / values > 0 and stop_sum <= number:
			print('yes')
			result += key * int(abs(number / values))
			stop_sum += values * int(abs(number / values))
	return result

def to_arrabic(number):
	result_number = ''
	stop_number = number
	for key, values in NUMERALS.items():
		if stop_number - values >= 0 and stop_number / values > 0 and stop_number > 0:
			print('yeap')
			result_number += key * int(abs(stop_number / values))
			stop_number -= values
		elif stop_number == 0:
			break
	return result_number


NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}
Rims = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
# print(pars('XX')==20) 
# print(pars('I'))
# print(pars('LIX'))
# print(pars('MMM'))
# print(to_roman(6))
print(to_arrabic(9))