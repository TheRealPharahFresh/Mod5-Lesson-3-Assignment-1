from Gym_Database_SQL import connect_database
conn = connect_database()

if conn is not None:
    def add_workout_session(member_id, date, duration_minutes, calories_burned):
        try:
            cursor = conn.cursor()
            new_workout_session = (member_id, date, duration_minutes, calories_burned)
            query = "INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned) VALUES (%s, %s, %s, %s)"
            
            
            cursor.execute(query, new_workout_session)
            conn.commit()
            print("New Workout Session Added Successfully")

        finally:
            cursor.close()
            conn.close()


member_id = 8
date = "2024-11-20"
duration_minutes = 60
calories_burned = 1000

add_workout_session(member_id, date, duration_minutes, calories_burned)
