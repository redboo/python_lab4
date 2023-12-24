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


class University:
    def __init__(self, name, students, aspirants):
        self.name = name
        self.students = [Student(**student) for student in students]
        self.aspirants = [Aspirant(**aspirant) for aspirant in aspirants]
        self.scholarship_balance = 200

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


# Пример использования нового метода conduct_olympiad()

# Загружаем данные из файла universities.json
with open("universities.json", "r") as file:
    data = json.load(file)

# Создаем объекты класса University для каждого университета
universities = [University(**university) for university in data]

# Проводим олимпиаду
universities[0].conduct_olympiad()

# Выводим информацию о студентах и аспирантах после олимпиады
print(universities[0])
