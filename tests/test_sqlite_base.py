"""
Created on Apr 27, 2020

@author: Lassi Lehtinen
Tests using pytest on the interface
"""

import pytest
import os
import sql.sqlite_base as s
from sqlite3 import Error

def test_sql_object():
    assert(s.sql_base() != None)

def test_database_folder_exists():
    assert(os.path.isdir('./databases') == True)

def test_databases_exists():
    filenames = os.listdir('./databases/')
    assert filenames != None
    assert len(filenames) > 0
