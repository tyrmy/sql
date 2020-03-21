# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from time import sleep
import sqlite3
from sqlite3 import Error

class sqlite_object:
    def __init__(self):
        self.conn = None
        self.cur = None

    def create_connection(self, db_file):
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row
            print("Successful connection to {}!".format(db_file))
            print("SQLite version: " + sqlite3.version)
            self.cur = self.conn.cursor()
        except Error as e:
            print("create_connection: {}".format(e))

    def print_all_from_table(self, table_name):
        try:
            self.cur.execute('SELECT * FROM {}'.format(table_name))
            rows = self.cur.fetchall()
            t = PrettyTable(dict(rows[0]).keys())
            for row in rows:
                t.add_row(dict(row).values())
            print(t)
        except Error as e:
            print("read_sensordb: {}".format(e))

    def get_table_columns(self, table_name):
        try:
            self.cur.execute("SELECT * FROM " + table_name)
            rows = self.cur.fetchall()
            print((table_name + ": column names").upper())
            for name in rows[0].keys():
                print(name)
        except Error as e:
            print("get_table_columns: {}".format(e))

    def print_quary(self, input_string):
        try:
            self.cur.execute(input_string)
            rows = self.cur.fetchall()
            t = PrettyTable(dict(rows[0]).keys())
            for row in rows:
                t.add_row(dict(row).values())
            print(t)
        except Error as e:
            print("Quary error: {}".format(e))

    def write_to_database(self, input_string):
        try:
            self.cur.execute(input_string)
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
