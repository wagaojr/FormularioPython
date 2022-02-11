from database import BancodeDados

class Dados:

    def __init__(self, id=0, nome="", idade=int,vinculo="", local="", pergunta1="", pergunta2=""):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.vinculo = vinculo
        self.local = local
        self.pergunta1 = pergunta1
        self.pergunta2 = pergunta2
    
    def insertDado(nome="", idade=int,vinculo="", local="", pergunta1="",  pergunta2=""):
          banco = BancodeDados()
          c = banco.conexao.cursor()
          comando = "insert into dados(nome, idade, vinculo, local, pergunta1, pergunta2) values('"+ nome +"', '"+ str(idade) + "','"+vinculo+"','"+ local +"','"+ pergunta1 +"','"+ pergunta2 +"')"
          c.execute(comando)
          banco.conexao.commit()
          c.close()  
    
    def deleteDados(id):
        banco = BancodeDados()
        c = banco.conexao.cursor()
        comando = "delete from dados where id = "+id
        c.execute(comando)
        banco.conexao.commit()
        c.close()
    
    def selectDados(self, id):
        banco = BancodeDados()
        c = banco.conexao.cursor()
        comando = "select * from dados where id = " + str(id) + " "
        c.execute(comando)
        for elemento in c:
            self.iditem = elemento[0]
            self.produto = elemento[1]
            self.quantidade = elemento[2]
            self.categoria = elemento[3]
            self.preco = elemento[4]
            self.limite = elemento[5]
        c.close()
    
    def updateDados(nome, idade,vinculo, local, pergunta1,  pergunta2, id):
        banco = BancodeDados()
        c = banco.conexao.cursor()
        comando = "update dados set nome = '" + nome +"', idade = '" + idade +"', vinculo = '"+vinculo+"',local = '"+local+"', pergunta1 = '" +pergunta1+"', pergunta2 = '" +pergunta2+"'where id= "+id+""
        c.execute(comando)
        banco.conexao.commit()
        c.close()

    def populaDados():
        lista = []
        banco = BancodeDados()
        c = banco.conexao.cursor()
        comando = "select * from dados "
        c.execute(comando)
        for elementos in c:

            lista.append(elementos)
            total_rows = len(lista)
            total_columns = len(lista[0])

        c.close()
        for i in range(total_rows):
            for j in range(total_columns):
                lista[i][j]
        return lista
        
   