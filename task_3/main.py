import math

class Figure:
    """Базовый класс для всех фигур."""

    def get_area(self):
        """Вычисляет площадь фигуры."""
        pass

    def get_perimeter(self):
        """Вычисляет периметр фигуры."""
        pass

    def compare_area(self, other):
        """Сравнивает площадь с другой фигурой."""
        my_area = self.get_area()
        other_area = other.get_area()

        if my_area > other_area:
            print(f"Площадь больше: {my_area:.2f} > {other_area:.2f}")
        elif my_area < other_area:
            print(f"Площадь меньше: {my_area:.2f} < {other_area:.2f}")
        else:
            print(f"Площади равны: {my_area:.2f} = {other_area:.2f}")

    def compare_perimeter(self, other):
        """Сравнивает периметр с другой фигурой."""
        my_perimeter = self.get_perimeter()
        other_perimeter = other.get_perimeter()

        if my_perimeter > other_perimeter:
            print(f"Периметр больше: {my_perimeter:.2f} > {other_perimeter:.2f}")
        elif my_perimeter < other_perimeter:
            print(f"Периметр меньше: {my_perimeter:.2f} < {other_perimeter:.2f}")
        else:
            print(f"Периметры равны: {my_perimeter:.2f} = {other_perimeter:.2f}")


class Square(Figure):
    """Класс для квадрата."""

    def __init__(self, side):
        self.side = side

    def get_area(self):
        """Вычисляет площадь квадрата."""
        return self.side ** 2

    def get_perimeter(self):
        """Вычисляет периметр квадрата."""
        return 4 * self.side


class Rectangle(Figure):
    """Класс для прямоугольника."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    def get_perimeter(self):
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)


class Triangle(Figure):
    """Класс для треугольника."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        """Вычисляет площадь треугольника по формуле Герона."""
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def get_perimeter(self):
        """Вычисляет периметр треугольника."""
        return self.a + self.b + self.c


class Circle(Figure):
    """Класс для круга."""

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        """Вычисляет площадь круга."""
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        """Вычисляет периметр (длину окружности) круга."""
        return 2 * math.pi * self.radius


square = Square(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(5, 3, 4)
circle = Circle(5)


print("Квадрат")
print(f"  Площадь: {square.get_area():.2f}")
print(f"  Периметр: {square.get_perimeter():.2f}\n")

print("Прямоугольник")
print(f"  Площадь: {rectangle.get_area():.2f}")
print(f"  Периметр: {rectangle.get_perimeter():.2f}\n")

print("Треугольник")
print(f"  Площадь: {triangle.get_area():.2f}")
print(f"  Периметр: {triangle.get_perimeter():.2f}\n")

print("Круг")
print(f"  Площадь: {circle.get_area():.2f}")
print(f"  Периметр: {circle.get_perimeter():.2f}\n")

print("Сравнение площадей\n")

print("Квадрат vs Прямоугольник:")
square.compare_area(rectangle)

print("\nКруг vs Треугольник:")
circle.compare_area(triangle)

print("\nСравнение периметров\n")

print("Прямоугольник vs Квадрат:")
rectangle.compare_perimeter(square)

print("\nКруг vs Треугольник:")
circle.compare_perimeter(triangle)