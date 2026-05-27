class Car:
    # для интереса я выложил файл на гитхаб 27 мая 2026 года, это мой первый файл
    def __init__(self, brand, country, year, condition):
        self.brand = brand
        self.country = country
        self.year = year
        self.condition = condition

    def start_engine(self, status):
        if status == 1:
            return "есть контакт"
        else:
            return "всё плохо"

    def car_conclusions(self, final):
        if final == 2:
            return "конфетка"
        elif final == 1:
            return "ещё поездит"
        else:
            return "ну пиздец"


class FireTruck(Car):

    # В __init__ мы просим всё то же самое + объем цистерны с водой
    def __init__(self, brand, country, year, condition, water_tank):
        # super() отправляет базовые свойства наверх в класс Car [Python]
        super().__init__(brand, country, year, condition)
        self.water_tank = water_tank


class PoliceHelicopter(Car):

    # В __init__ мы просим всё то же самое + объем цистерны с водой
    def __init__(self, brand, country, year, condition, man):
        # super() отправляет базовые свойства наверх в класс Car [Python]
        super().__init__(brand, country, year, condition)
        self.man = man


car1 = Car(brand="BMW", country="ФРГ", year=2020, condition="Новая")
car2 = Car(brand="Tesla", country="США", year=2023, condition="Использованная")
car3 = Car(brand="Жигули", country="СССР", year=1989, condition="Говно")

fire_car1 = FireTruck(
    brand="КамАЗ", country="РФ", year=2020, condition="почти новая", water_tank=500
)
fire_car2 = FireTruck(
    brand="ГАЗ", country="РФ", year=2019, condition="неновая", water_tank=400
)
fire_car3 = FireTruck(
    brand="Краз", country="РФ", year=2024, condition="Чуть новая", water_tank=200
)

helicopter1 = PoliceHelicopter(
    brand="Ми-8", country="РФ", year=2026, condition="только с завода", man=8
)
helicopter2 = PoliceHelicopter(
    brand="Робинсон-2", country="США", year=2016, condition="Б/у", man=2
)


print("Открываем сервис")
print("-" * 30)
print("Проверяем наличие")
print(" ")
print("Проверяем описание машин")
print(
    f"Машина 1: марка: {car1.brand}, страна: {car1.country}, год: {car1.year}, состояние: {car1.condition}"
)
print(
    f"Машина 2: марка: {car2.brand}, страна: {car2.country}, год: {car2.year}, состояние: {car2.condition}"
)
print(
    f"Машина 3: марка: {car3.brand}, страна: {car3.country}, год: {car3.year}, состояние: {car3.condition}"
)
print(" ")
print("Проверяем описание спецтехники")
print(
    f"Спецмашина 1: марка: {fire_car1.brand}, страна: {fire_car1.country}, год: {fire_car1.year}, состояние: {fire_car1.condition}, цистерна: {fire_car1.water_tank} л."
)
print(
    f"Спецмашина 2: марка: {fire_car2.brand}, страна: {fire_car2.country}, год: {fire_car2.year}, состояние: {fire_car2.condition}, цистерна: {fire_car2.water_tank} л."
)
print(
    f"Спецмашина 3: марка: {fire_car3.brand}, страна: {fire_car3.country}, год: {fire_car3.year}, состояние: {fire_car3.condition}, цистерна: {fire_car3.water_tank} л."
)
print(" ")
print("Проверяем описание вертолётов")
print(
    f"Вертолёт 1: марка: {helicopter1.brand}, страна: {helicopter1.country}, год: {helicopter1.year}, состояние: {helicopter1.condition}, людей помещается: {helicopter1.man}."
)
print(
    f"Вертолёт 2: марка: {helicopter2.brand}, страна: {helicopter2.country}, год: {helicopter2.year}, состояние: {helicopter2.condition}, людей помещается: {helicopter2.man}."
)
print(" ")
print("Проверяем мотор")
print(f"{car1.brand}: {car1.start_engine(1)}")
print(f"{car2.brand}: {car2.start_engine(1)}")
print(f"{car3.brand}: ёбаный в рот, опять {car3.start_engine(0)}")
print(" ")
print("Проверяем мотор спецтехники")
print(f"{fire_car1.brand}: {fire_car1.start_engine(1)} ")
print(f"{fire_car2.brand}: {fire_car2.start_engine(1)} ")
print(f"{fire_car3.brand}: опять {fire_car3.start_engine(0)}")
print(" ")
print("Проверяем мотор вертолетов")
print(f"{helicopter1.brand}: {helicopter1.start_engine(1)}")
print(f"{helicopter2.brand}: {helicopter2.start_engine(1)}")
print(" ")
print("Выводы по машинам")
print(f"моё мнение по {car1.brand}: {car1.car_conclusions(2)}")
print(f"моё мнение по {car2.brand}: {car2.car_conclusions(1)}")
print(f"моё мнение по {car3.brand}: {car3.car_conclusions(0)}")
print(" ")
print("Выводы по спецтехнике")
print(f"моё мнение по {fire_car1.brand}: {fire_car1.car_conclusions(1)}")
print(f"моё мнение по {fire_car2.brand}: {fire_car2.car_conclusions(2)}")
print(f"моё мнение по {fire_car3.brand}: {fire_car3.car_conclusions(0)}")
