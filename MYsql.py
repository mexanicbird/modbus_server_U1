"""Импортируем библиотеки"""
import pymysql
import modbus_Slave_001
import modbus_Slave_002
from termcolor import colored

"""функция отправки данных в базу"""
def send_to_database():
    try:
        '''Подключение к базе данных'''
        con = pymysql.connect('localhost', 'root', '23232323Aa', 'sensor_001')
        '''Читаем версию базы данных'''
        cur = con.cursor()
        cur.execute("SELECT VERSION()")
        version = cur.fetchone()
        #print("Database version: {}".format(version[0]))
        cur = con.cursor()
        cur.execute("INSERT INTO `sensor_001`.`sensor_data_001` (`S1_t1`, `S1_t2`, "
                    "`S1_h1`, `S1_h2`, `S1_p1`, `S2_t1`, `S2_t2`, `S2_h1`, `S2_h2`, "
                 "`S2_p1`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,"
                 " %s)" % (modbus_Slave_001.S1_t1_q, modbus_Slave_001.S1_t2_q,
                          modbus_Slave_001.S1_h1_q, modbus_Slave_001.S1_h2_q,
                         modbus_Slave_001.S1_p1_q, modbus_Slave_002.S2_t1_q,
                         modbus_Slave_002.S2_t2_q, modbus_Slave_002.S2_h1_q,
                             modbus_Slave_002.S2_h2_q, modbus_Slave_002.S2_p1_q))
        con.commit()
        print(colored("recorded in the database", 'green', attrs=['reverse', 'blink']))
        ''' в конце сеанса отключаемся'''
        con.close()
    except:
        print(colored("not recorded in the database", 'yellow', attrs=['reverse', 'blink']))







