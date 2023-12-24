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


# Загружаем данные из файла universities.json
with open("universities.json", "r") as file:
    data = json.load(file)

# Создаем объекты класса University для каждого университета
universities = [University(**university) for university in data]

# Примеры использования новых методов enroll_student и dismiss_student

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

universities[2].enroll_students(student1, student2)

universities[3].dismiss_student(first_name="John", last_name="Smith")
universities[2].dismiss_student(first_name="John", last_name="Smith")
universities[1].dismiss_student(first_name="Jane", last_name="Johnson", group="posuere")
universities[2].dismiss_student(first_name="Jane", last_name="Johnson", group="posuere")
