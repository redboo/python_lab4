import json
import random
from typing import Any

from cafeteria import Cafeteria
from student import Aspirant, Student
from university import University

# # Чтение данных об университетах из файла
with open("universities.json", "r", encoding="utf-8") as file:
    universities_data = json.load(file)

# Инициализация данных о столовых
cafeterias_data: list[dict[str, Any]] = [
    {
        "name": "Столовая 1",
        "dishes": [
            {"name": "Борщ", "satiety": 5, "cost": 3},
            {"name": "Пельмени", "satiety": 4, "cost": 4},
            {"name": "Салат", "satiety": 3, "cost": 2},
        ],
        "money": 100,
    },
    {
        "name": "Столовая 2",
        "dishes": [
            {"name": "Суп", "satiety": 4, "cost": 3},
            {"name": "Гречка", "satiety": 5, "cost": 5},
            {"name": "Курица", "satiety": 4, "cost": 4},
        ],
        "money": 150,
    },
]

# Создание объектов университетов
universities: list[University] = [
    University(cafeterias=cafeterias_data, **university)
    for university in universities_data
]

# Выбор случайного университета
university: University = random.choice(universities)

# Вывод информации о текущем университете
print(university)

# Создание данных о студентах
students_data: list[dict[str, Any]] = [
    {
        "first_name": "John",
        "second_name": "Doe",
        "last_name": "Smith",
        "group": "CS101",
        "marks": [4, 5, 3],
    },
    {
        "first_name": "Jane",
        "second_name": "Doe",
        "last_name": "Johnson",
        "group": "CS102",
        "marks": [3, 4, 5],
    },
    {
        "first_name": "Jane",
        "second_name": "Doe",
        "last_name": "Johnson",
        "group": "CS103",
        "marks": [5, 4, 5],
    },
]

# Зачисление студентов в университет
for student_data in students_data:
    university.enroll_student(Student(**student_data))

# Процесс отчисления студентов
university.dismiss_student(first_name="John", last_name="Smith")
university.dismiss_student(first_name="John", last_name="Smith")
university.dismiss_student(first_name="Jane", last_name="Johnson", group="CS103")
university.dismiss_student(first_name="Jane", last_name="Johnson", group="CS103")

# Пример использования случайных объектов студента и аспиранта
student: Student = random.choice(university.students)
print(student)

# Добавление оценки 5 случайному студенту
student.add_mark(5)
print(student)

# Вывод информации о случайном аспиранте
aspirant: Aspirant = random.choice(university.aspirants)
print(aspirant)

# Увеличение прогресса аспиранта случайным образом
aspirant_progress_increase: int = random.randint(0, 100 - aspirant.science_progress)
aspirant.work_on_science(aspirant_progress_increase)
print(aspirant)

# Выплата стипендии всем участникам университета
university.pay_scholarship()

# Проведение олимпиады
university.conduct_olympiad()

# Посещение столовой случайным студентом
student = random.choice(university.students)
cafeteria: Cafeteria = random.choice(university.cafeterias)
random_dish: str = random.choice(cafeteria.dishes).name
student.visit_cafeteria(cafeteria, random_dish)

# Посещение столовой случайным аспирантом
aspirant = random.choice(university.aspirants)
cafeteria = random.choice(university.cafeterias)
random_dish = random.choice(cafeteria.dishes).name
aspirant.visit_cafeteria(cafeteria, random_dish)
