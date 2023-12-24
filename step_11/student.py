import random


class Student:
    def __init__(self, first_name, second_name, last_name, group, marks):
        self.first_name = first_name
        self.second_name = second_name
        self.last_name = last_name
        self.group = group
        self.marks = marks
        self.scholarship_balance = 0
        self.satiety = 0

    def calculate_average_mark(self):
        return sum(self.marks) / len(self.marks) if len(self.marks) > 0 else 0

    def add_mark(self, mark):
        self.marks.append(mark)

    def receive_scholarship(self, amount):
        self.scholarship_balance += amount

    def participate_in_olympiad(self):
        return random.randint(0, 100)

    def visit_cafeteria(self, cafeteria, dish_name):
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
        self.satiety = 0

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

    def visit_cafeteria(self, cafeteria, dish_name):
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
