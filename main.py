"""Импортируем библиотеки"""
from termcolor import colored
#import modbus_Slave_001
#import modbus_Slave_002
import static_var
import time

"""функция вызова результатов в терминал"""
def print_Data_001(i):
    static_var.loadA()
    static_var.SS1.printer()
    static_var.SS2.printer()
    static_var.SS3.printer()
    print(' ')
    #import modbus_Slave_001.loadA()
    #import modbus_Slave_002.loadA()
    #modbus_Slave_001.S1_t1.printer()
    #modbus_Slave_001.S1_t2.printer()
    #modbus_Slave_001.S1_h1.printer()
    #modbus_Slave_001.S1_h2.printer()
    #modbus_Slave_001.S1_h2.printer()
    #print(' ')
    #modbus_Slave_002.S1_t1.printer()
    #modbus_Slave_002.S1_t2.printer()
    #modbus_Slave_002.S1_h1.printer()
    #modbus_Slave_002.S1_h2.printer()
    #modbus_Slave_002.S1_h2.printer()
    #print(' ')
    print(colored("Result №  " + str(i) + ":", 'red', attrs=['reverse', 'blink']))
    time.sleep(0.3)

#i = 0
#while i > 0:
    #i = i + 1
    #print_Data_001(i)

i = 0
for i in range(10):
    i = i + 1
    print_Data_001(i)




