class Universo:
    def __init__(self):
        self.numMundos = 5
        self.mundos = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
        self.conexoes = []

        for i in range(self.numMundos):
            linha = []

            for j in range(self.numMundos):
                linha.append(0)
            self.conexoes.append(linha)
    
    def getCodMundo(self, nome):
        return self.mundos[nome]

    def getNomeMundo(self, i):
        for nome in self.mundos:
            if self.mundos[nome] == i:
                return nome

    def adcionarCaminho(self, inicio, fim, distancia):
        self.conexoes[self.getCodMundo(inicio)][self.getCodMundo(fim)] = distancia
    
    def mostraDistancia(self, inicio, fim):
        return self.conexoes[self.getCodMundo(inicio)][self.getCodMundo(fim)]

    def criaUniverso(self):
        self.adcionarCaminho('a', 'b', 50)
        self.adcionarCaminho('a', 'e', 70)
        self.adcionarCaminho('a', 'd', 50)
        self.adcionarCaminho('b', 'c', 40)
        self.adcionarCaminho('c', 'd', 40)
        self.adcionarCaminho('c', 'e', 20)
        self.adcionarCaminho('d', 'c', 40)
        self.adcionarCaminho('d', 'e', 80)
        self.adcionarCaminho('e', 'b', 30)
    
    def getVizinhos(self, mundo):
        vizinhos = []

        for i in range(self.numMundos):
            if self.conexoes[self.getCodMundo(mundo)][i] > 0:
                vizinhos.append(self.getNomeMundo(i))

        return vizinhos

novinhos = Universo()

novinhos.criaUniverso()

print(novinhos.getVizinhos('e'))
print(novinhos.mostraDistancia('a', 'b'))
