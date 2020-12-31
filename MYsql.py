"""Импортируем библиотеки"""
import pymysql

'''Подключение к базе данных'''
con = pymysql.connect('localhost', 'root',
                      '23232323Aa', 'data_sensors')

'''Читаем версию базы данных'''
cur = con.cursor()
cur.execute("SELECT VERSION()")
version = cur.fetchone()
print("Database version: {}".format(version[0]))




"""функция отправки данных в базу"""
def send_to_database():
    print("Отправка данных в базу")
    '''пишем  базу и коммитим'''
    cur = con.cursor()
    cur.execute("INSERT INTO `shop`.`brand` (`name`) VALUES ('Red FOX')")
    con.commit()

    ''' в конце сеанса отключаемся'''
    con.close()


'''читаем таблицу в консоль'''
#cur = con.cursor()
#cur.execute("SELECT * FROM shop.brand")
#rows = cur.fetchall()
#for row in rows:
    #print("{0} {1} ".format(row[0], row[1]))


