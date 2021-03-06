# реализовать функцию all_unique, которая должна принимать итератор 
# (в т.ч. и те, которые не перезапускаемые!) и возвращать True, если 
# элементы в итераторе не повторяются (если элементов нет, то ничего не повторяется!). 
def all_unique(something):
	something = list(something)
   if len(something) == len(set(something)) or not something:
      return True
   return False


print(len('ggggg'))
print(len(set('ggggg')))
# item = iter([])
# item = list(item)
# print(len(item))