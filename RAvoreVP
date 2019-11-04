class nodo():
    def __init__(self, dados, pai=None, esquerdo= None, direito = None,cor = "black" ):
        self.__dados = dados
        self.__pai = pai
        self.__esquerdo = esquerdo
        self.__direito = direito
        self.__cor = cor
        self.__nivel = 0
    def getDado(self):
        return self.__dados
    
    def getPai(self):
        return self.__pai
        
    def getEsquerdo(self):
        return self.__esquerdo
        
    def getDireito(self):
        return self.__direito
    
    def setPai(self, painovo):
        self.__pai = painovo
        
    def setDireito(self, direitonovo):
        self.__direito = direitonovo      
        
    def setEsquerdo(self, Esquerdonovo):
        self.__esquerdo = Esquerdonovo
        
    def setDados(self, dadonovo):
        self.__pai = dadonovo
    
    def getCor(self):
        return self.__cor
    
    def setCor(self,novacor):
        self.__cor = novacor
    
    
    
    def getnivel(self):
        return self.nivel
    
    def setNivel(self,nivelnovo):
        self.__nivel = nivelnovo
        
class arvore():
    
    def __init__(self):
        self.__none = nodo(None)
        self.__none.setDireito(self.__none)
        self.__none.setEsquerdo(self.__none)
        self.__none.setPai(self.__none)
        self.__root = self.__none
        self.pos,self.pre,self.ino = "","",""
        self.__dic={}
    def getNone(self):
        return self.__none
        
    def setRoot(self,nodo):
        self.__root = nodo
    def getdic(self):
        return self.__dic
    def getRoot(self):
        return self.__root
    
    def adicionar(self, nodo):
        y = self.__none
        x = self.__root
        
        while x != self.__none:
            y = x 
            if nodo.getDado() < x.getDado():
                x = x.getEsquerdo()
            else:
                x = x.getDireito()
        nodo.setPai(y)
        if y == self.__none:
            self.__root = nodo
        elif nodo.getDado() < y.getDado():
            y.setEsquerdo(nodo)
        else:
            y.setDireito(nodo)
        nodo.setEsquerdo(self.__none)
        nodo.setDireito(self.__none)
        nodo.setCor("red")
        self.insertAux(nodo)    
                 
    def insertAux(self,nodo):
        while nodo.getPai().getCor() == "red":
            if nodo.getPai() == nodo.getPai().getPai().getEsquerdo():
                y = nodo.getPai().getPai().getDireito()
                if y.getCor() == "red":
                    nodo.getPai().setCor("black")
                    y.setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    nodo = nodo.getPai().getPai()
                else:
                    if nodo == nodo.getPai().getDireito():
                        nodo = nodo.getPai()
                        self.rotacaoEsquerda(nodo)
                    nodo.getPai().setCor("black")
                    nodo.getPai().getPai().setCor("red")
                    self.rotacaoDireita(nodo.getPai().getPai())
            else:
                if nodo.getPai() == nodo.getPai().getPai().getDireito():
                    y = nodo.getPai().getPai().getEsquerdo()
                    if y.getCor() == "red":
                        nodo.getPai().setCor("black")
                        y.setCor("black")
                        nodo.getPai().getPai().setCor("red")
                        nodo = nodo.getPai().getPai()
                    else:
                        if nodo == nodo.getPai().getEsquerdo():
                            nodo = nodo.getPai()
                            self.rotacaoDireita(nodo)
                        nodo.getPai().setCor("black")
                        nodo.getPai().getPai().setCor("red")
                        self.rotacaoEsquerda(nodo.getPai().getPai())
        self.__root.setCor("black")       
                 
    def minimo(self,raiz):
        temp = raiz
        
        while temp.getEsquerdo() != self.__none:
        
            temp = temp.getEsquerdo()
        
        return temp
    
    def maximo(self,raiz):
    
        temp = raiz
        
        while temp.getDireito() != self.__none:
        
            temp = temp.getDireito()
        return temp
          
    def info(self, nodo):
        return nodo.getDado()
    
    def filhoEsquerdo(self, nodo):
        return nodo.getEsquerdo()
    
    def filhoDireito(self, nodo):
        return nodo.getDireito()
    
    def pai(self, nodo):
        return nodo.getPai()
    
    def ehEsquerdo(self, nodo):
        a = arvore.pai(nodo)
        if a == None:
            return "naoTemPai"
        if a.filhoEsquerdo() == nodo:
            return True
        else:
            return False
        
    def ehDireito(self, nodo):
        a = arvore.ehEsquerdo(nodo)
        if a == "naoTemPai":
            return False
        
        if a == False:
            return True
        else:
            return False   
        
    def irmao(self, nodo):

        a = arvore.ehEsquerdo(nodo)
        p = arvore.pai(nodo)
        if p == None:
            return False
        if a == True:
            return p.filhoDireito()
        else:
            return p.filhoEsquerdo()
        
    def sucessor(self,nodo):
        temp = nodo
        
        if temp.getDireito() != self.__none:
            return self.minimo(temp.getDireito())
        y = temp.getPai()
        while y != self.__none and nodo == y.getDireito():
            nodo = y
            y = y.getPai()
        return y
    
    def predecessor(self,nodo):
        temp = nodo
        if temp.getDireito() != self.__none:
            return self.maximo(temp.getEsquerdo())
        y = temp.getPai()
        while y != self.__none and nodo == y.getDireito():
            nodo = y
            y = y.getPai()
        return y
    
    def transplante (self,u,v):
        if u.getPai() == self.__none:
            self.__root = v
        elif u == u.getPai().getEsquerdo():
                u.getPai().setEsquerdo(v)
        else:
            u.getPai().setDireito(v)
        v.setPai(u.getPai())
                                          
    def rbDelete(self,nodo):
        y = nodo
        origCor = y.getCor()
        if nodo.getEsquerdo() == self.__none:
            x = nodo.getDireito()
            self.transplante(nodo,nodo.getDireito())
        elif nodo.getDireito()==self.__none:
            x = nodo.getEsquerdo()
            self.transplante(nodo, nodo.getEsquerdo())
        else:
            y = self.maximo(nodo.getDireito())
            origCor = y.getCor()
            x = y.getDireito()
            if y.getPai() == nodo:
                x.setPai(y)
            else:
                self.transplante(y, y.getDireito())
                y.setDireito(nodo.getDireito())
                y.getDireito().setPai(y)
            self.transplante(nodo, y)
            y.setEsquerdo(nodo.getEsquerdo())
            y.getEsquerdo().setPai(y)
            y.setCor(nodo.getCor())
        if origCor == "black":
            self.deleteFix(x)
            
    def deleteFix(self,nodo):
        while nodo != self.__root and nodo.getCor() == 'black':
            if nodo == nodo.getPai().getEsquerdo():
                w = nodo.getPai().getDireito()
                if w.getCor()== 'red':
                    w.setCor('black')
                    nodo.getPai().setCor('red')
                    self.rotacaoEsquerda(nodo.getPai())
                    w = nodo.getPai().getDireito()
                    
                if w.getEsquerdo().getCor() == 'black' and  w.getDireito().getCor() == 'black':
                    w.setCor('red')
                    nodo = nodo.getPai()
                else:
                    if w.getDireito().getCor()=='black':
                        w.getEsquerdo().setCor('black')
                        w.setCor('red')
                        self.rotacaoDireita(w)
                        w = nodo.getPai().getDireito()
                    w.setCor(nodo.getPai().getCor())
                    nodo.getPai().setCor('black')
                    w.getDireito().setCor('black')
                    self.rotacaoEsquerda(nodo.getPai())
                    nodo = self.__root
            else:
                w = nodo.getPai().getEsquerdo()
                if w.getCor()== 'red':
                    w.setCor('black')
                    nodo.getPai().setCor('red')
                    self.rotacaoDireita(nodo.getPai())
                    w = nodo.getPai().getEsquerdo()
                    
                if w.getDireito().getCor() == 'black' and  w.getEsquerdo().getCor() == 'black':
                    w.setCor('red')
                    nodo = nodo.getPai()
                else:
                    if w.getEsquerdo().getCor()=='black':
                        w.getDireito().setCor('black')
                        w.setCor('red')
                        self.rotacaoEsquerda(w)
                        w = nodo.getPai().getEsquerdo()
                    w.setCor(nodo.getPai().getCor())
                    nodo.getPai().setCor('black')
                    w.getEsquerdo().setCor('black')
                    self.rotacaoDireita(nodo.getPai())
                    nodo = self.__root
        nodo.setCor('black')        
    def buscar(self, raiz, numeroTitulo):
        if numeroTitulo==raiz.getDado():
            return raiz
        elif raiz.getDado()==self.__none.getDado():
            return False
        
        elif numeroTitulo<raiz.getDado():
            return self.buscar(raiz.getEsquerdo(), numeroTitulo)
        else:
            return self.buscar(raiz.getDireito(), numeroTitulo)                         
    def preOrder(self):
        "Caminho percorrido em Pre-Ordem"
        self.preOrderAux(self.__root)

    def preOrderAux(self, nodo):
        "Funcao auxiliar para o percuso em Pre-Ordem"
        if nodo is not self.__none:
            self.pre+= str(nodo.getDado()) + " "
            self.preOrderAux(nodo.getEsquerdo())
            self.preOrderAux(nodo.getDireito())

    def inOrder(self):
        "Caminho percorrido em Ordem"
        self.inOrderAux(self.__root)

    def inOrderAux(self, nodo):
        "Funcao auxiliar para percuso em Ordem"
        if nodo is not self.__none:
            self.inOrderAux(nodo.getEsquerdo())
            self.ino+= str(nodo.getDado()) + " "
            self.inOrderAux(nodo.getDireito())

    def posOrder(self):
        "Caminho percorrido em Pos-Ordem"
        self.posOrderAux(self.__root)

    def posOrderAux(self, nodo):
        "Funcao auxiliar para percurso em Pos-Ordem"
        if nodo is not self.__none:
            self.posOrderAux(nodo.getEsquerdo())
            self.posOrderAux(nodo.getDireito())
            self.pos+= str(nodo.getDado()) +" "
    
    def altura(self,nodo):
        if nodo == self.__none:
            return -1
        h1 = self.altura(nodo.getEsquerdo())
        h2 = self.altura(nodo.getDireito())
        return 1+max(h1,h2)
    
    def fatorBala(self,nodo):
        e = self.altura(nodo.getEsquerdo())
        d = self.altura(nodo.getDireito())
        return d-e
    
    def rotacaoEsquerda(self,nodo):
        y = nodo.getDireito()
        nodo.setDireito(y.getEsquerdo())
        if y.getEsquerdo() != self.__none:
            y.getEsquerdo().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai() == self.__none:
            self.__root = y
        elif nodo == nodo.getPai().getEsquerdo():
            nodo.getPai().setEsquerdo(y)
        else:
            nodo.getPai().setDireito(y)
        y.setEsquerdo(nodo)
        nodo.setPai(y)
           
    def rotacaoDireita(self,nodo):
        y = nodo.getEsquerdo()
        nodo.setEsquerdo(y.getDireito())
        if y.getDireito() != self.__none:
            y.getDireito().setPai(nodo)
        y.setPai(nodo.getPai())
        if nodo.getPai()== self.__none:
            self.setRoot(y)
        elif nodo == nodo.getPai().getDireito():
            nodo.getPai().setDireito(y)
        else:
            nodo.getPai().setEsquerdo(y)
        y.setDireito(nodo)
        nodo.setPai(y)
        
    def transferir(self,nod,arvoreO,arvoreT):
        
        dado = nod.getDado()
        novo = nodo(dado)
        arvoreO.rbDelete(nod)
        arvoreT.adicionar(novo)
      
    def reset(self,arvorev):
        arvorev.__root = self.__none
        arvorev.self__dic={}


###########   FUNÇÕES AUXILIARES    ################
listaVerif=[]
def criarcandidato():
    while True:            
        nome=input("Digite o Nome do Candidato: ")
        numero=input("Digite o Numero do Candidato: ")
        if numero.isnumeric() == True and len(numero)==2:
            if numero not in votacao.getdic():
                votacao.getdic()[numero]=[nome,0]
                listaVerif.append(numero)
                break
            else:
                print("erro!!! Numero do Candidato já Cadastrado")
        elif len(numero)!=2:
            print("erro!!! digite novamente")
        else:
            print("erro!!! digite novamente")
            continue
##    arquivo= open("Printcandidatos.txt", "a")
##    a = '\n'+nome+" "+numero
##    arquivo.write(a)
##    arquivo.close()
    return "\nCandidato Cadastrado com Sucesso"
def pedirtitulo():
    titulo=input('Digite o número do título: ')
    return titulo
##def gerarCandidato():
##    arquivo = open("candidatos.txt","r")
##    for i in arquivo.readlines():
##        i = i.replace("\n","")
##        i = i.split()
##        votacao.getdic()[i[1]]=[i[0],0]
##    arquivo.close()
   
#============================================================
eleitores = arvore()
votacao= arvore()
##
##lista=[100,90,80,70,91,89,92,110,102,111]
##for x in lista:
##    a = nodo(x)
##    eleitores.adicionar(a)
##
##print(eleitores.getRoot().getDado())
###eleitores.rbDelete(eleitores.getRoot())
##eleitores.transfetir(eleitores.getRoot(), eleitores, votacao)
##print(eleitores.getRoot().getDado())
##print(votacao.getRoot().getDado())
##
##eleitores.inOrder()
##print(eleitores.ino)
##eleitores.reset(eleitores)
##
##votacao.reset(votacao)
##print(eleitores.getRoot().getEsquerdo().getDado())
