"""Импорт библиотек"""
import socket
import modbus_Slave_001
import modbus_Slave_002
from termcolor import colored
import time



"""функция отправка на сайт"""
def send_data_to_site():
    """подключение сокета"""
    sock = socket.socket()
    try:
        """подключение адреса"""
        sock.connect(('localhost', 9090))

        """переменные"""
        c0 = (b'     ')
        c1 = str(modbus_Slave_001.S1_t1_q)
        c2 = str(modbus_Slave_001.S1_t2_q)
        c3 = str(modbus_Slave_001.S1_h1_q)
        c4 = str(modbus_Slave_001.S1_h2_q)
        c5 = str(modbus_Slave_001.S1_p1_q)
        c6 = str(modbus_Slave_002.S2_t1_q)
        c7 = str(modbus_Slave_002.S2_t2_q)
        c8 = str(modbus_Slave_002.S2_h1_q)
        c9 = str(modbus_Slave_002.S2_h2_q)
        c10 = str(modbus_Slave_002.S2_p1_q)

        """Конвертируем в байты"""
        c1.encode('utf-8')
        c2.encode('utf-8')
        c3.encode('utf-8')
        c4.encode('utf-8')
        c5.encode('utf-8')
        c6.encode('utf-8')
        c7.encode('utf-8')
        c8.encode('utf-8')
        c9.encode('utf-8')
        c10.encode('utf-8')

        с_bytes1 = c1.encode('utf-8')
        с_bytes2 = c2.encode('utf-8')
        с_bytes3 = c3.encode('utf-8')
        с_bytes4 = c4.encode('utf-8')
        с_bytes5 = c5.encode('utf-8')
        с_bytes6 = c6.encode('utf-8')
        с_bytes7 = c7.encode('utf-8')
        с_bytes8 = c8.encode('utf-8')
        с_bytes9 = c9.encode('utf-8')
        с_bytes10 = c10.encode('utf-8')

        """Отправляем в байтах"""
        sock.send(c0)
        sock.send(с_bytes1)
        sock.send(c0)
        sock.send(с_bytes2)
        sock.send(c0)
        sock.send(с_bytes3)
        sock.send(c0)
        sock.send(с_bytes4)
        sock.send(c0)
        sock.send(с_bytes5)
        sock.send(c0)
        sock.send(с_bytes6)
        sock.send(c0)
        sock.send(с_bytes7)
        sock.send(c0)
        sock.send(с_bytes8)
        sock.send(c0)
        sock.send(с_bytes9)
        sock.send(c0)
        sock.send(с_bytes10)

        """Получение данных"""
        data = sock.recv(4096)

        """Закрываем подключение"""
        sock.close()
        print(colored("sent to the site", 'green', attrs=['reverse', 'blink']))
        print(data)

    except:
        print(colored("not submitted to the site", 'yellow', attrs=['reverse', 'blink']))

i = 0
for i in range(7):
    i = i + 1
    #send_data_to_site()
    #time.sleep(0.5)