#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from prettytable import PrettyTable
from time import sleep as slp
import pymysql

con = pymysql.connect('192.168.1.13', 'lassi', 'nukkumatti', 'mysql', charset='utf8mb4')

def print_sql():
    t = PrettyTable(['id','temp','stamp'])
    cur = con.cursor()
    cur.execute("USE mittaukset")
    cur.execute("SELECT * FROM zerotemp")

    for row in cur.fetchall():
       t.add_row(row) 

    print(t)

print_sql()
