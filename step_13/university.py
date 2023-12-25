from typing import Any, Optional, Union

from cafeteria import Cafeteria
from student import Aspirant, Student


class University:
    def __init__(
        self,
        name: str,
        students: list[dict[str, Any]],
        aspirants: list[dict[str, Any]],
        cafeterias: Optional[list[dict[str, Any]]] = None,
    ) -> None:
        self.name: str = name
        self.students: list[Student] = [Student(**student) for student in students]
        self.aspirants: list[Aspirant] = [
            Aspirant(**aspirant) for aspirant in aspirants
        ]
        self.scholarship_balance = 200

        self.cafeterias: list[Cafeteria] = (
            [Cafeteria(**cafeteria) for cafeteria in cafeterias] if cafeterias else []
        )

    def __str__(self) -> str:
        university_info: list[str] = [f"Университет: {self.name}"]

        students_info: list[str] = ["Студенты:"]
        students_info.extend(str(student) for student in self.students)

        aspirants_info: list[str] = ["Аспиранты:"]
        aspirants_info.extend(str(aspirant) for aspirant in self.aspirants)

        cafeterias_info: list[str] = ["Столовые:"]
        cafeterias_info.extend(str(cafeteria) for cafeteria in self.cafeterias)

        university_info.extend(students_info + aspirants_info + cafeterias_info)
        return "\n".join(university_info)

    def enroll_student(self, student) -> None:
        self.students.append(student)
        print(
            f"Студент {student.last_name} {student.first_name} {student.second_name} зачислен в университет {self.name}."
        )

    def enroll_students(self, *students) -> None:
        for student in students:
            self.enroll_student(student)

    def dismiss_student(self, first_name, last_name, group=None) -> None:
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

    def pay_scholarship(self) -> None:
        for student in self.students:
            student.receive_scholarship(self.scholarship_balance)

        for aspirant in self.aspirants:
            aspirant.receive_scholarship(self.scholarship_balance)

        print("Стипендия выплачена всем студентам и аспирантам.")

    def conduct_olympiad(self) -> None:
        scores: list[tuple[Union[Student, Aspirant], int]] = []

        for student in self.students:
            score: int = student.participate_in_olympiad()
            scores.append((student, score))

        for aspirant in self.aspirants:
            score: int = aspirant.participate_in_olympiad()
            scores.append((aspirant, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        top_performers: list[tuple[Union[Student, Aspirant], int]] = scores[:3]

        for performer, score in top_performers:
            performer.receive_scholarship(500)
            scholar_type: str = (
                "Студент" if isinstance(performer, Student) else "Аспирант"
            )
            print(
                f"{scholar_type} {performer.first_name} {performer.last_name} получает дополнительную стипендию в размере 500 у.е. за успешное участие в олимпиаде."
            )


if __name__ == "__main__":
    # Создание объекта университета с данными из словаря
    university_data_with_cafeterias: dict[str, Any] = {
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
                    {"name": "Борщ", "satiety": 3, "cost": 3},
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

    # Создание объекта университета
    university = University(**university_data_with_cafeterias)

    print(university)

    # Создание трех студентов
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

    # Зачисление студентов в университет
    university.enroll_student(student1)
    university.enroll_students(student2, student3)

    print(university)

    # Отчисление студентов
    university.dismiss_student(first_name="John", last_name="Smith")
    university.dismiss_student(first_name="Jane", last_name="Johnson", group="CS102")

    print(university)

    # Выплата стипендии студентам и аспирантам
    university.pay_scholarship()

    print(university)

    # Проведение олимпиады и вывод результатов
    university.conduct_olympiad()
