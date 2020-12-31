"""Импортируем библиотеки"""
import pymysql

'''Подключение к базе данных'''
con = pymysql.connect('localhost', 'root', '23232323Aa', 'sensor_001')
S1_t1 = 0
S1_t2 = 125
S1_h1 = 126
S1_h2 = 127
S1_p1 = 128
S2_t1 = 129
S2_t2 = 130
S2_h1 = 131
S2_h2 = 132
S2_p1 = 133

'''Читаем версию базы данных'''
cur = con.cursor()
cur.execute("SELECT VERSION()")
version = cur.fetchone()
print("Database version: {}".format(version[0]))

''' передаем данные в базу'''
cur = con.cursor()
cur.execute("INSERT INTO `sensor_001`.`sensor_data_001` (`S1_t1`, `S1_t2`, "
            "`S1_h1`, `S1_h2`, `S1_p1`, `S2_t1`, `S2_t2`, `S2_h1`, `S2_h2`, "
            "`S2_p1`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,"
            " %s)" % (S1_t1, S1_t2, S1_h1, S1_h2, S1_p1, S2_t1, S2_t2, S2_h1, S2_h2, S2_p1))
con.commit()

''' в конце сеанса отключаемся'''
con.close()

"""функция отправки данных в базу"""
def send_to_database():
    print("Отправка данных в базу")





