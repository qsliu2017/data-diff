import data_diff
import data_diff.__main__
from data_diff.sqeleton.databases.oracle import *
import cx_Oracle
from data_diff.sqeleton.databases.mysql import *
import mysql.connector

if __name__ == "__main__":
    data_diff.__main__.main()
