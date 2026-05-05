import _sqlite3

DB_NAME = "database.db"

def get_connection():
    return _sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   email TEXT UNIQUE,
                   password TEXT)""")
    
    conn.commit()
    conn.close()

def create_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                INSERT INTO users (email, password) VALUES (?, ?)
                       """, (email, password))
        conn.commit()
    except _sqlite3.IntegrityError:
        conn.close()
        return {"msg" : "Email já utilizado!"}
    conn.commit()
    return {"msg" : "Usuário criado"}

def login_db(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM users
                   WHERE email = ? and password = ?
                   """, (email,password))
    user =  cursor.fetchone()
    conn.close()

    if user:
        return {"msg" : "Login OK"}
    else:
        return {"msg" : "Email ou senha incorretos"}

def delete_user(email, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            DELETE FROM users
                   WHERE email = ? AND password = ?
                   """, (email, password))
    conn.commit()
    conn.close()
    return {"msg" : "Usuário deletado!"}

def show_all():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM users""")
    user = cursor.fetchall()
    
    conn.close()
    return(user)