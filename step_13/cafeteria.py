from typing import Any


class Dish:
    def __init__(self, name: str, satiety: int, cost: float) -> None:
        self.name: str = name
        self.satiety: int = satiety
        self.cost: float = cost

    def __str__(self) -> str:
        return f"{self.name} (Сытость: {self.satiety}, Стоимость: {self.cost} у.е.)"


class Cafeteria:
    def __init__(self, name: str, dishes: list[dict[str, Any]], money: float) -> None:
        self.name: str = name
        self.dishes: list[Dish] = [Dish(**dish) for dish in dishes]
        self.money: float = money

    def __str__(self) -> str:
        cafeteria_info: list[str] = [
            f"Столовая: {self.name} (Деньги: {self.money} у.е.)"
        ]

        dishes_info: list[str] = ["Блюда:"]
        dishes_info.extend(str(dish) for dish in self.dishes)

        cafeteria_info.extend(dishes_info)
        return "\n".join(cafeteria_info)


if __name__ == "__main__":
    # Инициализация данных о столовых
    cafeterias_data: list[dict[str, Any]] = [
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
    ]

    # Создание объектов столовых и вывод их информации
    for cafeteria_data in cafeterias_data:
        print(Cafeteria(**cafeteria_data))
