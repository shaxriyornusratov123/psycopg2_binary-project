from db import get_db_connection

connection=get_db_connection()
cursor=connection.cursor()

try:
    cursor.execute(""" 
    insert into student(name,age, course) values(%s, %s, %s)
    """,
    ("Shaxriyor",18,"2-kursDIF")
    )
    connection.commit()
    cursor.close()
    connection.close()
    print("malumot qushildi")

except:
    print("Xatolik")    