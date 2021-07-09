from datetime import date


class Pessoa:
    ano_atual = date.today().year
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    def falar(self, frase):
        if self.comendo:
            print(f'{self.nome} está comendo e não pode falar')
            return
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        print(f'{self.nome} está falando {frase}')
        self.falando = True


    def pararFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        print(f'{self.nome} parou de falar')
        self.falando = False


    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} está falando e não pode comer')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True


    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo!')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False


    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        from random import randint
        rand = randint(10000, 99999)
        return rand

