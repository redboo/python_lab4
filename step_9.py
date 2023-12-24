import json
import random


class Student:
    def __init__(self, first_name, second_name, last_name, group, marks):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
        self.scholarship_balance = 0

    def calculate_average_mark(self):
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def add_mark(self, mark):
        self.marks.append(mark)

    def receive_scholarship(self, amount):
        self.scholarship_balance += amount

    def participate_in_olympiad(self):
        return random.randint(0, 100)

    def __str__(self):
        return (
            f"Студент: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f} "
            f"Баланс стипендии: {self.scholarship_balance} у.е."
        )


class Aspirant:
    def __init__(
        self,
        first_name,
        second_name,
        last_name,
        group,
        science_work,
        science_progress,
        marks,
    ):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.science_work = science_work
        self.science_progress = science_progress
        self.marks = marks
        self.scholarship_balance = 0

    def calculate_average_mark(self):
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def work_on_science(self, progress_increase):
        self.science_progress += progress_increase

    def receive_scholarship(self, amount):
        self.scholarship_balance += amount

    def participate_in_olympiad(self):
        return random.randint(0, 100)

    def __str__(self):
        return (
            f"Аспирант: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f}, "
            f"Научная Работа: {self.science_work}, Прогресс: {self.science_progress}% "
            f"Баланс стипендии: {self.scholarship_balance} у.е."
        )


class Dish:
    def __init__(self, name, satiety, cost):
        self.name = name
        self.satiety = satiety
        self.cost = cost

    def __str__(self):
        return f"{self.name} (Сытость: {self.satiety}, Стоимость: {self.cost} у.е.)"


class Cafeteria:
    def __init__(self, name, dishes, money):
        self.name = name
        self.dishes = [Dish(**dish) for dish in dishes]
        self.money = money

    def __str__(self):
        cafeteria_info = [f"Столовая: {self.name} (Деньги: {self.money} у.е.)"]

        dishes_info = ["Блюда:"]
        dishes_info.extend(str(dish) for dish in self.dishes)

        cafeteria_info.extend(dishes_info)
        return "\n".join(cafeteria_info)


class University:
    def __init__(self, name, students, aspirants, cafeterias=None):
        self.name = name
        self.students = [Student(**student) for student in students]
        self.aspirants = [Aspirant(**aspirant) for aspirant in aspirants]
        self.scholarship_balance = 200

        self.cafeterias = (
            [Cafeteria(**cafeteria) for cafeteria in cafeterias] if cafeterias else []
        )

    def __str__(self):
        university_info = [f"Университет: {self.name}"]

        students_info = ["Студенты:"]
        students_info.extend(str(student) for student in self.students)

        aspirants_info = ["Аспиранты:"]
        aspirants_info.extend(str(aspirant) for aspirant in self.aspirants)

        cafeterias_info = ["Столовые:"]
        cafeterias_info.extend(str(cafeteria) for cafeteria in self.cafeterias)

        university_info.extend(students_info + aspirants_info + cafeterias_info)
        return "\n".join(university_info)

    def enroll_student(self, student):
        self.students.append(student)
        print(
            f"Студент {student.last_name} {student.first_name} {student.second_name} зачислен в университет {self.name}."
        )

    def enroll_students(self, *students):
        for student in students:
            self.enroll_student(student)

    def dismiss_student(self, first_name, last_name, group=None):
        for student in self.students:
            if (
                student.first_name == first_name
                and student.last_name == last_name
                and (group is None or student.group == group)
            ):
                self.students.remove(student)
                print(
                    f"Студент {student.last_name} {student.first_name} {student.second_name} исключен из университета {self.name}."
                )
                break
        else:
            print(f"Студент {last_name} {first_name} не найден.")

    def pay_scholarship(self):
        for student in self.students:
            student.receive_scholarship(self.scholarship_balance)

        for aspirant in self.aspirants:
            aspirant.receive_scholarship(self.scholarship_balance)

    def conduct_olympiad(self):
        scores = []

        for student in self.students:
            score = student.participate_in_olympiad()
            scores.append((student, score))

        for aspirant in self.aspirants:
            score = aspirant.participate_in_olympiad()
            scores.append((aspirant, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        top_performers = scores[:3]  # Топ-3 участников

        for performer, score in top_performers:
            performer.receive_scholarship(500)
            scholar_type = "Студент" if isinstance(performer, Student) else "Аспирант"
            print(
                f"{scholar_type} {performer.first_name} {performer.last_name} получает дополнительную стипендию в размере 500 у.е. за успешное участие в олимпиаде."
            )


# Пример использования новых классов и метода show_cafeterias_info()
# Создаем объекты класса University с информацией о блюдах и столовых
university_data_with_cafeterias = {
    "name": "Мой Университет",
    "students": [
        {
            "first_name": "Иван",
            "second_name": "Иванов",
            "last_name": "Иванович",
            "group": "CS101",
            "marks": [4, 5, 3],
        },
        {
            "first_name": "Петр",
            "second_name": "Петров",
            "last_name": "Петрович",
            "group": "CS102",
            "marks": [5, 4, 5],
        },
    ],
    "aspirants": [
        {
            "first_name": "Мария",
            "second_name": "Иванова",
            "last_name": "Петровна",
            "group": "CS201",
            "science_work": "Data Science",
            "science_progress": 70,
            "marks": [5, 5, 4],
        },
        {
            "first_name": "Александр",
            "second_name": "Петров",
            "last_name": "Александрович",
            "group": "CS202",
            "science_work": "Artificial Intelligence",
            "science_progress": 80,
            "marks": [4, 5, 4],
        },
    ],
    "cafeterias": [
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
    ],
}

my_university = University(**university_data_with_cafeterias)

# Выводим информацию о столовых
for cafeteria in my_university.cafeterias:
    print(cafeteria, end="\n\n")
