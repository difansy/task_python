def check_palindrome(t: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    chars = []
    for char in t:
        if char.isalpha() or char.isdigit():
            chars.append(char.lower())
    text = ''.join(chars)
    return text == text[::-1]

print(check_palindrome("заказ"))
print(check_palindrome("Дом мод"))
print(check_palindrome("Дмитрий"))
print(check_palindrome("1221"))
