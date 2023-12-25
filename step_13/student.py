import random


class Student:
    def __init__(
        self,
        first_name: str,
        second_name: str,
        last_name: str,
        group: str,
        marks: list[int],
    ) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.last_name: str = last_name
        self.group: str = group
        self.marks: list[int] = marks
        self.scholarship_balance = 0
        self.satiety = 0

    def calculate_average_mark(self) -> float:
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def add_mark(self, mark) -> None:
        self.marks.append(mark)

    def receive_scholarship(self, amount) -> None:
        self.scholarship_balance += amount

    def participate_in_olympiad(self) -> int:
        return random.randint(0, 100)

    def visit_cafeteria(self, cafeteria, dish_name) -> None:
        for dish in cafeteria.dishes:
            if dish.name == dish_name:
                if self.scholarship_balance >= dish.cost:
                    self.scholarship_balance -= dish.cost
                    self.satiety += dish.satiety
                    print(
                        f"{self.first_name} {self.last_name} посетил(а) столовую {cafeteria.name} и приобрел(а) блюдо '{dish.name}'."
                    )
                    print(
                        f"Сытость студента {self.first_name} {self.last_name} теперь составляет {self.satiety}."
                    )
                else:
                    print(
                        f"{self.first_name} {self.last_name} не может приобрести блюдо '{dish.name}', так как у него не хватает средств."
                    )
                break
        else:
            print(
                f"Блюдо с названием '{dish_name}' не найдено в столовой {cafeteria.name}."
            )

    def __str__(self) -> str:
        return (
            f"Студент: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f} "
            f"Баланс стипендии: {self.scholarship_balance} у.е."
        )


class Aspirant:
    def __init__(
        self,
        first_name: str,
        second_name: str,
        last_name: str,
        group: str,
        science_work: str,
        science_progress: int,
        marks: list[int],
    ) -> None:
        self.first_name: str = first_name
        self.second_name: str = second_name
        self.last_name: str = last_name
        self.group: str = group
        self.science_work: str = science_work
        self.science_progress: int = science_progress
        self.marks: list[int] = marks
        self.scholarship_balance = 0
        self.satiety = 0

    def calculate_average_mark(self) -> float:
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def work_on_science(self, progress_increase) -> None:
        self.science_progress += progress_increase

    def receive_scholarship(self, amount) -> None:
        self.scholarship_balance += amount

    def participate_in_olympiad(self) -> int:
        return random.randint(0, 100)

    def __str__(self) -> str:
        return (
            f"Аспирант: {self.last_name} {self.first_name} {self.second_name}, "
            f"Группа: {self.group}, Средняя Оценка: {self.calculate_average_mark():.2f}, "
            f"Научная Работа: {self.science_work}, Прогресс: {self.science_progress}% "
            f"Баланс стипендии: {self.scholarship_balance} у.е."
        )

    def visit_cafeteria(self, cafeteria, dish_name) -> None:
        for dish in cafeteria.dishes:
            if dish.name == dish_name:
                if self.scholarship_balance >= dish.cost:
                    self.scholarship_balance -= dish.cost
                    self.satiety += dish.satiety
                    print(
                        f"{self.first_name} {self.last_name} посетил(а) столовую {cafeteria.name} и приобрел(а) блюдо '{dish.name}'."
                    )
                    print(
                        f"Сытость аспиранта {self.first_name} {self.last_name} теперь составляет {self.satiety}."
                    )
                else:
                    print(
                        f"{self.first_name} {self.last_name} не может приобрести блюдо '{dish.name}', так как у него не хватает средств."
                    )
                break
        else:
            print(
                f"Блюдо с названием '{dish_name}' не найдено в столовой {cafeteria.name}."
            )


if __name__ == "__main__":
    # Создание объекта класса Student
    student = Student(
        first_name="John",
        second_name="Doe",
        last_name="Smith",
        group="CS101",
        marks=[4, 5, 3],
    )

    # Создание объекта класса Aspirant
    aspirant = Aspirant(
        first_name="Jane",
        second_name="Air",
        last_name="Johnson",
        group="CS101",
        marks=[4, 5, 3],
        science_work="my first test work",
        science_progress=0,
    )

    # Перебор и вывод информации о студенте и аспиранте
    for performer in [student, aspirant]:
        print(performer)

        # Если объект является студентом, добавляем ему оценку и выводим обновленную информацию
        if isinstance(performer, Student):
            performer.add_mark(5)
            print(performer)

        # Выплата стипендии и вывод обновленной информации
        performer.receive_scholarship(1000)
        print(performer)

        # Если объект является аспирантом, он работает над научной работой и выводит прогресс
        if isinstance(performer, Aspirant):
            performer.work_on_science(progress_increase=10)
            print(performer)

        # Вывод результатов участия в олимпиаде
        print("Оценка на Олимпиаде:", performer.participate_in_olympiad())
