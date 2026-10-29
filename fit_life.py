# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30
WATER_ML_IN_LIT = 1000


def convert_to_float(value):
    """Function replace ',' with '.'"""
    return float(value.replace(',', '.'))


if __name__ == '__main__':

    user_name = input('Введите Ваше имя: ')
    user_age = int(input('Введите количество полных лет: '))
    user_weight = convert_to_float(input('Введите Ваш вес: '))
    user_height = convert_to_float(input('Введите Ваш рост (например 1.75): '))

    bmi = bmi = user_weight / (user_height ** 2)  # расчет имт
    bmi = round(bmi, 1)
    water_needed = user_weight * WATER_PER_KG  # Подсчет воды: вес * 30 мл
    water_needed /= WATER_ML_IN_LIT  # перевод в литры

    print(
        f'\nОтчет для пользователя {user_name} ({user_age} г)\n'
        f'Ваш Индекс Массы Тела: {bmi}\n'
        f'Рекомендуемая норма воды {water_needed} л в день\n'
        f'Расчет окончен. Будьте здоровы!\n',
    )
