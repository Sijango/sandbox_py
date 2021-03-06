print('\nДобро пожаловать в китайскую игру "2 Палочки"')
print('Играют 2 игрока, по очереди берут от одной до трёх палок')
print('Введите имена игроков и количество палок от 10 и больше')

NameFirst = input('\nИмя первого игрока ')
NameSecond = input('Имя второго игрока ')
Num = int(input("Кол-во палок "))

Num1 = 0
Num2 = 0

print(f'\nИмя 1-ого игрока {NameFirst}\nИмя 2-ого игрока {NameSecond}\nКол-во палочек {Num}\n')

while Num != 0:
	print(f'{NameFirst} берёт ')
	take = int(input())
	if take >= 1 and take <= 3 and (Num - take) >= 0:
		Num -= take
		print(f'Кол-во палочек {Num}')
	else:
		print("Не подходит по условию, вы пропускаете ход")
	if Num == 0:
		print(f'Побеждает {NameSecond}')
		break

	print(f'{NameSecond} берёт ')
	take = int(input())
	if take >= 1 and take <= 3 and (Num - take) >= 0:
		Num -= take
		print(f'Кол-во палочек {Num}')
	else:
		print("Не подходит по условию, вы пропускаете ход")
	if Num == 0:
		print(f'Побеждает {NameFirst}')
		break
