from db import get_conn

def log_interaction(user_id, topic, action):
    conn = get_conn()
    c = conn.cursor()
    c.execute("INSERT INTO interactions (user_id, topic, action) VALUES (?, ?, ?)", (user_id, topic, action))
    conn.commit()
    conn.close()

def add_points(user_id, points):
    conn = get_conn()
    c = conn.cursor()
    c.execute("UPDATE users SET points = points + ? WHERE id=?", (points, user_id))
    conn.commit()
    conn.close()
