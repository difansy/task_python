class Student:
    """Класс для студента."""

    def __init__(self, full_name, age, group_number, average_grade):
        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_grade = average_grade

    def show_info(self):
        """Выводит информацию о студенте."""
        print(f"ФИО: {self.full_name}")
        print(f"Возраст: {self.age} лет")
        print(f"Группа: {self.group_number}")
        print(f"Средний балл: {self.average_grade}")

    def get_scholarship(self):
        """Вычисляет размер стипендии студента."""
        if self.average_grade == 5:
            return 6000
        elif self.average_grade < 5:
            return 4000
        else:
            return 0

    def show_scholarship(self):
        """Выводит размер стипендии."""
        scholarship = self.get_scholarship()
        print(f"Стипендия: {scholarship} руб.")

    def compare_scholarship(self, other):
        """Сравнивает размер стипендии с другим студентом/аспирантом."""
        my_scholarship = self.get_scholarship()
        other_scholarship = other.get_scholarship()

        if my_scholarship > other_scholarship:
            print(f"Стипендия больше: {my_scholarship} руб. > {other_scholarship} руб.")
        elif my_scholarship < other_scholarship:
            print(f"Стипендия меньше: {my_scholarship} руб. < {other_scholarship} руб.")
        else:
            print(f"Стипендии равны: {my_scholarship} руб. = {other_scholarship} руб.")


class Aspirant(Student):
    """Класс для аспиранта."""

    def __init__(self, full_name, age, group_number, average_grade, research_work):
        """Инициализирует аспиранта."""
        super().__init__(full_name, age, group_number, average_grade)
        self.research_work = research_work

    def show_info(self):
        """Выводит информацию об аспиранте."""
        super().show_info()
        print(f"Научная работа: {self.research_work}")

    def get_scholarship(self):
        """Вычисляет размер стипендии аспиранта."""
        if self.average_grade == 5:
            return 8000
        elif self.average_grade < 5:
            return 6000
        else:
            return 0

# Создаём студентов
student1 = Student("Афанасьев Дмитрий Павлович", 20, "5132704/30801", 4.25)
student2 = Student("Павелков Артём Владимирович", 19, "5132704/30502", 5.0)

# Создаём аспирантов
aspirant1 = Aspirant(
    "Козлов Дмитрий Николаевич",
    25,
    "5132704/40802",
    4.3,
    "Влияние котов на психологическое состояние людей"
)
aspirant2 = Aspirant(
    "Фошкин Павел Дмитриевич",
    24,
    "5132704/50801",
    5.0,
    "Оптимизация алгоритмов сортировки"
)

print("Информация о студентах")
print("Студент 1")
student1.show_info()
student1.show_scholarship()

print("Студент 2")
student2.show_info()
student2.show_scholarship()

print("Информация об аспирантах")
print("Аспирант 1")
aspirant1.show_info()
aspirant1.show_scholarship()

print("Аспирант 2")
aspirant2.show_info()
aspirant2.show_scholarship()

print("Сравнение стипендий")

print("Студент 1 vs Студент 2:")
student1.compare_scholarship(student2)

print("Аспирант 1 vs Аспирант 2:")
aspirant1.compare_scholarship(aspirant2)

print("Студент 1 vs Аспирант 1:")
student1.compare_scholarship(aspirant1)