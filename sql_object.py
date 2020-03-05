#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from time import sleep
import sqlite3
from sqlite3 import Error

class sql_object:
    def __init__(self):
        self.conn = None
        self.cur = None

    def create_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row
            print("Successful connection!")
            print("SQLite version: " + sqlite3.version)
            self.cur = self.conn.cursor()
        except Error as e:
            print("create_connection: {}".format(e))

    def read_sensordb(self):
        try:
            self.cur.execute('SELECT * FROM sensor_readings')
            rows = self.cur.fetchall()
            t = PrettyTable(dict(rows[0]).keys())
            for row in rows:
                t.add_row(dict(row).values())
            print(t)
        except Error as e:
            print("read_sensordb: {}".format(e))

    def fetch_quary(self, input_string):
        try:
            self.cur.execute(input_string)
            rows = self.cur.fetchall()
            t = PrettyTable(dict(rows[0]).keys())
            for row in rows:
                t.add_row(dict(row).values())
            print(t)
        except Error as e:
            print("Quary error: ", e)

    def write_to_database(self, input_string):
        try:
            self.cur.execute("INSERT INTO sensor_readings (temperature, humidity, time, date, sensor, location) VALUES ({})".format(input_string))
            self.conn.commit()
            print("Values added to database!")
        except Error as e:
            print("Write error: ", e)

    def close_connection(self):
        if self.conn:
            try:
                self.conn.close()
            except Error as e:
                print("close connection: {}".format(e))
            else:
                print("Connection closed!")
