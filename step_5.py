import json


class Student:
    def __init__(self, first_name, second_name, last_name, group, marks):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.marks = marks

    def calculate_average_mark(self):
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def add_mark(self, mark):
        self.marks.append(mark)

    def __str__(self):
        return (
            f"Студент: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f}"
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

    def calculate_average_mark(self):
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def __str__(self):
        return (
            f"Аспирант: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f}, "
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


# Пример использования нового метода add_mark()
student = Student(
    first_name="John",
    second_name="Doe",
    last_name="Smith",
    group="CS101",
    marks=[4, 5, 3],
)

print(student)  # Вывод: Студент: Smith John Doe, Группа: CS101, Средняя Оценка: 4.00

# Получение новой оценки
student.add_mark(5)

print(student)  # Вывод: Студент: Smith John Doe, Группа: CS101, Средняя Оценка: 4.25
