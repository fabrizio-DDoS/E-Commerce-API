import _sqlite3

DB_NAME = "dbcarrinho.db"

def get_connection():
    return _sqlite3.connect(DB_NAME)

def create_table_carrinho():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            CREATE TABLE IF NOT EXISTS carrinho(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   produto TEXT UNIQUE,
                   preco FLOAT)""")
    
    conn.commit()
    conn.close()

def create_compra(produto, preco):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
                INSERT INTO carrinho (produto, preco) VALUES (?, ?)
                       """, (produto, preco))
        conn.commit()
    except _sqlite3.IntegrityError:
        conn.close()
        return {"msg" : "Produto já adicionado ao carrinho!"}
    conn.commit()
    return {"msg" : "Produto adicionado ao carrinho"}

def achar_carrinho(produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM carrinho
                   WHERE produto = ?
                   """, (produto,))
    prod =  cursor.fetchone()
    conn.close()

    return prod

def delete_produto_carrinho(produto):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            DELETE FROM carrinho
                   WHERE produto = ?
                   """, (produto,))
    conn.commit()
    conn.close()
    return {"msg" : "Produto deletado do carrinho!"}

def show_all_carrinho():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            SELECT * FROM carrinho""")
    prod = cursor.fetchall()
    
    conn.close()
    return(prod)