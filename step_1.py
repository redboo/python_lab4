import json


class Student:
    def __init__(self, first_name, second_name, last_name, group, marks):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.marks = marks


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


class University:
    def __init__(self, name, students, aspirants):
        self.name = name
        self.students = [Student(**student) for student in students]
        self.aspirants = [Aspirant(**aspirant) for aspirant in aspirants]

    def print_info(self):
        print(f"Университет: {self.name}")
        print("Студенты:")
        for student in self.students:
            print(
                f"  - {student.last_name} {student.first_name} {student.second_name}, группа: {student.group}"
            )

        print("Аспиранты:")
        for aspirant in self.aspirants:
            print(
                f"  - {aspirant.last_name} {aspirant.first_name} {aspirant.second_name}, группа: {aspirant.group}"
            )
            print(
                f"    Научная работа: {aspirant.science_work}, Прогресс: {aspirant.science_progress}%"
            )


# Загружаем данные из файла universities.json
with open("universities.json", "r") as file:
    data = json.load(file)

# Создаем объекты класса University для каждого университета
universities = [University(**university) for university in data]

# Выводим информацию о первом университете
universities[0].print_info()
