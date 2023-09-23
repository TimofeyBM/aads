import random
import typing
import timeit
import functools
import matplotlib.pyplot as plt


def timing_decorator(ndigits: int, number: int) -> typing.Callable:
    def decorator(func: typing.Callable) -> typing.Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> float:
            usage_time = timeit.timeit(
                lambda: func(*args, **kwargs),
                number=number,
            )
            return round(usage_time / number, ndigits)

        return wrapper

    return decorator


max_n = 1100001
max_vector = [random.randint(1, 100) for _ in range(max_n)]

ndigits = 6
number_of_runs = 5

n_values = list(range(1, max_n, 1100))
average_times = []


@timing_decorator(ndigits, number_of_runs)
def find_max_bruteforce(vector):
    max_value = vector[0]
    for value in vector:
        if value > max_value:
            max_value = value
    return max_value


for n in n_values:
    print(n)

    average_time = find_max_bruteforce(max_vector[:n])
    average_times.append(average_time)

plt.plot(n_values, average_times, linestyle='-', color='b')
plt.title('Зависимость времени поиска максимума простым перебором от n')
plt.xlabel('n')
plt.ylabel('Среднее время выполнения (секунды)')
plt.savefig('max.png')
