#coding: utf-8
try:
    import os
    os.chdir("C:")
    os.chdir("C:\instantclient-basic-windows.x64-19.6.0.0.0dbru\instantclient_19_6")
    '''os.chdir("C:\\Courses\\Puc\\sqldeveloper-20.4.1.407.0006-x64\\sqldeveloper")'''
    import cx_Oracle
except OSError as err:
    print("OS error: {0}".format(err))
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

def cadastreAutor (conexao):
    cursor = conexao.cursor()
    nome   = input("\nNome do autor? ")

    try:
        cursor.execute("INSERT INTO Autores (Id,Nome) VALUES (seqAutores.nextval,'"+nome+"')")
        conexao.commit()
        print("Autor cadastrado com sucesso")
    except cx_Oracle.DatabaseError:
        print("Autor repetido")


def removaAutor (conexao):
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
    

def cadastreLivro (conexao):
    cursor    = conexao.cursor()
    nomeLivro = input("\nNome do livro? ")
    
    try:
        precoLivro = float(input("Preço do livro? "))
    except ValueError:
        print("Preço inválido")
    else:   
        nomeAutor = input("Nome do autor? ")

        cursor.execute("SELECT Id FROM Autores WHERE Nome='"+nomeAutor+"'")
        linha = cursor.fetchone()
        if not linha:
            print("Autor inexistente")
        else:
            idAutor = linha[0]

            try:
                cursor.execute("INSERT INTO Livros (Codigo,Nome,Preco) VALUES (seqLivros.nextval,'"+nomeLivro+"',"+str(precoLivro)+")")
                conexao.commit ()
            except cx_Oracle.DatabaseError:
                print("Livro repetido")
            else:
                cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nomeLivro+"'")
                linha  = cursor.fetchone()
                CodigoLivro = linha[0]
                
                cursor.execute("INSERT INTO Autorias (Id,Codigo) VALUES ("+str(idAutor)+","+str(CodigoLivro)+")")
                conexao.commit ()
                print("Livro cadastrado com sucesso")

                
def removaLivro (conexao):
    cursor = conexao.cursor()
    nome = input("\nNome do livro? ")

    cursor.execute("SELECT Codigo FROM Livros WHERE Nome='"+nome+"'")
    linha = cursor.fetchone()
        
    if not linha:
        print("Livro inexistente")
    else:
        CodigoLivro = linha[0]
        
        cursor.execute("SELECT Id FROM Autorias WHERE Codigo="+str(CodigoLivro))
        linha   = cursor.fetchone()
        idAutor = linha[0]
        
        cursor.execute("DELETE FROM Autorias WHERE Id="     + str(idAutor))
        cursor.execute("DELETE FROM Livros   WHERE Codigo=" + str(CodigoLivro))
        conexao.commit ()
        
        print("Autor removido com sucesso")
    
    
def listeLivros (conexao):
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
    print ("PROGRAMA PARA PARA CADASTRAR LIVROS E SEUS AUTORES")
	
    servidor = 'localhost/xe'
    usuario  = 'SYSTEM'
    senha    = 'oracle'

    try:
        conexao = cx_Oracle.connect(dsn=servidor,user=usuario,password=senha)
        cursor  = conexao.cursor()
    except cx_Oracle.DatabaseError:
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
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a sequência já existe

    try:
        cursor.execute("CREATE TABLE Autores (Id NUMBER(3) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE SEQUENCE seqLivros START WITH 1 INCREMENT BY 1 MAXVALUE 999 NOCACHE CYCLE")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Livros (Codigo NUMBER(5) PRIMARY KEY, Nome NVARCHAR2(50) UNIQUE NOT NULL, Preco NUMBER(5,2) NOT NULL)")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    try:
        cursor.execute("CREATE TABLE Autorias (Id NUMBER(3), Codigo NUMBER(5), FOREIGN KEY (Id) REFERENCES Autores(Id), FOREIGN KEY (Codigo) REFERENCES Livros(Codigo))")
        conexao.commit()
    except cx_Oracle.DatabaseError:
        pass # ignora, pois a tabela já existe

    fimDoPrograma=False
    while not fimDoPrograma:
        print ("\n1) Cadastrar Autor")
        print ("2) Remover   Autor")
        print ("3) Cadastrar Livro")
        print ("4) Remover   Livro")
        print ("5) Listar    Livros")
        print ("6) Terminar\n")
            
        try:
            opcao = int(input("Digite sua opção: "));
        except ValueError:
            print ("Opção inválida\n")
        else:
            if opcao==1:
                cadastreAutor (conexao)
            elif opcao==2:
                removaAutor (conexao)
            elif opcao==3:
                cadastreLivro (conexao)
            elif opcao==4:
                removaLivro (conexao)
            elif opcao==5:
                listeLivros (conexao)
            elif opcao==6:
                fimDoPrograma=True
            else:
                print ("Opção inválida\n")
                
    print ("\nOBRIGADO POR USAR ESTE PROGRAMA")

# daqui para cima  temos definições de subprogramas
# daqui para baixo temos o programa

main()
