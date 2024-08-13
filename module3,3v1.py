def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


values_list = [777, 'Azino', False]
values_list2 = [[34, 76], 'Text']
values_dict = {'a': 90, 'b': 'Шестьдесят', 'c':[9, 0]}

print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list2, 42)
print_params(42, *values_list2)

