import json
import random

from student import Student
from university import University

# Чтение данных из файла
with open("universities.json", "r", encoding="utf-8") as file:
    universities_data = json.load(file)

cafeterias = [
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
universities = [
    University(cafeterias=cafeterias, **university) for university in universities_data
]

university = random.choice(universities)

print(university)

student = Student(
    first_name="John",
    second_name="Doe",
    last_name="Smith",
    group="CS101",
    marks=[4, 5, 3],
)
student2 = Student(
    first_name="Jane",
    second_name="Doe",
    last_name="Johnson",
    group="CS102",
    marks=[3, 4, 5],
)
student3 = Student(
    first_name="Jane",
    second_name="Doe",
    last_name="Johnson",
    group="CS103",
    marks=[5, 4, 5],
)

university.enroll_student(student)
university.enroll_students(student2, student3)

university.dismiss_student(first_name="John", last_name="Smith")
university.dismiss_student(first_name="John", last_name="Smith")
university.dismiss_student(first_name="Jane", last_name="Johnson", group="CS103")
university.dismiss_student(first_name="Jane", last_name="Johnson", group="CS103")

student = random.choice(university.students)
print(student)

student.add_mark(5)
print(student)

aspirant = random.choice(university.aspirants)
print(aspirant)

aspirant.work_on_science(random.randint(0, (100 - aspirant.science_progress)))
print(aspirant)

university.pay_scholarship()

university.conduct_olympiad()

student = random.choice(university.students)
cafeteria = random.choice(university.cafeterias)
student.visit_cafeteria(cafeteria, random.choice(cafeteria.dishes).name)

aspirant = random.choice(university.aspirants)
cafeteria = random.choice(university.cafeterias)
aspirant.visit_cafeteria(cafeteria, random.choice(cafeteria.dishes).name)
