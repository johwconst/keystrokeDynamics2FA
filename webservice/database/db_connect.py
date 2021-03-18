import sqlite3 as sql

def create_db():
    try:
        conn = sql.connect('database.db')
        conn.execute('CREATE TABLE tb_usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)')
        print("Tabela criada corretamente")
        conn.close()
    except:
        print("Conexão não pode ser sucedida")

def drop_db():
    try:
        conn = sql.connect('database.db')
        conn.execute('DROP TABLE tb_usuario')
        print("Tabela deletada com sucesso!")
        conn.close()
    except:
        print("Conexão negada")


def add_user_and_passw(username, password):
    try:
        with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM tb_usuario where username=?",[username])
            con.row_factory = sql.Row
            rows = cur.fetchall()
            if rows:
                print("Username já existente!")
                return 0, False
            else:
                con.commit()
                cur.execute("INSERT INTO tb_usuario (username,password)  VALUES (?,?)",(username,password))   
                id = cur.lastrowid
                print("Usuario criado, ID:",id)
                return id, True
    except:
        print("Erro no cadastro")
        

def get_user_and_passw(id):
    try:
        con = sql.connect("database.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("select * from tb_usuario")
   
        rows = cur.fetchall()
        username = rows[id]['username']
        password = rows[id]['password']
        return username, password
    except:
        print("Não foi possivel obter os usuarios!")

