
import sqlite3

conn=sqlite3.connect("Example.db")

c=conn.cursor()
# c.execute('''
# CREATE TABLE STUDENTS (date text,name text)
# ''')
# c.execute('''insert into STUDENTS values ('2001/3/20','ali')''')
list = c.execute('''  
     Select * from STUDENTS
 ''').fetchall()
print(type(list))
conn.commit()
conn.close()
  