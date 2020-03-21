#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

import random
import time
from sqlite import sqlite_object as SQL

def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)

def random_time(start, end, prop):
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

sql = SQL()
sql.create_connection('sensordata.db')

#sql.print_quary('SELECT * FROM sensor_readings')
#sql.print_quary('SELECT DISTINCT * FROM sensor_readings ORDER BY date(date) DESC Limit 10')
#sql.print_quary('SELECT DISTINCT * FROM sensor_readings ORDER BY time(time) DESC Limit 10')
#sql.print_quary('SELECT * FROM sensor_readings ORDER BY date(date) DESC')
#sql.print_quary('SELECT COUNT(*), temperature FROM sensor_readings WHERE temperature = temperature GROUP BY temperature')
#generate_random_bigdata(sql, 100)
sql.print_all_from_table("sensor_readings")

#sql.get_table_columns("sensor_readings")
#sql.get_table_columns("sensors")
sql.close_connection()
