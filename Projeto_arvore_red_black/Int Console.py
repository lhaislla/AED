from Arvore import *
##gerarCandidato()
while True:
    print ("""\033[;32;m
********************************
    1 - Cadastrar título
    2 - Cadastrar Candidato
    3 - Descadastrar título
    4 - Carregar títulos
    5 - Iniciar Votação
    6 - Resultado Parcial
    7 - Sair
    Resetar
********************************""")
    entrada=input('\033[;31;mDigite o número de sua operação: ')
    print ()
    
    if entrada=="1":#Feito
        try:
            titulo=int(input('\033[;31;mDigite o número do seu título: '))
        except(ValueError):
            print ()
            print ("\033[;36;mDIGITE APENAS NÚMEROS.")
            print ()
            continue
        titulo=str(titulo)
        if len(titulo)!=12:
            print ()
            print ("\033[;36;mTITULO INVÁLIDO.!!!")
            print ()
            continue
        else:
            busca= eleitores.buscar(eleitores.getRoot(), titulo)
            busca2=votacao.buscar(votacao.getRoot(),titulo)
            if busca2!=False and busca==False:
                print ("\033[;36;mESTA PESSOA JÁ VOTOU.")
            elif busca==False:
                noh=nodo(titulo, None, eleitores.getNone(), eleitores.getNone())
                eleitores.adicionar(noh)
                print ()
                print ("\033[;36;mTítulo adicionado com sucesso.")
            elif busca!= False:
                print ()
                print ("\033[;36;mO título já foi cadastrado.")
                print ()
                continue
    elif entrada=="2":#Feito
        print(criarcandidato())
        
    elif entrada=="3":#Feito
        titulo=input('\033[;36;mNúmero do título a ser descadastrado: ')
        busca=eleitores.buscar(eleitores.getRoot(), titulo)
        if busca==False:
            print ()
            print ('\033[;36;mTÍTULO NÃO ENCONTRADO.')
            print ()
        else:
            eleitores.rbDelete(busca)
            print ("\033[;36;mTítulo descadastrado.")

    elif entrada=="4":#Feito
        arquivo = open("\033[;36;mtitulos.txt","r")
        for i in arquivo.readlines():
            i = i.replace("\n","")
            busca=eleitores.buscar(eleitores.getRoot(),i)
            if busca==False:
                noh=nodo(i, None, eleitores.getNone(), eleitores.getNone())
                eleitores.adicionar(noh)
            else:
                continue
        arquivo.close()
        print ()
        print ("\033[;36;mTítulos adicionados.")
        print ()

    elif entrada=="5":#
        titulo=input('\033[;36;mDigite o número do título: ').upper()
        busca=eleitores.buscar(eleitores.getRoot(),titulo)
        busca2=votacao.buscar(votacao.getRoot(), titulo)
        if busca2!=False and busca==False:
            print ()
            print ('\033[;36;mESTA PESSOA JÁ VOTOU.')
            print ()
        elif busca==False:
            print ("\033[;36;mTÍTULO NÃO ENCONTRADO.")

        else:    
            print()
##            print('''***************************************
##Candidatos para Presidente do DEINFO
##            
####Nomes:              nº''')

##            arquivo=open("Printcandidatos.txt", "r")
##            for i in arquivo.readlines():
##                i = i.replace("\n","")
##                print(i)
##            arquivo.close()
            print()
            voto = input("\033[;36;mDigite o numero do seu Candidato: ")
##            arquivo=open("Printcandidatos.txt", "r")
            if voto not in listaVerif:
                print ("\033[;36;mNÚMERO INVÁLIDO.")
            else:
##                for i in arquivo.readlines():
##                    i = i.replace("\n","")
##                    i = i.split()
##                if voto in i:
                votacao.getdic()[voto][1]+=1
##                arquivo.close()
                eleitores.transferir(busca,eleitores,votacao)
                print ()
                print ("\033[;36;mVoto computado com sucesso.")
                print ()
            
    elif entrada=='6':#FEITO
        if votacao.getdic == {}:
            print("\033[;36;mNão candidato")
        else:
            for i in votacao.getdic().values():
                print("\033[;36;mNome: %s | voto(s) : %s "%(i[0],i[1]))

    elif entrada=="7":
        print ("\033[;36;mResultado final:")
        for i in votacao.getdic().values():
            print("\033[;36;mNome: %s | votos : %s "%(i[0],i[1]))
        eleitores.reset(votacao)
        titulos = open("\033[;36;mtitulos.txt","w")
        titulos.write("")
        titulos.close()
##        printCand=open("Printcandidatos.txt", "w")
##        printCand.write("")
##        printCand.close()
        print ()
        print ("\033[;36;mVOTAÇÃO ENCERRADA.")
        print ("\033[;36;mObrigado por utilizar nosso sistema. Por favor deixe sua avaliação.")
        print ("\033[;36;m0-3  >> Fraco\n4-7  >> Regular\n8-10 >> Bom")
        print ()
        nota=int(input('Nota: '))
        if nota>-1 and nota<4:
            print (":(")
        elif nota>3 and nota<8:
            print (':|')
        elif nota>7 and nota <11:
            print (':D')
        break

#imprime todos os títulos cadastrados       
    elif entrada=="10":
        eleitores.ino=""
        eleitores.inOrderAux(eleitores.getRoot())
        print (eleitores.ino)

    elif entrada=="\033[;36;mResetar":
        eleitores.reset(votacao)
        gerarCandidato()
    else:
        print ("\033[;36;mDigitou algo errado")
    
##print ()
##print (string)
