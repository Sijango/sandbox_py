# Функция count_all. Эта функция должна принимать на вход iterable 
# источник и возвращать словарь, ключами которого являются 
# элементы источника, а значения отражают количество повторов 
# элемента в коллекции-источнике. 

def count_all(something):
    if not something:
        return {}
    result = {}
    something = list(something)
    for item in something:
    	if not result.get(item):
    		result.setdefault(item, 0)
    	result[item] += 1
    return result


print(count_all("GG"))
# count = {'a': 20}
# print(count['a'])