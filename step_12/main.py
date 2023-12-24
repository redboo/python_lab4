import json

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

university = universities[0]

print(university)

student1 = Student(
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
    group="ut",
    marks=[3, 4, 5],
)
student3 = Student(
    first_name="Jane",
    second_name="Doe",
    last_name="Johnson",
    group="posuere",
    marks=[5, 4, 5],
)

universities[0].enroll_student(student1)
universities[1].enroll_student(student2)
universities[2].enroll_student(student3)

universities[3].enroll_students(student1, student2)

universities[3].dismiss_student(first_name="John", last_name="Smith")
universities[2].dismiss_student(first_name="John", last_name="Smith")
universities[2].dismiss_student(first_name="Jane", last_name="Johnson", group="posuere")
universities[1].dismiss_student(first_name="Jane", last_name="Johnson", group="posuere")

# Пример использования нового метода add_mark()
student = university.students[0]
print(student)

# Получение новой оценки
student.add_mark(5)
print(student)

# Пример использования нового метода work_on_science()
# Создаем объект аспиранта
aspirant = university.aspirants[0]
print(aspirant)

# Аспирант работает над своей научной работой
aspirant.work_on_science(10)
print(aspirant)

# Университет выплачивает стипендии
university.pay_scholarship()

# Проводим олимпиаду
university.conduct_olympiad()

# Посещение столовой студентом
student1 = university.students[0]
cafeteria1 = university.cafeterias[0]
student1.visit_cafeteria(cafeteria1, "Борщ")

# Посещение столовой аспирантом
aspirant1 = university.aspirants[0]
cafeteria2 = university.cafeterias[1]
aspirant1.visit_cafeteria(cafeteria2, "Гречка")
