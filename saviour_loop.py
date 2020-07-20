# -*- coding: UTF-8 -*-

import time


global TICK
TICK = 1
def wait_for_sos():
    """
    Ожидание сигнала СОС

    """
    global TICK
    TICK += 1
    time.sleep(3)
    if TICK % 3 == 0:
        return True
    return False


def get_info():
    """
    Получение данных от сигнала СОС

    """
    location = (125, 125) #Точка на карте - место происшествия
    N4 = 1
    return location, N4


def go_charge():
    """
    Отправляет дрона на подзарядку

    """
    time.sleep(6)


def send_error(error_msg):
    """
    Отправляет сообщение error_msg об ошибке оператору

    """
    print(error_msg)


def tell_route(route):
    """
    Говорит ближайшим дронам о своём маршруте
    """
    pass


def sync_route():
    """
    Собирает информацию о маршрутах построенных ближайшими дронами и возвращает кратчайший
    """
    route = [(1, 1), (1, 125), (125, 125)]
    time.sleep(3)
    return route


def build_route(address):
    """
    Построить маршрут до адреса
    """
    route = [(1, 1), (1, 125), (125, 125)]
    return route


## Сигналы готовности

def tell_ready():
    """
    Подать сигнал готовности ближайшим дронам
    """
    pass


def wait_for_readies(n):
    """
    Подождать n сигналов готовности
    """
    time.sleep(n)
    pass

## Управление полётом


def calculate_engines(target):
    """
    Счиатает необходимые значения активности пропеллеров? чтобы лететь в правильную сторону
    """
    return [10, 10, 10]


def calculate_formation_correction(engine_state, drone_distances, obstacles, location):
    """
    Считает необходимые значения активности пропеллеров? + корректировка на расстояние до дронов и облет препятствий
    """
    return [5, 20, 20]


def get_drone_distances():
    """
    Считывает данные с устройств для определения расстояния до дронов и возвращает их
    """
    return [2, 5, 5]


def get_obstacles():
    """
    Считывает данные с устройств для определения расстояния и говорит о препятствиях (близких объектах)
    """
    return 1


def get_gps_location():
    """
    Считывает данные с gps трекера для ориентирования на местности
    """
    return 42

def everything_ok():
    """
    Определяет отсутствие неполадок
    """
    if 1:
        return True
    else:
        return False


def send_ok_signal():
    """
    Отправляет сигнал соседним дронам о исправной работе
    """
    pass


def nearby_drones_ok_count():
    """
    Сбор сигналов о исправной работе дронов, подсчет соседей
    """
    return 8


def fly_to(target):
    """
    Лететь в сторону точки на карте до её достижения с учётом препятствий + коррекция
    """
    not_okay_flag = False
    while 1:
        # Псевдокодная магия для полёта и его корректировки

        #Сбор информации с датчиков
        location = get_gps_location()
        drone_distances = get_drone_distances()
        obstacles = get_obstacles()

        #Корректировка направления движения
        engine_state = calculate_formation_correction(calculate_engines(target), drone_distances, obstacles, location)
        time.sleep(4)
        break


def fly(route):
    """
    Метод осуществляющий передвижение дрона в соответствии с маршрутом, препятствиями и другими дронами
    """
    for target in route:
        print("Лечу до ["+ str(target[0]) + ", " + str(target[1]) + "]...")
        fly_to(target)


def drop_cargo():
    """
    Отпустить точку крепления
    """
    pass

def attach_to_dead():
    """
    Спрашивает на каких позициях находятся выбывшие из строя дроны
    и присоединяется к одной из них, отправляя сигнал о том, что
    точка теперь работает

    """
    pass

def loop():
    """
    Основной цикл работы

    """

    #Проверка уровня зарядки
    energy_level = 100
    if energy_level <= 95:
        send_error("Дрон разряжен, лечу на подзарядку...")
        go_charge()
        energy_level = 100
    print("Дрон заряжен, можно лететь.")


    #Проверка наличия сигналов СОС
    while not wait_for_sos():
        print("Ожидание сигнала аварии...")


    location, N4 = get_info()
    print("Получен сигнал аварии, вылетаю")

    # Определение с маршрутом
    print("Определяю маршрут...")
    route = build_route(location)
    tell_route(route)
    best_route = sync_route()
    if best_route != route:
        route = best_route

    #Сигналы готвности
    print("Готов к полёту, жду сигналов готовности дронов")
    tell_ready()
    wait_for_readies(N4-1)

    #Лечу по маршруту
    print("Все дроны готовы, начинаем полёт...")
    fly(best_route)
    print("Я долетел до [" + str(location[0]) + ", " + str(location[1])+ "]!")

    attach_to_dead() #Присоединиться к выбывшему из строя дрону
    print("Присоединился к грузу...")
    route = sync_route() #Перенять маршрут у соседних дронов
    fly(route)
    drop_cargo()
    print("Груз успешно доставлен! Возвращаюсь домой...")
    fly([(125, 125), (1, 1)]) #Возвращение в док

    loop()

if __name__ == "__main__":
    loop()
