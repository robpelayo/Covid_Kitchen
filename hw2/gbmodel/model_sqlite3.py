"""
A simple guestbook flask app.
ata is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+
| Name       | Email            | signed_on  | message        |
+============+==================+============+----------------+
| John Doe   | jdoe@example.com | 2012-05-28 | Hello world    |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table guestbook (name text, email text, signed_on date, message);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from foodtrucks")
        except sqlite3.OperationalError:
            cursor.execute("create table foodtrucks(name text, "
                           "address text, "
                           "city text, "
                           "state text,"
                           "zip text,"
                           "hours text,"
                           "phone text,"
                           "rating text,"
                           "pricing text,"
                           "parking text,"
                           "review text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: name, email, date, message
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM foodtrucks")
        return cursor.fetchall()

    def insert(self, name, address, city, state, zip, hours, phone, rating, pricing, parking, review):
        """
        Inserts entry into database
        :param name: String
        :param address: String
        :param city: String
        :param state: String
        :param zip: String
        :param hours: String
        :param phone: String
        :param rating: String
        :param pricing: String
        :param parking: String
        :param review: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'name':name,
                  'address':address,
                  'city':city,
                  'state':state,
                  'zip':zip,
                  'hours':hours,
                  'phone':phone,
                  'rating':rating,
                  'pricing':pricing,
                  'parking':parking,
                  'review':review}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into foodtrucks(name, address, city, state, zip, hours, phone, rating, pricing, parking, review) "
                       "VALUES (:name, :address, :city, :state, :zip, :hours, :phone, :rating,"
                       ":pricing, :parking, :review)", params)

        connection.commit()
        cursor.close()
        return True
