'''''
# Базовый класс Media
class Media:
    # Метод для воспроизведения медиа
    def play(self):
        return "Playing media"  # Возвращает стандартную строку для воспроизведения медиа
    
    # Метод для паузы медиа
    def pause(self):
        return "Pausing media"  # Возвращает строку для паузы медиа


# Подкласс Music, который наследует от Media
class Music(Media):
    # Переопределенный метод play для музыки
    def play(self):
        return "Playing music track"  # Возвращает строку для воспроизведения музыкального трека


# Подкласс Video, который наследует от Media
class Video(Media):
    # Переопределенный метод play для видео
    def play(self):
        return "Playing video file"  # Возвращает строку для воспроизведения видеофайла


# Пример использования классов
media = Media()  # Создание объекта базового класса Media
music = Music()  # Создание объекта подкласса Music
video = Video()  # Создание объекта подкласса Video

# Вызов метода play для каждого объекта и вывод результата
print(media.play())  # "Playing media" - для объекта Media
print(music.play())  # "Playing music track" - для объекта Music
print(video.play())  # "Playing video file" - для объекта Video

# Вызов метода pause для каждого объекта и вывод результата
print(media.pause())  # "Pausing media" - для объекта Media
print(music.pause())  # "Pausing media" - для объекта Music (метод не переопределен)
print(video.pause())  # "Pausing media" - для объекта Video (метод не переопределен)
'''''

'''''
class BankAccount:
    # Конструктор для инициализации счета с начальным балансом
    def __init__(self, initial_balance=0):
        # Приватное поле для хранения баланса счета
        self.__balance = initial_balance  # Устанавливаем начальный баланс

    # Метод для пополнения счета
    def deposit(self, amount):
        if amount > 0:
            # Увеличиваем баланс на сумму пополнения
            self.__balance += amount  # Обновляем баланс
            print(f"Deposited: {amount}. Current balance: {self.__balance}")
        else:
            # Выводим ошибку, если сумма пополнения неверна
            print("Deposit amount must be greater than zero.")

    # Метод для снятия средств с счета
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                # Уменьшаем баланс на сумму снятия
                self.__balance -= amount  # Обновляем баланс
                print(f"Withdrew: {amount}. Current balance: {self.__balance}")
            else:
                # Выводим ошибку, если на счете недостаточно средств
                print("Error: Insufficient funds.")
        else:
            # Выводим ошибку, если сумма снятия неверна
            print("Withdrawal amount must be greater than zero.")

    # Метод для получения текущего баланса счета
    def get_balance(self):
        # Возвращаем текущий баланс
        return self.__balance

# Пример использования
account = BankAccount(100)  # Создаем счет с начальным балансом 100

account.deposit(50)   # Пополняем счет на 50
account.withdraw(30)  # Снимаем 30
account.withdraw(200) # Пытаемся снять больше, чем на счете

# Выводим финальный баланс
print(f"Final balance: {account.get_balance()}")  # Показываем текущий баланс счета
'''''

'''''
from abc import ABC, abstractmethod  # Импортируем базовый класс и декоратор для абстрактных методов

# Абстрактный класс Worker, который наследует от ABC (Abstract Base Class)
class Worker(ABC):
    # Абстрактный метод work, который обязаны реализовать все подклассы
    @abstractmethod
    def work(self):
        pass  # Метод, который описывает, как работник выполняет свою работу

    # Абстрактный метод rest, который обязаны реализовать все подклассы
    @abstractmethod
    def rest(self):
        pass  # Метод, который описывает, как работник отдыхает


# Подкласс Programmer, реализующий методы абстрактного класса Worker
class Programmer(Worker):
    # Реализация метода work для программиста
    def work(self):
        return "Programming code"  # Программист выполняет работу, программируя код

    # Реализация метода rest для программиста
    def rest(self):
        return "Taking a coffee break"  # Программист отдыхает, делая перерыв на кофе


# Подкласс Designer, реализующий методы абстрактного класса Worker
class Designer(Worker):
    # Реализация метода work для дизайнера
    def work(self):
        return "Designing graphics"  # Дизайнер выполняет работу, создавая графику

    # Реализация метода rest для дизайнера
    def rest(self):
        return "Resting with music"  # Дизайнер отдыхает, слушая музыку


# Пример использования
programmer = Programmer()  # Создаем объект программиста
designer = Designer()  # Создаем объект дизайнера

# Вызов методов work и rest для каждого объекта и вывод результата
print(programmer.work())  # "Programming code"
print(programmer.rest())  # "Taking a coffee break"

print(designer.work())  # "Designing graphics"
print(designer.rest())  # "Resting with music"
'''''