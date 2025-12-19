import psycopg2 

def get_db_connection():

    try:
        connection=psycopg2.connect(
            dbname="education_db",
            user="postgres",
            password="Nusratov07",
            host="localhost",
            port="5432"
        )
        return connection
    except psycopg2.Error as e :
        print(f"Operational error: {e}")

print(get_db_connection())