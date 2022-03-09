import sqlite3

conn = sqlite3.connect('sample.database')

cursor = conn.cursor()

cursor.execute("""
select  e.firstname ,e.lastname.d.name from e , d
where e.dept==d.departmentid
order by e.lastname desc""")

for row in cursor.fetchall():
    print(row)

cursor.close()