# Требуется реализовать функцию diff_keys, которая должна 
# принимать два словаря-аргумента — "старый" и "новый" — и 
# возвращать словарь с результатами анализа. 
# Результирующий словарь должен содержать строго 
# три ниже перечисленных ключа:

# 1. 'kept' — множество ключей, которые присутствовали в старом словаре и остались в новом;
# 2. 'added' — множество ключей, которые отсутствовали в старом словаре, но появились в новом;
# 3. 'removed' — множество ключей, которые присутствовали в старом словаре, но в новый не вошли.

def diff_keys(old_set, new_set):
	result_set = {}
	result_set.setdefault('kept', set(old_set) & set(new_set))
	result_set.setdefault('added', set(new_set) - set(old_set))
	result_set.setdefault('removed', set(old_set) - set(new_set))
	return result_set


print(diff_keys({'name': 'Bob', 'age': 42}, {}))