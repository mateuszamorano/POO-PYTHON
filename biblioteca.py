class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.falando = False
        self.comendo = False
        self.dormindo = False
    def falar(self):
        if self.falando == False:
            if self.dormindo == False:
                if self.comendo == False:
                    print(f"{self.nome} está falando!")
                    self.falando = True
                else:
                    print(f"{self.nome} está comendo então não pode falar!")
            else:
                print("Está dormindo então não pode falar!")
        else:
            print("Já está falando!")

    def parar_falar(self):
        print(f"{self.nome} parou de falar!")

    def dormir(self):
        if self.dormindo == False:
            if self.comendo == False:
                if self.falando == False:
                    print(f"{self.nome} está dormindo.")
                    self.comendo = True
                else:
                    print(f"{self.nome} não pode dormir, pois está falando.")
            else:
                print(f"{self.nome} não pode dormir, pois está comendo.")
        else:
            print(f"{self.nome} já está dormindo.")

        def acordar(self):
            print(f"{self.nome} acordou.")

    def pararDormir(self):
        print(f"{self.nome} parou de dormir!")

    def comer(self):
        if self.comendo == False:
            if self.dormindo == False:
                if self.falando == False:
                    print(f"{self.nome} está comendo!")
                    self.comendo = True
                else:
                    print("Está falando!")
            else:
                print("Está dormindo!")
        else:
            print("Já estava comendo!")

    def pararComer(self):
        print(f"{self.nome} parou de comer!")

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f"O {self.nome} {self.cor} está comendo!")

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} está miando!")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} está mugindo!")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} está latindo!")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} está pulando!")

class Atleta:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso
        self.aposentado = False
        self.aquecido = False

    def aquecer(self):
        print(f"{self.nome} está aquecendo!")
        self.aquecimento = False
    def aposentar(self):
        print(f"{self.nome} está aposentado!")
        self.aposentado = False
    def desaposentar(self):
        print(f"{self.nome} foi desaposentado, ou seja, terá que contribuir com o INSS novamente!")

class Ciclista(Atleta):
    def __int__(self, nome, peso):
        super().__init__(nome, peso)

    def pedalar(self):
        print(f"{self.nome} está peladando!")

class Nadador(Atleta):
    def __int__(self, nome, peso):
        super().__init__(nome, peso)

    def nadar(self):
        print(f"{self.nome} está nadando!")

class Corredor(Atleta):
    def __int__(self, nome, peso):
        super().__init__(nome, peso)

    def correr(self):
        if self.aquecido == True:
            print(f"{self.nome} está aquecido!")
            if self.aposentado == False:
                print(f"{self.nome} foi correr!")
            else:
                print(f"{self.nome} não pode correr, pois está aposentado!")
        else:
            print(f"{self.nome} não está aquecido, então, aqueça antes de correr!")

class Tri_atleta(Atleta):
    def __int__(self, nome, peso):
        super().__init__(nome, peso)

    def pedalar(self):
        print(f"{self.nome} está peladando!")

    def nadar(self):
        print(f"{self.nome} está nadando!")

    def correr(self):
        print(f"{self.nome} está correndo!")