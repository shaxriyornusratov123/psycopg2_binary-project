from db import get_db_connection

connection=get_db_connection()
cursor=connection.cursor()

try:
    cursor.execute(
        """ select * from student"""
    )
    
    records=cursor.fetchall()
    for i in records:
        print(i)


except:
    print("xatolik")
