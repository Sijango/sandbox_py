def merged(*data):
	result = {}
	for element in data:
		if not element:
			return {}
		for key, item in element.items():
			if key in result:
				result[key] += values
			else:
				result.setdefault(key, value)
	return result


print(merged({'a': 1}, {'a': 2}))