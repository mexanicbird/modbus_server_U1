"""Импортируем библиотеки"""
from termcolor import colored
import datetime

"""функции времени и даты"""
dt = datetime.time()
a = datetime.datetime.now()

"""Создаем класс аналоговой переменной"""
class Analog_val(object):
    def __init__(self, name, val, log, data1, data2, data3, data4, data5, data6):
        """Инициализация класса"""
        self.name = name
        self.val = val
        self.log = log
        self.data1 = data1
        self.data2 = data2
        self.data3 = data3
        self.data4 = data4
        self.data5 = data5
        self.data6 = data6

    """метод принтера значений в строку"""
    def printer(self):
        print(colored(str(self.name) + " " + str(self.val) + " " + str(self.log) + " " + str(self.data1) + " " + str(self.data2) + " "
                      + str(self.data3) + " " + str(self.data4) + " " + str(self.data5) + " " + str(self.data6) + " ", 'blue', ))

    """метод принтера значений в строку"""
    def printer_short(self):
        print(colored(str(self.name) + " " + str(self.val) + " ", 'yellow', ))


"""опрос слейв устройства """

def loadA():
    a = datetime.datetime.now()
    global SS1, SS2, SS3
    try:
        s1 = 777
        SS1 = Analog_val('SS1 =', s1, 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        s2 = 778
        SS2 = Analog_val('SS2 =', s2, 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        s3 = 779
        SS3 = Analog_val('SS3 =' ,s3, 1, a.day, a.month, a.year, a.hour, a.minute, a.second)

    except:
        SS1 = Analog_val('SS1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        SS2 = Analog_val('SS2 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        SS3 = Analog_val('SS3 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)

    return SS1, SS2, SS3

a1 = SS1.name