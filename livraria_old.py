"""Program CRUD to library. coding: utf-8"""

try:
    import os
    from os import system
    from os import sys
    import sys
    import oracledb
    os.chdir("C:")
    os.chdir("C:\\instantclient")
    '''os.chdir("C:\\Courses\\Puc\\sqldeveloper-20.4.1.407.0006-x64\\sqldeveloper")'''
    import cx_Oracle
except OSError as err:
    print(f"OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

def cadastre_autor (conexao):
    """Função para cadastrar autor"""
    cursor = conexao.cursor()
    nome   = input("\nNome do autor? ")

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'"+nome+"')")
        conexao.commit()
        print("Autor cadastrado com sucesso")
    except oracledb.DatabaseError:
        print("Autor repetido")


def remova_autor (conexao):
    """Função para remover autor"""
    cursor = conexao.cursor()
    nome   = input("\nNome do autor? ")

    cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome+"'")
    conexao.commit ()

    linha = cursor.fetchone()
    if not linha:
        print("Autor inexistente")
    else:
        cursor.execute("DELETE FROM Autores WHERE Nome='"+nome+"'")
        conexao.commit ()
        print("Autor removido com sucesso")

def cadastre_livro (conexao):
    """Função para cadastrar um livro"""
    cursor    = conexao.cursor()
    nome_livro = input("\nNome do livro? ")
    try:
        preco_livro = float(input("Preço do livro? "))
    except ValueError:
        print("Preço inválido")
    else:
        nome_autor = input("Nome do autor? ")

        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nome_autor+"'")
        linha = cursor.fetchone()
        if not linha:
            print("Autor inexistente")
        else:
            id_autor = linha[0]

            try:
                cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'"+nome_livro+"',"+str(preco_livro)+")")
                conexao.commit ()
            except oracledb.DatabaseError:
                print("Livro repetido")
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome_livro+"'")
                linha  = cursor.fetchone()
                codigo_livro = linha[0]
                cursor.execute(
                    "INSERT INTO Autorias (Id,Codigo) VALUES ("+str(id_autor)+","+
                    str(codigo_livro)+")")
                conexao.commit ()
                print("Livro cadastrado com sucesso")

def remova_livro (conexao):
    """Função para remover um livro cadastrado"""
    cursor = conexao.cursor()
    nome = input("\nNome do livro? ")
    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
    linha = cursor.fetchone()
    if not linha:
        print("Livro inexistente")
    else:
        codigo_livro = linha[0]
        cursor.execute("SELECT Id FROM Autorias WHERE Codigo="+str(codigo_livro))
        linha   = cursor.fetchone()
        id_autor = linha[0]
        cursor.execute("DELETE FROM Autorias WHERE Id="     + str(id_autor))
        cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(codigo_livro))
        conexao.commit ()
        print("Autor removido com sucesso")

def liste_livros (conexao):
    """Função para listar os livros cadastrados"""
    cursor=conexao.cursor()
    cursor.execute("SELECT Livros.Nome, Autores.Nome, Livros.Preco FROM Livros, Autorias, Autores WHERE Livros.Codigo=Autorias.Codigo AND Autorias.Id=Autores.Id")

    linha = cursor.fetchone()
    if not linha:
        print ("Não há livros cadastrados")
        return

    while linha:
        print (linha[0]+" "+linha[1]+" "+str(linha[2]))
        linha = cursor.fetchone()

def main():
    """Função principal do programa"""
    print ("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")
    servidor = 'localhost/xe'
    usuario  = 'SYSTEM'
    senha    = 'system123'

    try:
        conexao = oracledb.connect(dsn=servidor,user=usuario,password=senha)
        cursor  = conexao.cursor()
    except oracledb.DatabaseError:
        print ("Erro de conexão com o BD\n")
        return
    '''
    try:
        cursor.execute("DROP TABLE Autorias")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute("DROP SEQUENCE seqAutores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute("DROP TABLE Autores")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe

    try:
        cursor.execute("DROP SEQUENCE seqLivros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequencia nao existe

    try:
        cursor.execute("DROP TABLE Livros")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela nao existe
    '''
    try:
        cursor.execute("CREATE SEQUENCE seqAutores START WITH 1 INCREMENT BY 1 MINVALUE 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except oracledb.DatabaseError:
        pass # ignora, pois a sequência já existe

    try:
        cursor.execute("CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)")
        conexao.commit()
    except oracledb.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except oracledb.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)")
        conexao.commit()
    except oracledb.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute(
            "CREATE TABLE Autorias ("\
                "Id NUMBER(3), "\
                "Codigo NUMBER(5), "\
                "FOREIGN KEY (Id) REFERENCES Autores(Id), "\
                "FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))")
        conexao.commit()
    except oracledb.DatabaseError:
        pass # ignora, pois a tabela já existe

    fim_do_programa=False
    while not fim_do_programa:
        print ("\n1) Cadastrar Autor")
        print ("2) Remover   Autor")
        print ("3) Cadastrar Livro")
        print ("4) Remover   Livro")
        print ("5) Listar    Livros")
        print ("6) Terminar\n")
        try:
            opcao = int(input("Digite sua opção: "))
        except ValueError:
            print ("Opção inválida\n")
        else:
            if opcao==1:
                cadastre_autor (conexao)
            elif opcao==2:
                remova_autor (conexao)
            elif opcao==3:
                cadastre_livro (conexao)
            elif opcao==4:
                remova_livro (conexao)
            elif opcao==5:
                liste_livros (conexao)
            elif opcao==6:
                fim_do_programa=True
            else:
                print ("Opção inválida\n")
    print ("\nOBRIGADO POR USAR ESTE PROGRAMA")

# daqui para cima  temos definições de subprogramas
# daqui para baixo temos o programa

main()
