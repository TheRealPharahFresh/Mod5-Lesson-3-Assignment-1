from Gym_Database_SQL import connect_database

conn = connect_database()

if conn is not None:
    def get_members_in_age_range(start_age, end_age):
        try:
            cursor = conn.cursor()
            age_range = (start_age, end_age)

            query = "SELECT * FROM Members WHERE age BETWEEN %s AND %s"

            cursor.execute(query, age_range)
            
            results = cursor.fetchall()
            print("Age Range Gathered Successfully")
            return results
        except Exception as e:
            print(f"Error: {e}")
        finally:
            cursor.close()
            


members_in_range = get_members_in_age_range(25,30)
for member in members_in_range:
    print(member)


conn.close()







