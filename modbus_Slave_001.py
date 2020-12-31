"""Импортируем библиотеки"""
from termcolor import colored
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import datetime

"""функции времени и даты"""
dt = datetime.time()
a = datetime.datetime.now()

"""адресация и опрос подчиненного устройства"""
master1 = modbus_tcp.TcpMaster(host="192.168.1.10", port=int(502))
master1.set_timeout(1.0)

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
        print(colored(str(self.name) + " " + str(self.val) + " ", 'blue', ))


"""функия опроса и заполнения экземпляров класса"""
def loadA():
    a = datetime.datetime.now()
    global S1_t1, S1_t2, S1_h1, S1_h2, S1_p1
    try:
        t1 = master1.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
        S1_t1 = Analog_val('S1_t1 =', t1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        t2 = master1.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S1_t2 = Analog_val('S1_t2 =', t2[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        h1 = master1.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S1_h1 = Analog_val('S1_h1 =', h1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        h2 = master1.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S1_h2 = Analog_val('S1_h2 =', h2[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        p1 = master1.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S1_p1 = Analog_val('S1_p1 =', p1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)

    except:
        S1_t1 = Analog_val('S1_t1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S1_t2 = Analog_val('S1_t2 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S1_h1 = Analog_val('S1_h1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S1_h2 = Analog_val('S1_h2 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S1_p1 = Analog_val('S1_p1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)

    return S1_t1, S1_t2, S1_h1, S1_h2, S1_p1



