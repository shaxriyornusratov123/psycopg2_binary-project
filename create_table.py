from db import get_db_connection

connection=get_db_connection()
cursor=connection.cursor()

try:
    cursor.execute(
        """
    create table if not exists student(
    id serial primary key,
    name varchar(100),
    age int,
    course varchar(50)
    )
"""
    )

    connection.commit()
    cursor.close()
    connection.close()
    print("Jadval yaratildi! ")

except :
    print("xatolik")