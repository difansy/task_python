def check_palindrome(t: str) -> bool:
    """Проверяет, является ли строка палиндромом."""
    text = ""
    for char in t:
        if char.isalpha() or char.isdigit():
            text += char.lower()

    return text == text[::-1]

print(check_palindrome("заказ"))
print(check_palindrome("Дом мод"))
print(check_palindrome("Дмитрий"))
print(check_palindrome("1221"))
