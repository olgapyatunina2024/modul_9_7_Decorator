def is_prime(func):
# функция wrapper в is_prime
    def wrapper(*args, ** kwargs):
        result = func(*args, ** kwargs)
        sum_ = sum(args)
        k = 0
        for i in range(2, sum_ // 2 + 1):
            if sum_ % i == 0:
                k = k +1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

# декоратор для функции sum_three
@is_prime
# функция сложения трех чисел
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)

result = sum_three(2, 3, 5)
print(result)