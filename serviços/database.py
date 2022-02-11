import sqlite3

class BancodeDados:
    def __init__(self):
        self.conexao = sqlite3.connect("bancoDados.csv")
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()
        #Cria uma tabela
        c.execute(
            """
            create table if not exists dados(
                id integer primary key autoincrement,
                nome text,
                idade integer,
                local text,
                pergunta1 text,
                pergunta2 text
            )
            """
        )
        self.conexao.commit()
        c.close()