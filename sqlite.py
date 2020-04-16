"""
Created on Mar 10, 2020

@author: Lassi Lehtinen
A basic sqlite3-Python interface. 
"""

from prettytable import PrettyTable
from time import sleep
import sqlite3
from sqlite3 import Error

class sqlite_object:
    def __init__(self):
        """
        Contructs a new sqlite object. Takes no arguments.
        """
        self.conn = None
        self.cur = None

    def create_connection(self, db_file):
        """
        Enstablish a connection to a database file.
        """
        try:
            self.conn = sqlite3.connect(db_file)
            self.conn.row_factory = sqlite3.Row
            print("Successful connection to {}!".format(db_file))
            print("SQLite version: " + sqlite3.version)
            self.cur = self.conn.cursor()
        except Error as e:
            print("create_connection: {}".format(e))

    def get_two_values(self, table, x, y):
        """
        Get two values as lists for plotting etc
        """
        try:
            self.cur.execute('SELECT {value1},{value2} FROM {source} LIMIT 10'.format(value1=x, value2=y, source=table))
            rows = self.cur.fetchall()

            x = []
            y = []
            for row in rows:
                x.append(row[0])
                y.append(row[1])
            return x, y
        except Error as e:
            print("get_two_values: {}".format(e))

    def print_topten(self, table_name):
        """
        Prints 10 latest rows of every column in database using PrettyTable
        """
        try:
            self.cur.execute('SELECT * FROM {} LIMIT 10'.format(table_name))
            rows = self.cur.fetchall()
            t = PrettyTable(dict(rows[0]).keys())
            for row in rows:
                t.add_row(dict(row).values())
            print(t)
        except Error as e:
            print("read_sensordb: {}".format(e))

    def print_all_from_table(self, table_name):
        """
        Prints all rows of every column in database using PrettyTable
        """
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
        """
        Prints the columns names of a table specified.
        """
        try:
            self.cur.execute("SELECT * FROM " + table_name)
            rows = self.cur.fetchall()
            print((table_name + ": column names").upper())
            for name in rows[0].keys():
                print(name)
        except Error as e:
            print("get_table_columns: {}".format(e))

    def print_quary(self, input_string):
        """
        Prints the results of an SQL quary using PrettyTable
        """
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
        """
        Executes an SQL quary to store values to database.
        """
        try:
            self.cur.execute(input_string)
            self.conn.commit()
            print("Values added to database!")
        except Error as e:
            print("Write error: ", e)

    def close_connection(self):
        """
        Closes the connection safely.
        """
        if self.conn:
            try:
                self.conn.close()
            except Error as e:
                print("close connection: {}".format(e))
            else:
                print("Connection closed!")
