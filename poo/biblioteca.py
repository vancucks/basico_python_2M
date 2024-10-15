class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, andando=False, dormindo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo= False
        self.andando= False
        self.dormindo= False

    def comer (self):
        if self.comendo == False:
            if self.andando == False:
                if self.dormindo == False:
                    print("foi comer")
                    self.comendo=True
                else:
                    print("n pode comer pq ta dormindo")
            else:
                print("n pode comer pois ta andando")
        else:
            print("ja esta comendo")

    def andar (self):
        if self.andando == False:
            if self.comendo == False:
                if self.dormindo == False:
                    print("foi andar")
                    self.andando = True
                else:
                    print("n pode andar pq ta dormindo ")
            else:
                print("n pode andar pois ta comendo")
        else:
            print("ja esta andando")

    def dormir (self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.andando == False:
                    print("foi dormir")
                    self.andando = True
                else:
                    print("n pode dormir pq ta andando")
            else:
                print("n pode dormir pq ta comendo")
        else:
            print("ja esta dormindo")

class Animal:
    def __init__(self, nome, cor):
        self.nome= nome
        self.cor= cor
    def comer(self):
        print(f"{self.nome} foi comer")

class Gato(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def comer(self):
        print(f"{self.nome} toma leite")
    def miar(self):
        print(f"{self.nome} foi miar")

class Vaca(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)


    def comer(self):
        print(f"{self.nome} comendo mato")
    def mugi(self):
        print(f"{self.nome} ela faz muuuu")

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def comer(self):
        print(f"{self.nome} morde o osso")

    def late(self):
        print(f"{self.nome} late")

class Coelho(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)

    def comer(self):
        print(f"{self.nome} pulando muito")
    def grunhido(self):
        print(f"{self.nome} foi grunhiar")

class Atleta:
    def __init__(self, nome, peso):
        self.aposentado = False
        self.aquecido = False
        self.nome= nome
        self.peso= peso

    def aposentar(self):
        if self.aposentado == False:
            print(f"{self.nome} ele esta se aposentando!!")
            self.aposentado = True
        else:
            print(f"{self.nome} foi aposentado!!")

    def aquecer(self):
        if self.aquecido == False:
            print(f"{self.nome} ele esta se aquecendo!!")
            self.aquecido = True
        else:
            print(f"{self.nome} aquecido!")


class Corredor (Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print("foi correr.")
            else:
                print("ele esta aposentado :(")
        else:
            print("tem que aquecer ;)")


class Nadador(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def nadar(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print("foi nadar.")
            else:
                print("ele esta aposentado :(")
        else:
            print("tem que aquecer ;)")


class Ciclista(Atleta):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)

    def pedalar(self):
        if self.aquecido == True:
            if self.aposentado == False:
                print("foi pedalar.")
            else:
                print("ele esta aposentado :(")
        else:
            print("tem que aquecer ;)")


class TriAtleta(Corredor, Nadador,Ciclista):
    def __init__(self, nome, peso):
        super().__init__(nome, peso)






