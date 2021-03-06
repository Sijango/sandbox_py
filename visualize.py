from collections import Counter


def visualize(coins, bar_char = '₽'):
	coins_counter = {}
	for item in coins:
		if str(item) in coins_counter:
			coins_counter[str(item)] += 1
		else:
			coins_counter.setdefault(str(item), 1)
	list_keys = list(coins_counter.keys())
	list_keys.sort()
	for key in list_keys:
		print('{} = {}'.format(key, coins_counter[key]))
	max_value = max(coins_counter.values())
	print(max_value)

	while max_value >= 0:
		


visualize((2,2,2,2,2,2,1))