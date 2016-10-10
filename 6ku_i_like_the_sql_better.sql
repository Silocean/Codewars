# Create a database /tmp/movies.db using SQLite3
# Create a table in it called "MOVIES"
# Insert data
import sqlite3

conn = sqlite3.connect('/tmp/movies.db')

conn.execute('CREATE TABLE IF NOT EXISTS MOVIES (Name TEXT NOT NULL, '
             'Year INT NOT NULL,'
             'Rating INT NOT NULL);')

conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Rise of the Planet of the Apes", 2011, 77)')
conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Dawn of the Planet of the Apes", 2014, 91)')
conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Alien", 1979, 97)')
conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Aliens", 1986, 98)')
conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Mad Max", 1979, 95)')
conn.execute('INSERT INTO MOVIES (Name, Year, Rating) VALUES '
             '("Mad Max 2: The Road Warrior", 1981, 100)')
conn.commit()
conn.close()