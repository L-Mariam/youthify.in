from config import db

cursor = db.cursor()

def getEvents():
    query = "SELECT title, starttime, endtime, image FROM events, event_images WHERE events.event_id = event_images.event_id;"
    cursor.execute(query)
    for i in cursor.fetchall():
        yield i