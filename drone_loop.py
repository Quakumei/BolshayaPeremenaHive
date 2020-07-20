# -*- coding: UTF-8 -*-
# encoding declaration

import sys
import time


def calc_possibility(cargo_weight,
             cargo_length,
             cargo_width,
             drone_capacity,
             drone_length,
             drone_width,
                     N2):
    # Определяет возможность поднять груз определнным типом дронов

    # UAV count for lifting the cargo
    N1 = 2 + cargo_weight/drone_capacity
    # Placement opportunity calc
#    if cargo_width/drone_width>1:
#        N2 = (cargo_width/drone_width) * (cargo_length/drone_length)
#    else:
#        N2 = cargo_length/drone_length
#
    return N2>N1

def send_error(error_msg):
    print(error_msg)
    return

def go_charge():
    #Отправляет на ближайшую зарядку до полной подзарядки
    time.sleep(6)
    print("Дрон заряжен, можно лететь.")
    pass

def check_db(login_data):
    print("Проверка наличия недоставленных грузов...")
    time.sleep(5)
    print("Получены сведения о доставке!")
    address = "г. Ярославль, ул. Зелинского, д.6"
    cargo_id = 42
    cargo_weight = 15 #в кг
    cargo_length = 150 #в см
    cargo_width = 50 #в см
    N2 = 8 # n креплений
    return address, cargo_id, cargo_weight, cargo_length, cargo_width, N2

#global tick
#tick = 0

# def get_free_points():
    #Сигнал остальным дронам, просьба сообщить о свободных местах крепления
#    global tick
#    tick +=1
#    return [1,3,4][:-tick]

def calc_distance(point_index, cargo_id):
    #Расчёт расстояния в см до крепления point_index груза с уникальным идентификатором cargo_id
    return point_index[0] * 30

def cargo_ready_to_go(free_points):
    #Возвращает да, если свободных точек нет.
    if free_points == []:
        return True
    else:
        return False

def tell_others(dist,point):
    #Сообщает дронам вокруг дистанцию до точки крепления
    pass

def get_swarm_closest_dist(point, cargo_id):
    #В течении некоторого времени собирает сообщения tell_others от других дронов
    #И выдаёт минимальное расстояние среди услышанных к точке point
    time.sleep(3)
    return 500


def tell_route(route):
    #Говорит ближайшем дронам о своём маршруте
    pass

def sync_route():
    #Собирает информацию о маршрутах построенных ближайшими дронами и возвращает кратчайший
    route = [(1,1),(1,125),(125,125),(125,255),(255,255)] #route - специальный тип данных - точки на карте до которых летит дрон (координаты)
    time.sleep(3)
    return route

def build_route(route):
    #Строит маршрут до адреса
    route = [(1, 1), (1, 125), (125, 125), (125, 255), (255, 255)] #route - специальный тип данных - точки на карте до которых летит дрон (координаты)
    return route

def calculate_engines(target):
    #Счиатает необходимые значения активности пропеллеров? чтобы лететь в правильную сторону
    return [10, 10, 10]

def calculate_formation_correction(engine_state, drone_distances, obstacles, location):
    #Считает необходимые значения активности пропеллеров? + корректировка на расстояние до дронов и облет препятствий
    return [5, 20, 20]

def get_drone_distances():
    #Считывает данные с устройств для определения расстояния до дронов и возвращает их
    return [2, 5, 5]

def get_obstacles():
    #Считывает данные с устройств для определения расстояния и говорит о препятствиях (близких объектах)
    return 1

def get_gps_location():
    #Считывает данные с gps трекера для ориентирования на местности
    return 42

def fly_to(target):
    #Лететь в сторону точки на карте до её достижения с учётом препятствий + коррекция
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
    #Метод осуществляющий передвижение дрона в соответствии с маршрутом, препятствиями и другими дронами
    for target in route:
        print("Лечу до ["+ str(target[0]) + ", " + str(target[1]) + "]...")
        fly_to(target)

def bind_to_point(point):
    #Метод для прикрепления к точке дрона
    pass

def send_point_closed(point):
    #Сказать другим дронам о закрытии точки
    pass

def drop_cargo():
    #Отпустить точку крепления
    pass

def reverse_route(route):
    #Возвращает обратный маршрут
    return route[::-1]

def tell_cargo_state(state, login_data, cargo_id):
    #Сообщить базе данных о изменении статуса груза
    pass

global tick
tick = 0

def listen_for_point_index(cargo_id):
    global tick
    tick+=1
    if tick >= 4:
        return []
    return [tick]

def loop():
    ##Стадия 1 - проверка готовности к полёту \ возможности доставки

    #Характеристики дрона
    drone_capacity, drone_length, drone_width = 5, 50, 50

    #Проверка уровня зарядки
    energy_level = 100
    if energy_level <= 95:
        send_error("Дрон разряжен, летит на подзарядку...")
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


   ##Стадия 2 - Крепление к грузу

    #Пока не прицепилось достаточно дронов
    i_am_binded = False
#   free_points = get_free_points()
    while not (cargo_ready_to_go(listen_for_point_index(cargo_id)) or i_am_binded):

        #print("Вычисляю расстояние до ближайшего крепления...")

      #  free_points = get_free_points()
       # dist_min = 99999999 #Большое число, больше каждого расстояния
        #closest_point_index = -1

        #Рассчет ближайшейшего места крепления *относительно дрона* и расстояния до него
        #for point_index in free_points:
         #   dist = calc_distance(point_index, cargo_id)
          #  if dist_min > dist:
           #     dist_min = dist
            #    closest_point_index = point_index

        #Сказать другим
       # print("Сравниваю своё расстояние с другими...")

  #      tell_others(dist_min, closest_point_index) #Отправляет информацию рою о ближайшем месте крепления
 #       closest_dist = get_swarm_closest_dist(closest_point_index) #В течении некоторого времени этот метод собирает информацию с tell_others() других дронов

        point_index = listen_for_point_index(cargo_id) #Получить текущую точку крепления
        point_distance = calc_distance(point_index, cargo_id)
        closest_dist = get_swarm_closest_dist(point_index, cargo_id)



        if closest_dist >= point_distance: #Если минимальное расстояние совпадает с тем что посчитал сам дрон, то значит что он является и ближе всех.

            print("Я ближе всех! Прикрепляюсь...")

            bind_to_point(point_index) # Присоединиться к креплению
            send_point_closed(point_index) # Сказать другим дронам, что крепление успешно занято
            i_am_binded = True
            time.sleep(2)

            print("Я прикреплён к грузу.")
        #Если дрон не прикрепился, то с изменением информации о занятых точках, изменится и информация которую он отдаёт другим дронам,
        #начинается новый цикл и он имеет возможность присоединиться к грузу.


    #TO-DO get_free_points() выдаёт одно и то же значение --> никогда не полетит
    if i_am_binded: #Подождать пока другие дроны присоединятся к грузу
        while not cargo_ready_to_go(listen_for_point_index(cargo_id)):
            print("Жду прикрепления других дронов...")
            time.sleep(5)
    else:
        print("Груз улетел, ищу другой...")
        #сюда попадут только те дроны, что не присоединились, когда груз уже полетел
        loop() #начать новую итерацию цикла

    time.sleep(2)


    ## Стадия 3 - Перелёт к адресу
    # псевдометоды
    # route - отдельный тип данных представляющий маршрут (содержит массив пар точек-координат на карте)
    # build_route(address) - построить маршрут
    # tell_route(route) - та же штука что и с tell_others
    # sync_route(address) - выбрать кратчайший на основе построений ближайших дронов
    # fly(route) - полететь по заданному маршруту, луп в котором он постоянно чекает дистанцию до других дронов и обстаклов

    tell_cargo_state("Доставляется...", "login:pass@database.com", cargo_id)
    #Определяюсь с маршрутом
    route = build_route(address)
    tell_route(route)
    best_route = sync_route()
    if best_route != route:
        route = best_route

    #Лечу по маршруту
    fly(best_route)
    print("Я долетел до " + address + "!")


    ## Стадия 4 - Сброс груза и возвращение домой
    drop_cargo()
    tell_cargo_state("Доставлен!", "login:pass@database.com", cargo_id)
    print("Груз успешно доставлен! Возвращаюсь на базу...")
    fly(reverse_route(best_route)) # вернуться домой по обратному маршруту

    loop()

if __name__ == "__main__":
    while 1:
        loop()

