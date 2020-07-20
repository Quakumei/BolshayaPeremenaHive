# -*- coding: UTF-8 -*-

import time

#  _
# / |
# | |
# |_|
#

def calc_possibility(cargo_weight,
             cargo_length,
             cargo_width,
             drone_capacity,
             drone_length,
             drone_width,
                     N2):
    """
    Определяет возможность поднять груз определнным типом дронов
    N2 -- количество зацепов на грузе
    N1 -- необходимое количество дронов для подъёма

    """
    global N1
    N1 = 2 + cargo_weight/drone_capacity
    return N2>N1


def send_error(error_msg):
    """
    Отправляет сообщение error_msg об ошибке оператору

    """
    print(error_msg)


def go_charge():
    """
    Отправляет дрона на подзарядку

    """
    time.sleep(6)
    print("Дрон заряжен, можно лететь.")


def check_db(login_data):
    """
    Проверка наличия в базе данных недоставленных грузов,
    получение информации о грузе.

    """
    print("Проверка наличия недоставленных грузов...")
    time.sleep(5)
    print("Получены сведения о доставке!")
    address = "г. Ярославль, ул. Зелинского, д.6"
    cargo_id = 42
    cargo_weight = 15 #в кг
    cargo_length = 150 #в см
    cargo_width = 50 #в см
    N2 = 8 #n креплений
    return address, cargo_id, cargo_weight, cargo_length, cargo_width, N2

#  ___
# |_  )
#  / /
# /___|
#

def calc_distance(point_index, cargo_id):
    """
    Расчёт расстояни от дрона до точки с номером point_index груза cargo_id

    """
    return point_index * 15


def cargo_ready_to_go(N1, i):
    """
    Проверка готовности груза к перевозке (N1>=i)

    """
    if N1 >= i:
        return False
    return True


#Магия для демонстрации
global index
index = 1

def tell_point_index(point_index ,cargo_id):
    """
    Сообщение дронам текущей точки крепления груза
    если точка крепления груза, сообщеная другим дроном
    меньше, чем та, что хранится у дрона, дрон ставит себе
    новое значение индекса точки и рассчитывает уже расстояние до неё

    """
    pass


def listen_for_point_index(cargo_id):
    """
    Ждать сообщения от других дронов об индексе
    Возвращает индекс следующей точки крепления.
    Возвращает 0, если точек больше нет, груз укомплектован.

    """
    global index
    index += 1
    if index == 13:
        index = 1
    return index


def tell_distance(cargo_id):
    """
    Сообщить дронам поблизости о расстоянии до точки i

    """
    pass


def listen_for_distances(cargo_id):
    """
    Ждать сообщений tell_distance() от других дронов о расстоянии
    до текущей точки i

    возвращает массив расстояний

    """
    return [200, 300, 60]


def bind_to_point(point_index, cargo_id):
    """
    Прикрепиться к креплению point_index груза cargo_id

    """
    pass


def send_point_closed(point_index, cargo_id):
    """
    Сообщить дронам вокруг о занятии точки point_index груза cargo_id

    """
    pass

global drone_id

def solve_bind_conflict(cargo_id):
    """
    Решает проблему нескольких дронов, находящихся на одной дистанции от груза

    Принцип:
        1) У каждого дрона есть уникальный id
        2) У кого id больше тот и крепится
    """
    #Два параллельных процесса
    global drone_id #id этого дрона
    ids = listen_for_id(cargo_id)
    ids.append(drone_id)
    if ids.sort()[-1] == drone_id:
        return True
    return False



#  ____
# |__ /
#  |_ \
# |___/
#


## Маршрут
#route - специальный тип данных - точки на карте до которых летит дрон (координаты)
# Например следующий массив - route
# [(1,2),(2,3),(10,10)]
# Последовательность точек на карте по которым полетит дрон

def tell_route(route):
    """
    Говорит ближайшим дронам о своём маршруте

    """
    pass


def sync_route():
    """
    Собирает информацию о маршрутах построенных ближайшими дронами и возвращает кратчайший

    """
    route = [(1, 1), (1, 125), (125, 125), (125, 255), (255, 255)]
    time.sleep(3)
    return route


def build_route(route):
    """
    Построить маршрут до адреса

    """
    route = [(1, 1), (1, 125), (125, 125), (125, 255), (255, 255)]
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


def send_sos(N4):
    """
    Отправление сигнала команде спасателей

    """
    pass

def slow_down(engine_state):
    """
    Замедляет полёт с сохранением направления

    """
    return engine_state


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

        if everything_ok():
            send_ok_signal() # Нормальное функционирование
        else:
            #сюда попадут сломавшиеся дроны
            pass

        #Проверка соседей
        N3 = nearby_drones_ok_count()
        global N1
        if N1-1 > N3:
            send_sos(N1-N3)
            not_okay_flag = True

        #Корректировка направления движения
        engine_state = calculate_formation_correction(calculate_engines(target), drone_distances, obstacles, location)

        #Замедление если что то пошло нет так
        if not_okay_flag:
            engine_state = slow_down(engine_state)

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

#  _ _
# | | |
# |_  _|
#   |_|
#

def reverse_route(route):
    """
    Возвращает обратный маршрут

    """
    return route[::-1]

def tell_cargo_state(state, login_data, cargo_id):
    """
    Сообщить базе данных о изменении статуса груза

    """
    pass




#             _        _
#  _ __  __ _(_)_ _   | |___  ___ _ __
# | '  \/ _` | | ' \  | / _ \/ _ \ '_ \
# |_|_|_\__,_|_|_||_| |_\___/\___/ .__/
#                                |_|
#


def loop():
    """
    Главный цикл работы дрона
    Смотреть схему.

    """

#      _
#     / |
#     | | Стадия 1 - Получение сведений и проверка возможностей
#     |_|
#

    #Характеристики дрона
    drone_capacity, drone_length, drone_width = 5, 50, 50
    global drone_id
    drone_id = 777 #Уникальный идентификатор для разрешения конфликтов

    #Проверка уровня зарядки
    energy_level = 100
    if energy_level <= 95:
        send_error("Дрон разряжен, лечу на подзарядку...")
        go_charge()
        energy_level = 100
    print("Дрон заряжен, можно лететь.")


    #Получение данных о грузе
    print("Получаю данные о грузе...")
    time.sleep(3)
    address, cargo_id, cargo_weight, cargo_length, cargo_width, N2 = check_db("login:pass@database.com")
    print("Задание получено. Проверяю возможность выполнения...")

    #Проверка возможности доставки груза
    if not calc_possibility(cargo_weight,
                            cargo_length,
                            cargo_width,
                            drone_capacity,
                            drone_length,
                            drone_width,
                            N2):
        send_error("Невозможно доставить груз. Меняю статус груза...")
        tell_cargo_state("Ждёт курьера", "login:pass@address.com", cargo_id)
        loop()
    else:
        print("Груз удовлетворяет возможностям дронов. Начинаю крепление!")


#    ___
#   |_  )
#    / /  Стадия 2 - Крепление дрона к грузу
#   /___|
#

    global N1
    binded = False
    point_index = listen_for_point_index(cargo_id)


    while (not cargo_ready_to_go(N1, point_index)) and not binded:
        point_index = listen_for_point_index(cargo_id)
        point_distance = calc_distance(point_index, cargo_id)

        tell_distance(point_distance)
        distances = listen_for_distances(cargo_id) #По идее процесс прослушивания расстояний должен быть асинхронным
        distances.sort()

        if point_distance > distances[0]:
            going_to_bind = False #Является не ближайшим
        elif point_distance == distances[0]:
            going_to_bind = solve_bind_conflict(cargo_id)
        else:
            going_to_bind = True

        if going_to_bind:
            print("Я ближе всех к точке " + str(point_index) + "! Прикрепляюсь...")
            time.sleep(3)
            bind_to_point(point_index, cargo_id)
            print("Прикрепился к грузу.")

            point_index += 1
            binded = True

        tell_point_index(point_index, cargo_id)
        time.sleep(3) #Задержка, чтобы дроны приняли новое значение

    if binded:
        while not cargo_ready_to_go(N1, listen_for_point_index(cargo_id)):
            print("Ожидание дронов для перевозки...")
            time.sleep(2)
    else:
        print("На грузе уже максимальное количество дронов... Меняю задание")
        loop()

    #Cюда попадают дроны которые приклеились и собираются лететь
    print("Все необходимые дроны сели, начинаю процесс доставки")
    time.sleep(3)
    tell_cargo_state("Доставляется...", "login:pass@database.com", cargo_id)


#    ____
#   |__ /
#    |_ \  Стадия 3 - Полёт к адресу
#   |___/
#

    # Определение с маршрутом
    print("Определяю маршрут...")
    route = build_route(address)
    tell_route(route)
    best_route = sync_route()
    if best_route != route:
        route = best_route

    #Сигналы готвности
    print("Готов к полёту, жду сигналов готовности дронов")
    tell_ready()
    wait_for_readies(N1-1)

    #Лечу по маршруту
    print("Все дроны готовы, начинаем полёт...")
    fly(best_route)
    print("Я долетел до " + address + "!")


#     _ _
#    | | |
#    |_  _|  Стадия 4 - Сброс груза и возвращение домой
#      |_|
#
#

    drop_cargo()
    tell_cargo_state("Доставлен!", "login:pass@database.com", cargo_id)
    print("Груз успешно доставлен! Возвращаюсь на базу...")
    fly(reverse_route(best_route)) # вернуться домой по обратному маршруту

    loop()

if __name__ == "__main__":
    while 1:
        loop()

