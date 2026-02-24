# Практическая работа №1 по Python на тему "Разработка программы с использованием потоков данных"
# Импортируем необходимые модули
import threading  # Модуль для работы с потоками
import time        # Модуль для работы со временем

# Функция my_func из методички - принимает номер потока и выводит сообщение
def my_func(thread_number):
    """Функция, которая выводит сообщение о том, какой поток ее вызвал"""
    print(f"my_func called by thread N°{thread_number}")

# Основные функции для демонстрации работы потоков
def function_A():
    """Функция A - демонстрирует базовую работу потока"""
    print(f"Имя текущего потока: {threading.current_thread().name}")
    print("--> starting function_A")
    time.sleep(2)  # Имитация работы в течение 2 секунд
    print("--> exiting function_A")

def function_B():
    """Функция B - демонстрирует базовую работу потока"""
    print(f"Имя текущего потока: {threading.current_thread().name}")
    print("--> starting function_B")
    time.sleep(2)  # Имитация работы в течение 2 секунд
    print("--> exiting function_B")

def function_C():
    """Функция C - демонстрирует базовую работу потока"""
    print(f"Имя текущего потока: {threading.current_thread().name}")
    print("--> starting function_C")
    time.sleep(2)  # Имитация работы в течение 2 секунд
    print("--> exiting function_C")

# Дополнительные функции с арифметическими вычислениями
def function_add():
    """Функция сложения - складывает два числа и выводит результат"""
    print(f"Имя текущего потока: {threading.current_thread().name}")
    print("--> starting function_add")
    a = 15  # Первое число
    b = 7   # Второе число
    result = a + b  # Складываем числа
    print(f"Результат сложения {a} + {b} = {result}")
    print("--> exiting function_add")

def function_multiply():
    """Функция умножения - умножает два числа и выводит результат"""
    print(f"Имя текущего потока: {threading.current_thread().name}")
    print("--> starting function_multiply")
    a = 8   # Первое число
    b = 9   # Второе число
    result = a * b  # Умножаем числа
    print(f"Результат умножения {a} * {b} = {result}")
    print("--> exiting function_multiply")

# Основная часть программы
if __name__ == "__main__":
    print("=== Начало выполнения программы с потоками ===")
    
    # Создаем 5 потоков с функцией my_func для демонстрации передачи номера
    threads_my_func = []
    for i in range(1, 6):  # Создаем потоки с номерами от 1 до 5
        thread = threading.Thread(target=my_func, args=(i,))
        threads_my_func.append(thread)
    
    # Создаем 5 потоков с именами для разных функций
    threads_functions = []
    
    # Поток для функции A
    thread_A = threading.Thread(target=function_A, name="Поток-A")
    threads_functions.append(thread_A)
    
    # Поток для функции B
    thread_B = threading.Thread(target=function_B, name="Поток-B")
    threads_functions.append(thread_B)
    
    # Поток для функции C
    thread_C = threading.Thread(target=function_C, name="Поток-C")
    threads_functions.append(thread_C)
    
    # Поток для функции сложения
    thread_add = threading.Thread(target=function_add, name="Поток-Сложение")
    threads_functions.append(thread_add)
    
    # Поток для функции умножения
    thread_multiply = threading.Thread(target=function_multiply, name="Поток-Умножение")
    threads_functions.append(thread_multiply)
    
    print("\n--- Запуск потоков my_func ---")
    # Запускаем все потоки с my_func
    for thread in threads_my_func:
        thread.start()
    
    print("\n--- Запуск потоков с именами ---")
    # Запускаем все потоки с именами
    for thread in threads_functions:
        thread.start()
    
    print("\n--- Ожидание завершения потоков my_func ---")
    # Ожидаем завершения всех потоков my_func
    for thread in threads_my_func:
        thread.join()
    
    print("\n--- Ожидание завершения потоков с именами ---")
    # Ожидаем завершения всех потоков с именами
    for thread in threads_functions:
        thread.join()
    
    print("\n=== Все потоки завершены. Программа закончила работу ===")
