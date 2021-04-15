# импортируем модуль
import timeit

# создан класс Timing
class Timing:

    # принимаем декорируемую фунцию file_name
    def __init__(self, file_name):

        # запускаем декорируемую фунцию file_name
        self.file_name = file_name()

        # определяем имя файла
        self.name = self.file_name[0]

        # определяем кол-во повторений кода
        self.repeat = self.file_name[1]

        # запуск контекстного менеджера
        with self:
            pass

    # начало работы контекстного менеджера
    def __enter__(self):

        # открывем файл с именем, полученым из фунции file_name
        self.file = open(self.name, 'r')

        # итарируем файл self.file и переобразуем в код
        self.code_test = ''.join([string for string in self.file])

        # используя timeit.repeat, фиксируем время выполнения кода, производим расчет среднего времени выполнения
        # repeat кол-во прогонов кода
        self.timeming = sum(timeit.repeat(self.code_test, repeat=self.repeat)) / self.repeat

        # вывод результата
        print(f'Среднее время выполнения кода при {self.repeat} запуске:{self.timeming:.5f}')

    # окончание работы контекстного менеджера
    def __exit__(self, exc_type, exc_val, exc_tb):

        # закрываем файл с именем, полученым из фунции file_name
        self.file.close()

# использование класса Timing как декоратора
@Timing
# фунция запроса имени файла
def file_name():

    # запрос имени тестируемого файла
    name = input('Введите название тестируемого файла: ')

    # запрос кол-ва повторений
    repeat = int(input('Введите кол-во повторений: '))

    # объединяем запрашиваемые данные в кортеж
    params = (name, repeat)

    # возвращение результата работы фунции
    return params

# with Timing(file_name) as file:
#     pass

# для использования обЪекта класса как контекстного менеджера, необходимо
# закоментировать строки 14, 15 и 40
# раскоментировать 50 и 51
