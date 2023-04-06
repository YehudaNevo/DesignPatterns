import sqlite3
import psycopg2  # Assuming psycopg2 package is installed
import mysql.connector  # Assuming mysql-connector-python package is installed
from abc import ABC, abstractmethod

# Product Interface
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Concrete Products
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return psycopg2.connect(database="example", user="user", password="password")

class MySQLConnection(DatabaseConnection):
    def connect(self):
        return mysql.connector.connect(user="user", password="password", database="example")

class SQLiteConnection(DatabaseConnection):
    def connect(self):
        return sqlite3.connect("example.db")

# Creator Interface
class DatabaseConnectionFactory(ABC):
    @abstractmethod
    def create_connection(self):
        pass

# Concrete Creators
class PostgreSQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return PostgreSQLConnection()

class MySQLConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return MySQLConnection()

class SQLiteConnectionFactory(DatabaseConnectionFactory):
    def create_connection(self):
        return SQLiteConnection()

# Usage
db_type = "sqlite"  # This can be set based on user input or configuration settings

if db_type == "postgresql":
    factory = PostgreSQLConnectionFactory()
elif db_type == "mysql":
    factory = MySQLConnectionFactory()
else:
    factory = SQLiteConnectionFactory()

connection = factory.create_connection().connect()
