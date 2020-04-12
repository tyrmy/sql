# Python-Sqlite3 interface

A basic interface for managing sqlite database with python

---

## PyDoc

Help on module sqlite:

NAME
    sqlite - Created on Mar 10, 2020

FILE
    /home/lassi/Python/sql/sqlite.py

DESCRIPTION
    @author: Lassi Lehtinen
    A basic sqlite3-Python interface.

CLASSES
    sqlite_object
    
    class sqlite_object
     |  Methods defined here:
     |  
     |  __init__(self)
     |      Contructs a new sqlite object. Takes no arguments.
     |  
     |  close_connection(self)
     |      Closes the connection safely.
     |  
     |  create_connection(self, db_file)
     |      Enstablish a connection to a database file.
     |  
     |  get_table_columns(self, table_name)
     |      Prints the columns names of a table specified.
     |  
     |  print_all_from_table(self, table_name)
     |      Prints all rows of every column in database using PrettyTable
     |  
     |  print_quary(self, input_string)
     |      Prints the results of an SQL quary using PrettyTable
     |  
     |  print_topten(self, table_name)
     |      Prints 10 latest rows of every column in database using PrettyTable
     |  
     |  write_to_database(self, input_string)
     |      Executes an SQL quary to store values to database.

FUNCTIONS
    sleep(...)
        sleep(seconds)
        
        Delay execution for a given number of seconds.  The argument may be
        a floating point number for subsecond precision.


