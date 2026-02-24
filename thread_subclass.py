# Практическая работа №2 по Python на тему "Задание подкласса потока"
# Импортируем необходимые модули
import time      # Модуль для работы со временем и задержками
import os        # Модуль для работы с операционной системой (получение ID процесса)
from random import randint  # Функция для генерации случайных чисел
from threading import Thread # Класс Thread для создания потоков

# Создаем подкласс класса Thread
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        """Конструктор класса - инициализирует поток с именем и длительностью"""
        Thread.__init__(self)  # Вызываем конструктор родительского класса Thread
        self.name = name      # Сохраняем имя потока
        self.duration = duration  # Сохраняем длительность работы потока

    def run(self):
        """Основной метод потока - выполняется при запуске потока"""
        # Выводим сообщение о запуске потока с именем и ID процесса
        print("---> " + self.name + " running, belonging to process ID " + str(os.getpid()) + "\n")
        time.sleep(self.duration)  # Имитируем работу потока в течение случайного времени
        print("---> " + self.name + " over\n")  # Выводим сообщение о завершении потока

def main():
    """Главная функция программы"""
    start_time = time.time()  # Засекаем время начала выполнения программы
    
    # Создание 20 потоков вместо 9
    threads = []  # Список для хранения всех потоков
    
    # Создаем 20 потоков в цикле для более компактного кода
    for i in range(1, 21):  # Создаем потоки с номерами от 1 до 20
        thread = MyThreadClass("Thread#" + str(i), randint(1, 10))
        threads.append(thread)
    
    # Запуск всех потоков
    for thread in threads:
        thread.start()
    
    # Присоединение всех потоков (ожидание их завершения)
    for thread in threads:
        thread.join()
    
    # Конец программы
    print("End")
    
    # Время исполнения программы
    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()  # Вызываем главную функцию при запуске скрипта
