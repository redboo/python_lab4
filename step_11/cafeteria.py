class Dish:
    def __init__(self, name, satiety, cost):
        self.name = name
        self.satiety = satiety
        self.cost = cost

    def __str__(self):
        return f"{self.name} (Сытость: {self.satiety}, Стоимость: {self.cost} у.е.)"


class Cafeteria:
    def __init__(self, name, dishes, money):
        self.name = name
        self.dishes = [Dish(**dish) for dish in dishes]
        self.money = money

    def __str__(self):
        cafeteria_info = [f"Столовая: {self.name} (Деньги: {self.money} у.е.)"]

        dishes_info = ["Блюда:"]
        dishes_info.extend(str(dish) for dish in self.dishes)

        cafeteria_info.extend(dishes_info)
        return "\n".join(cafeteria_info)
