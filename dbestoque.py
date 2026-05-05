import _sqlite3

DB_NAME = "dbestoque.db"

def get_connection():
    return _sqlite3.connect(DB_NAME)

def create_table_estoque():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS estoque(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   produto TEXT UNIQUE,
                   preco FLOAT)""")
    
    conn.commit()
    conn.close()

def create_estoque(produto, preco):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                INSERT INTO estoque (produto, preco) VALUES (?, ?)
                       """, (produto, preco))
        conn.commit()
    except _sqlite3.IntegrityError:
        conn.close()
        return {"msg" : "Produto já adicionado!"}
    conn.commit()
    return {"msg" : "Produto adicionado"}

def achar_produto(produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM estoque
                   WHERE produto = ?
                   """, (produto,))
    prod =  cursor.fetchone()
    conn.close()
    return prod

def delete_produto(produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            DELETE FROM estoque
                   WHERE produto = ?
                   """, (produto,))
    conn.commit()
    conn.close()
    return {"msg" : "Produto deletado!"}

def show_all_produtos():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM estoque""")
    prod = cursor.fetchall()
    
    conn.close()
    return(prod)

def show_preco(produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT preco FROM estoque
                   WHERE produto = ?
                   """, (produto,))
    prec = cursor.fetchone()
    conn.close()
    if not prec:
        return 0
    return float(prec[0])