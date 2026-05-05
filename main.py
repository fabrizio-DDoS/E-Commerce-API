from fastapi import FastAPI
from database import create_table, create_user, login_db, delete_user,show_all
from auth import criptografa
from dbestoque import create_table_estoque, create_estoque, achar_produto, delete_produto,show_all_produtos, show_preco
from dbcarrinho import create_table_carrinho, create_compra, achar_carrinho, delete_produto_carrinho,show_all_carrinho


app = FastAPI()

create_table()

@app.post("/register")
def register_user(email:str , senha:str ):
    senha_S = criptografa(senha)
    return create_user(email, senha_S)

@app.post("/login")
def login_user(email:str , senha:str ):
    senha_S = criptografa(senha)
    return login_db(email, senha_S)

@app.delete("/del")
def deletar_user(email:str , senha:str):
    senha_S = criptografa(senha)
    return delete_user(email, senha_S)

@app.get("/read")
def read_users():
    return show_all()

#ESTOQUE - 

create_table_estoque()

@app.post("/estoque")
def register_estoque(produto:str , preco:float ):
    return create_estoque(produto,preco)

@app.post("/buscar-estoque")
def buscar_produto(produto:str ):
    return achar_produto(produto)

@app.delete("/delete-produto")
def deletar_produto(produto:str):
    return delete_produto(produto)

@app.get("/mostrar-estoque")
def read_estoque():
    return show_all_produtos()


#CARRINHO - 

create_table_carrinho()

@app.post("/item-carrinho")
def register_carrinho(produto:str):
    preco = show_preco(produto)
    produto_db = buscar_produto(produto)
    if produto_db != None:
        return create_compra(produto, preco)
    else:
        return {"msg" : "produto não existe no estoque"}

@app.post("/buscar-carrinho")
def buscar_carrinho(produto:str ):
    return achar_carrinho(produto)

@app.delete("/delete-produto-carrinho")
def deletar_produto_carro(produto:str):
    return delete_produto_carrinho(produto)

@app.get("/mostrar-carrinho")
def read_carrinho():
    return show_all_carrinho()








