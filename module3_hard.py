data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calc_list(*list_):
    sum_ = 0
    for i in list_:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
        return sum_


def calc_dict(*dict_):
    sum_key = 0
    sum_value = 0
    sum_ = sum_key + sum_value
    for key in dict_.keys():
        if isinstance(key, int):
            sum_key += key
        elif isinstance(key, str):
            sum_key += len(key)
        elif isinstance(key, list):
            sum_key += calc_list(key)
        elif isinstance(key, dict):
            sum_key += calc_dict(key)
        elif isinstance(key, tuple):
            sum_key += calc_tuple(key)
        return sum_key
    for value in dict_.values():
        if isinstance(value, int):
            sum_value += value
        elif isinstance(value, str):
            sum_value += len(value)
        elif isinstance(value, list):
            sum_value += calc_list(value)
        elif isinstance(value, dict):
            sum_value += calc_dict(value)
        elif isinstance(value, tuple):
            sum_value += calc_tuple(value)
            return sum_value
    return sum_


def calc_tuple(*tup):
    sum_ = 0
    for i in tup:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
        return sum_


def calculate_structure_sum(func):
    sum_ = 0
    for i in func:
        if isinstance(i, int):
            sum_ += i
        elif isinstance(i, str):
            sum_ += len(i)
        elif isinstance(i, list):
            sum_ += calc_list(i)
        elif isinstance(i, dict):
            sum_ += calc_dict(i)
        elif isinstance(i, tuple):
            sum_ += calc_tuple(i)
        return sum_


result = calculate_structure_sum(data_structure)
print(result)