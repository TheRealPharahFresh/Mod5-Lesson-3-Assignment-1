from Gym_Database_SQL import connect_database

conn = connect_database()

if conn is not None:

    def delete_workout_session(id):

        try:
            cursor = conn.cursor()

            deleted_workout = (id, )

            query = "DELETE FROM WorkoutSessions WHERE id = %s "

            cursor.execute(query, deleted_workout)
            conn.commit()
            print("Workout Deleted Successfully.")
        finally:
            cursor.close()
            conn.close()

id = 1
delete_workout_session(id)