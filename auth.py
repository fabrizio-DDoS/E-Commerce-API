import hashlib

def criptografa(senha):
    senha_criptografada = hashlib.sha256(senha.encode()).hexdigest()
    return senha_criptografada
