# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
WATER_ML_IN_LIT = 1000

# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Введите Ваше имя: ')
# TODO: Спроси возраст и сохрани в переменную user_age
user_age = int(input('Введите Ваш возраст: '))

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
user_weight = float(input('Введите Ваш вес: '))
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height
while True:
    try:
        user_height = input('Введите Ваш рост(в метрах, например 1.75): ')
        if '.' not in user_height:
            raise ValueError

        user_height = float(user_height)
        break
    except ValueError:
        print('Вы ввели рост не в том формате,попробуйте еще раз')

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
bmi = bmi = user_weight / (user_height ** 2)  # расчет имт
bmi = round(bmi, 1)
# TODO: Рассчитай water_needed
water_needed = user_weight * WATER_PER_KG  # Подсчет воды: вес * 30 мл
water_needed /= WATER_ML_IN_LIT  # перевод в литры

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print()
print(f'Отчет для пользователя {user_name} ({user_age} г)')
print(f'Ваш Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды {water_needed} л в день')
print('Расчет окончен. Будьте здоровы!')
