import mysql.connector

def store_manga_data(manga_data):
    """
    Store fetched manga data into MySQL database.
    """
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            database="your_database"
        )

        cursor = db.cursor()

        for manga in manga_data:
            cursor.execute(
                """
                INSERT INTO manga (id, title, genres, description, average_score, popularity)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE 
                title=VALUES(title), genres=VALUES(genres), description=VALUES(description),
                average_score=VALUES(average_score), popularity=VALUES(popularity)
                """,
                (
                    manga["id"],
                    manga["title"]["romaji"],
                    ','.join(manga["genres"]),
                    manga["description"],
                    manga["averageScore"],
                    manga["popularity"]
                )
            )

        db.commit()
        print(f"{len(manga_data)} manga records stored successfully.")
    except mysql.connector.Error as err:
        print(f"Error storing data in MySQL: {err}")
    finally:
        db.close()