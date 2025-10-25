def filter_strings(lambda_func, strings):
    """Фильтрует массив строк по заданному условию."""
    return list(filter(lambda_func, strings))

test_strings = ['laptop', 'cookie', 'milk', 'cookie with milk', 'airplane', 'Apple Jack']

print(filter_strings(lambda f: ' ' not in f, test_strings))
print(filter_strings(lambda f: not f.startswith('a'), test_strings))
print(filter_strings(lambda f: len(f) >= 5, test_strings))
