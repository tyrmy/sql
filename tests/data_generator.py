"""
Created on 12 Apr, 2020

@author Lassi Lehtinen
A test script for generating random data to sqlite database
"""
import random
import time
from sql.sqli_writer import sqlite_object as SQL

def str_time_prop(start, end, format, prop):
    """
    Generates a random datetime object between two dates given as arguments.
    """
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    """
    Creates a random date (YYYY-MM-DD) in string format between two dates give as arguments.

    Ex.
    dat = random_date("2019-1-1", "2021-1-1", random.random())
    """
    return str_time_prop(start, end, '%Y-%m-%d', prop)

def random_time(start, end, prop):
    """
    Creates a random time (HH:MM) in string format between two dates give as arguments.

    Ex.
    time = random_time("00:00", "23:59", random.random())
    """
    return str_time_prop(start, end, '%H:%M', prop)

def random_datetime(start, end, prop):
    return str_time_prop(start, end, '%d-%m-%Y %H:%M', prop)

def generate_random_data():
    temp = round(random.uniform(2.5,22.5), 1)
    hum = random.randint(10,90)
    dat = random_date("2019-1-1", "2021-1-1", random.random())
    time = random_time("00:00", "23:59", random.random())
    output = '%s, %s, \'%s\', \'%s\', 1, \'olohuone\'' % (temp, hum, time, dat)
    return output

def generate_random_bigdata(db, size):
    for i in range(size):
        db.write_to_database(generate_random_data())

if __name__ == '__main__':
    sql = SQL()
    sql.create_connection('example.db')

    x, y = sql.get_two_values("sensor_readings", "temperature", "time")

    print(x)
    print(y)
    sql.close_connection()
