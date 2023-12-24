import json


class Student:
    def __init__(self, first_name, second_name, last_name, group, marks):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.marks = marks

    def __str__(self):
        return (
            f"Студент: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}"
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

    def __str__(self):
        return (
            f"Аспирант: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, "
            f"Научная Работа: {self.science_work}, Прогресс: {self.science_progress}%"
        )


class University:
    def __init__(self, name, students, aspirants):
        self.name = name
        self.students = [Student(**student) for student in students]
        self.aspirants = [Aspirant(**aspirant) for aspirant in aspirants]

    def __str__(self):
        university_info = [f"Университет: {self.name}"]

        students_info = ["Студенты:"]
        students_info.extend(str(student) for student in self.students)

        aspirants_info = ["Аспиранты:"]
        aspirants_info.extend(str(aspirant) for aspirant in self.aspirants)

        university_info.extend(students_info + aspirants_info)
        return "\n".join(university_info)


# Загружаем данные из файла universities.json
with open("universities.json", "r") as file:
    data = json.load(file)

# Создаем объекты класса University для каждого университета
universities = [University(**university) for university in data]

# Выводим информацию о первом университете
print(universities[0])
