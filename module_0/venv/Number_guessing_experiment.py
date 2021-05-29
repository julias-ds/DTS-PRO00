import numpy as np

def get_guess_tries(guessed_number):
    '''Функция принимает загаданное число, отгадывает его
    и возвращает число попыток'''

    '''Заводим переменные для хранения максимума и минимума наших чисел-отгадок,
       и количества попыток'''
    try_count = 1
    predict_max = 100
    predict_min = 1

    '''Устанавливаем любое random число, с которого начнем отгадывать'''
    predict = np.random.randint(1,101)

    while guessed_number != predict:
        try_count += 1

        '''Переопределяем максимум и минимум интервала'''
        if guessed_number > predict:
            predict_min = predict
        elif guessed_number < predict:
            predict_max = predict

        ''''Вычисляем новое число-попытку как середину интервала'''
        predict = round(predict_max + predict_min) / 2

        '''Возвращаем количество попыток'''
    return(try_count) # выход из цикла, если угадали

def check_predict_algorithm():
    '''Функция запускает игру 1000 раз и выводит среднее количество
    попыток, за которые алгоритм угадывает число'''

    '''Заводим список для хранения количества попыток в экспериментах'''
    experiment_tries_list = []

    '''Создаем массив из 1000 случайных чисел от 1 до 100'''
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    guessed_numbers_array = np.random.randint(1, 101, size=(1000))

    '''Проводим эксперимент и записываем количество попыток'''
    for number in guessed_numbers_array:
        experiment_tries_list.append(get_guess_tries(number))

    '''Вычисляем медиану попыток всех экспериментов'''
    mean_tries = int(np.mean(experiment_tries_list))

    print(f"Ваш алгоритм угадывает число в среднем за {mean_tries} попыток")

    '''Возвращаем медианное количество попыток'''
    return (mean_tries)


# запускаем проверку алгоритма
check_predict_algorithm()