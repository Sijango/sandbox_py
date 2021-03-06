import random

num = random.randint(1, 50)
for i in range(6):
	print(f'Попытка №{i + 1}')
	Num = input()
	if int(Num) == num:
		print('Игра закончена, вы выйграли.')
		break
	elif int(Num) >= num:
		print('Ниже')
	elif int(Num) <= num:
		print('Выше')
	if (i + 1) == 6:
		print('Игра закончена, вы проиграли.')
print(f'Загаданное число = {num}')
