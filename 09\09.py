class Pessoa:
    def __init__(self, nome, peso, idade, comendo=False, andando=False, dormindo=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo= comendo
        self.andando= andando
        self.dormindo= dormindo

    def andar (self):
        if self.andando == False:
            print("foi andar")
            self.andando = True
        else:
            print("ja esta andando")

    def comer (self):
        if self.comendo == False:
            print("foi comer")
            self.comendo=True
        else:
            print("ja esta comendo")

    def dormir (self):
        if self.dormindo == False:
            print("foi dormir")
            self.dormindo = True
        else:
            print("ja esta dormindo")
            



p1= Pessoa("nome",83,25)
p1.dormir()
p1.dormir()

