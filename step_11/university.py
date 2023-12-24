from student import Student, Aspirant
from cafeteria import Cafeteria


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

        print("Стипендия выплачена всем студентам и аспирантам.")

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

    def show_cafeterias_info(self):
        print("Информация о столовых в университете:")
        for cafeteria in self.cafeterias:
            print(cafeteria, end="\n\n")
