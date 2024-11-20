from Gym_Database_SQL import connect_database

conn = connect_database()

if conn is not None:

    def add_member(id, name, age):

        try:
            cursor = conn.cursor()

            new_member = (id, name, age )

            query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"

            cursor.execute(query, new_member)
            conn.commit()
            print("New Member Added Successfully.")
        finally:
            cursor.close()
            conn.close()


id = 8
name = "Gabe Aaron"
age = "32"

add_member(id, name, age)