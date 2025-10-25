import time

def func_time(func):
    """Декоратор для измерения времени выполнения функции."""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Время выполнения функции: {execution_time:.6f} секунд")
        return result

    return wrapper


@func_time
def sum_numbers(a, b):
    """Вычисляет сумму двух чисел и выводит результат."""
    result = a + b
    print(f"Сумма = {result}")
    return result


@func_time
def sum_from_file():
    """Читает два числа из файла input.txt, вычисляет их сумму и записывает результат в output.txt."""
    try:
        with open('input.txt', 'r') as file:
            content = file.read().strip()
            numbers = content.split()
            if len(numbers) < 2:
                print("Ошибка: файл input.txt должен содержать как минимум два числа.")
                return None
            try:
                a = float(numbers[0])
                b = float(numbers[1])
            except ValueError:
                print("Ошибка: файл input.txt должен содержать два корректных числа.")
                return None
    except FileNotFoundError:
        print("Ошибка: файл input.txt не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла input.txt: {e}")
        return None

    result = a + b

    try:
        with open('output.txt', 'w') as file:
            file.write(f"Сумма {a} + {b} = {result}\n")
        print(f"Результат записан в файл output.txt: {result}")
    except Exception as e:
        print(f"Ошибка при записи в файл output.txt: {e}")
        return None
    return result



print("ТЕСТ 1: Вычисление суммы двух чисел")
sum_numbers(10, 25)

print("ТЕСТ 2: Чтение из файла и запись результата")
sum_from_file()
