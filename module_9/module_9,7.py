import math

def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1 and result != 0:
            for i in range(2, int(math.sqrt(result)) + 1):
                if result % i == 0:
                    print('Данное число составное.')
                    return result
            print('Данное число простое.')
            return result
    return wrapper 

@is_prime
def sum_three(*args):

    result = sum(args)
    return result


result = sum_three(2, 3, 6)
print(result)