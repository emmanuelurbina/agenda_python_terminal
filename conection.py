import peewee as pw

from datetime import datetime
HOST = "localhost"
USER = "root"
PASSWORD = ""
DB = "agenda"
PORT = 3306

db = pw.MySQLDatabase(database=DB,
                      host=HOST,
                      port=PORT,
                      user=USER,
                      passwd=PASSWORD)
