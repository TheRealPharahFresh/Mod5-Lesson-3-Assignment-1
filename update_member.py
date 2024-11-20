from Gym_Database_SQL import connect_database

conn = connect_database()

if conn is not None:

    def update_member(member_id, new_age):

        try:
            cursor = conn.cursor()

            update_member = (new_age, member_id)

            query = "UPDATE Members SET age = %s WHERE id = %s "

            cursor.execute(query, update_member)
            conn.commit()
            print("Updated Member Added Successfully.")
        finally:
            cursor.close()
            conn.close()


member_id = 8
new_age = 31

update_member(member_id, new_age)