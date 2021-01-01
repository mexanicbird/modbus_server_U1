"""Импортируем библиотеки"""
from termcolor import colored
import time
import datetime

"""Импортируем файлы"""
import modbus_Slave_001
import modbus_Slave_002
import MYsql
#import send_to_site
import static_var



"""функция вызова результатов в терминал"""
def print_Data_001(i):

    """Запрос точного времени"""
    time_now = datetime.datetime.now()

    """вывод заголовка в терминал"""
    print(colored("Result №  " + str(i) + ":", 'red', attrs=['reverse', 'blink']))

    """функции опроса слэйв устройств"""
    modbus_Slave_001.loadA()
    modbus_Slave_002.loadA()
    modbus_Slave_001.S1_t1.printer()
    modbus_Slave_001.S1_t2.printer()
    modbus_Slave_001.S1_h1.printer()
    modbus_Slave_001.S1_h2.printer()
    modbus_Slave_001.S1_h2.printer()
    print(' ')

    """функции опроса слэйв устройств"""
    modbus_Slave_002.S2_t1.printer()
    modbus_Slave_002.S2_t2.printer()
    modbus_Slave_002.S2_h1.printer()
    modbus_Slave_002.S2_h2.printer()
    modbus_Slave_002.S2_h2.printer()
    print(' ')

    """запись в базу по условию 0 секунд точного времени"""
    if time_now.second == 0 or time_now.second == 30:
        MYsql.send_to_database()
    time.sleep(1)

#i = 0
#while i > 0:
    #i = i + 1
    #print_Data_001(i)

i = 0
for i in range(1000):
    i = i + 1
    print_Data_001(i)




