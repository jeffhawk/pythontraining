'''
Implementar a opção 2 (procurar contato) da seguinte forma:
Ficar pedindo para digitar um nome até digitar um nome que existe;
mostrar então na tela TODOS os demais dados daquela pessoa, cujo
nome foi digitado.

Implementar a opção 3 (atualizar contato) da seguinte forma:
Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
endereco, ou telefone, ou celular, ou email, ou finalizar as
atualizações; ficar pedindo para digitar a opção até digitar uma
opção válida; realizar a atulização solicitada; até ser escolhida a
opção de finalizar as atualizações.

Entregar até domingo, dia 23 de maio de 2021.
'''
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 04/maio/2019                                  |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    nroDaOpc=1
    for opc in mnu:
        print (nroDaOpc,') ',opc,sep='')
        nroDaOpc+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', [str(opc) for opc in range(1,len(mnu)+1)])

'''
procura nom em agd e, se achou:
na posicao 0, retorna 1;
na posicao 1, retorna 2;
na posicao 2, retorna 3;
e assim por diante; MAS, se não achou e concluiu
que o lugar para inserir, mantendo a ordenacao da
lista, aquilo que foi buscado e não foi encontrado era:
a posicao 0, retorna -1;
a posicao 1, retorna -2;
a posicao 2, retorna -3;
e assim por diante.
'''
def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom==agd[meio][0]:
            return meio+1 # retornamos a posição onde entramos o que buscávamos +1
        elif nom<agd[meio][0]:
            final=meio-1
        else: # nom>agd[meio][0]
            inicio=meio+1
            
    return -(inicio+1) # retornamos, negativada, a posicao onde inserir (já que não encontramos o que procurávamos) +1

def incluir (agd):
    digitouDireito=False
    while not digitouDireito:
        nome=input('\nNome.......: ')

        posicao=ondeEsta(nome,agd)
        if posicao>0:
            print ('Pessoa já existente - Favor redigitar...')
        else:
            digitouDireito=True
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')

    posicao=-posicao
    posicao-=1
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    print('Opção não implementada!')

def atualizar (agd):
    print('Opção não implementada!')

def listar (agd):
    if agd==[]:
        print ('A agenda não possui pessoas cadastradas!')
    else:
        for contato in agd:
            print('\nNome.......:',contato[0])
            print('Aniversário:',contato[1])
            print('Endereço...:',contato[2])
            print('Telefone...:',contato[3])
            print('Celular....:',contato[4])
            print('e-mail.....:',contato[5])
        '''
        posicao=0
        while posicao<len(agd):
            print('\nNome.......:',agd[posicao][0])
            print('Aniversário:',agd[posicao][1])
            print('Endereço...:',agd[posicao][2])
            print('Telefone...:',agd[posicao][3])
            print('Celular....:',agd[posicao][4])
            print('e-mail.....:',agd[posicao][5])
            posicao+=1
        '''

def excluir (agd):
    print()
    
    digitouDireito=False
    while not digitouDireito:
        nome=input('Nome.......: ')
        
        posicao=ondeEsta(nome,agd)
        if posicao<0:
            print ('Pessoa inexistente - Favor redigitar...')
        else:
            digitouDireito=True

    posicao-=1
    
    print('Aniversario:',agd[posicao][1])
    print('Endereco...:',agd[posicao][2])
    print('Telefone...:',agd[posicao][3])
    print('Celular....:',agd[posicao][4])
    print('e-mail.....:',agd[posicao][5])

    resposta=umTexto('Deseja realmente excluir? ','Você deve digitar S ou N',['s','S','n','N'])
    
    if resposta in ['s','S']:
        del agd[posicao]
        print('Remoção realizada com sucesso!')
    else:
        print('Remoção não realizada!')

# daqui para cima, definimos subprogramas
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

agenda=[]

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa'];

opcao=None
while opcao!=6:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
        
print('OBRIGADO POR USAR ESTE PROGRAMA!')
