import datetime as dt

FORMAT = ('%H:%M:%S')  # Запишите формат полученного времени.
WEIGHT = 75  # Вес.
HEIGHT = 175  # Рост.
K_1 = 0.035  # Коэффициент для подсчета калорий.
K_2 = 0.029  # Коэффициент для подсчета калорий.
STEP_M = 0.65  # Длина шага в метрах.
storage_data = {}  # Словарь для хранения полученных данных.

def check_correct_data(data):  # Проверка корректности полученного пакета.
    # Если длина пакета отлична от 2
    # или один из элементов пакета имеет пустое значение -
    # функция вернет False, иначе - True.
    if (len(data) != 2) or (data[0] == None or data[1] == None):
        return False
    return True



def check_correct_time(time):  # Проверка корректности параметра времени.
    if storage_data == {}:  # Если пустой - сразу возвращаем True
        return True
    else:
        max_key = max(storage_data)  # Если не пустой - присваиваем перременной max наибольший ключ словаря
        if time <= max_key:  # Сравниваем с нашим времем
            return False
    # Если словарь для хранения не пустой
    # и значение времени, полученное в аргументе,
    # меньше самого большого ключа в словаре,
    # функция вернет False.
    # Иначе - True



def get_step_day(steps):  # Получить количество пройденных шагов за этот день.
    total_steps = 0
    for step in storage_data.values():
        total_steps += step
    return total_steps + steps  # Возвращаем общее кол-во шагов

    # Посчитайте все шаги, записанные в словарь storage_data,
    # прибавьте к ним значение из последнего пакета
    # и верните  эту сумму.



def get_distance(steps):  # Получить дистанцию пройденного пути в км.
    distance = round((steps * STEP_M / 1000), 2)
    return distance  # Возвращаем дистанцию в км.
    # Посчитайте дистанцию в километрах,
    # исходя из количества шагов и длины шага.



def get_spent_calories(dist, current_time):  # Получить значения потраченных калорий.
    time_list = current_time.split(':')
    hour = round(int(time_list[0]) + int(time_list[1]) / 60 + int(time_list[2]) / 3600,
                 2)  # Высчитываем из пакета количество часов и округляем до сотых
    mean_speed = round(dist / hour, 2)
    spent_calories = (K_1 * WEIGHT + (
                mean_speed ** 2 / HEIGHT) * K_2 * WEIGHT) * hour * 60  # Высчитываем калории по формуле из урока
    return round(spent_calories, 2)
    # В уроке «Строки» вы написали формулу расчета калорий.
    # Перенесите её сюда и верните результат расчётов.
    # Для расчётов вам потребуется значение времени;
    # получите его из объекта current_time;
    # переведите часы и минуты в часы, в значение типа float.



def get_achievement(dist):  # Получить поздравления за пройденную дистанцию.
    if dist >= 6.5:
        achievement = 'Отличный результат! Цель достигнута.'
    elif dist >= 3.9:
        achievement = 'Неплохо! День был продуктивным.'
    elif dist >= 2:
        achievement = 'Маловато, но завтра наверстаем!'
    else:
        achievement = 'Лежать тоже полезно. Главное — участие, а не победа!'

    return achievement
    # В уроке «Строки» вы описали логику
    # вывода сообщений о достижении в зависимости
    # от пройденной дистанции.
    # Перенесите этот код сюда и замените print() на return.



def show_message(pack_time, day_steps, dist, spent_calories, achievement):  # Выводим информацию на экран
    print(f'''
Время: {pack_time}.
Количество шагов за сегодня: {day_steps}.
Дистанция составила {dist} км.
Вы сожгли {spent_calories} ккал.
{achievement}
''')




def accept_package(data):  # Обработать пакет данных.

    if check_correct_data(data) is False:
        return 'Некорректный пакет'

    pack_time = dt.datetime.time(
        dt.datetime.strptime(data[0], FORMAT))  # Конвертируем строку со временем в пакете в <class 'datetime.time'>
    if check_correct_time(pack_time) is False:  # Если функция проверки значения времени вернет False
        return 'Некорректное значение времени'

    day_steps = get_step_day(data[1])  # Запишите результат подсчёта пройденных шагов.
    dist = get_distance(day_steps)  # Запишите результат расчёта пройденной дистанции.
    spent_calories = get_spent_calories(dist, data[0])  # Запишите результат расчёта сожжённых калорий.
    achievement = get_achievement(dist)  # Запишите выбранное мотивирующее сообщение.
    show_message(pack_time, day_steps, dist, spent_calories, achievement)
    storage_data[pack_time] = day_steps  # Добавляем в словарь новую пару ключ-значение
    return storage_data

    # Данные для самопроверки.Не удаляйте их.
package_0 = ('2:00:01', 506)
package_1 = (None, 3211)
package_2 = ('9:36:02', 15000)
package_3 = ('9:36:02', 9000)
package_4 = ('8:01:02', 7600)

accept_package(package_0)
accept_package(package_1)
accept_package(package_2)
accept_package(package_3)
accept_package(package_4)


