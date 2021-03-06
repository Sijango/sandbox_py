# В этой практике вы будете реализовывать функции для работы
# с множествами, как с наборами флагов.
def toggle(something, flags):
    if something in flags:
        flags.discard(something)
    else:
        flags.add(something)


def toggled(something, flags):
    if flags:
        copy_flags = flags.copy()
    else:
        copy_flags = set()
    if something in copy_flags:
        copy_flags.discard(something)
    else:
        copy_flags.add(something)
    return copy_flags


READ_ONLY = 'read_only'
flags = set()
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)
toggle(READ_ONLY, flags)
print(READ_ONLY in flags)

new_flags = toggled(READ_ONLY, flags)
print(READ_ONLY in flags)
print(READ_ONLY in new_flags)
