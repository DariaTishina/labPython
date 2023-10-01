import psycopg2
import json
    """
    Написать функцию, которая переводит 
    структуру всех таблиц существующей 
    базы данных, в формат Json.
    (Также прикреплен файл dvdrent.tar)
    """
def lab6task7():

    # параметры соединения с БД
    connection = psycopg2.connect(dbname="postgres",user="postgres",password="1",host="127.0.0.1",port="5432")
    cursor = connection.cursor()
    # запрос для выбора всех таблиц схемы
    tables ="""SELECT * FROM pg_catalog.pg_tables WHERE schemaname = 'public';"""
    # выполнение запроса
    cursor.execute(tables)
    # возврат в виде списка
    results = cursor.fetchall()
    with open('result.txt', 'a') as file:
        json.dump(results, file)

lab6task7()
