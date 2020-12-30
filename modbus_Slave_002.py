"""Импортируем библиотеки"""
from termcolor import colored
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import datetime
dt = datetime.time()
a = datetime.datetime.now()

"""адресация и опрос подчиненного устройства"""
master2 = modbus_tcp.TcpMaster(host="192.168.1.11", port=int(502))
master2.set_timeout(1.0)

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
                      + str(self.data3) + " " + str(self.data5) + " " + str(self.data6) + " ", 'yellow', ))

"""функия опроса и заполнения экземпляров класса"""
def loadA():
    a = datetime.datetime.now()
    global S2_t1, S2_t2, S2_h1, S2_h2, S2_p1
    try:
        t1 = master2.execute(1, cst.READ_HOLDING_REGISTERS, 0, 1)
        S2_t1 = Analog_val('S2_t1 =', t1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        t2 = master2.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S2_t2 = Analog_val('S2_t2 =', t2[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        h1 = master2.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S2_h1 = Analog_val('S2_h1 =', h1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        h2 = master2.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S2_h2 = Analog_val('S2_h2 =', h2[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)
        p1 = master2.execute(1, cst.READ_HOLDING_REGISTERS, 1, 1)
        S2_p1 = Analog_val('S2_p1 =', p1[0], 1, a.day, a.month, a.year, a.hour, a.minute, a.second)

    except:
        S2_t1 = Analog_val('S2_t1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S2_t2 = Analog_val('S2_t2 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S2_h1 = Analog_val('S2_h1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S2_h2 = Analog_val('S2_h2 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)
        S2_p1 = Analog_val('S2_p1 =', None, 0, a.day, a.month, a.year, a.hour, a.minute, a.second)

    return S2_t1, S2_t2, S2_h1, S2_h2, S2_p1