class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):  # criando parâmetro nome
        self.nome = nome  # atributo é o self.nome, parâmetro é apenas o nome ou variável dentro do escopo
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'

    @staticmethod
    def metodo_estatico(): # não coloca o atributo self, este método está atrelado apneas da classe pessoa e
        # independe do objeto(atributo de instancia)
        return 42

    @classmethod
    # Um método de classe @classmethod -> vai ter acesso a classe onde está sendo executado esse método,
    # utilizar quando quer acessar dados da sua classe,como por exemplo o nome da classe e os atributos de
    # classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_clase = super().cumprimentar()
        return f'{cumprimentar_da_clase}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    luiz = Mutante(nome='Luiz')
    joao = Homem(luiz, nome='Joao')
    print(Pessoa.cumprimentar(luiz))
    print(joao.cumprimentar())
    print(id(luiz))
    try:
        print(luiz.cumprimentar())  # objeto é passado implicitamente por conta do self
    except TypeError:
        print('\033[31mVocê passou mais parâmetros do que o necessário.\033[m')
    else:
        print('Deu certo!')
    print(joao.filhos)
    for filho in joao.filhos:
        print(filho.nome)
    joao.sobrenome = 'Batista'
    del joao.idade
    print(joao.sobrenome)
    print(joao.__dict__)
    print(luiz.__dict__)
    print(Pessoa.olhos)
    print(joao.olhos)
    print(luiz.olhos)
    print(Pessoa.metodo_estatico(), joao.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), joao.nome_e_atributos_de_classe())
    pessoa = Pessoa('A')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(joao, Pessoa))
    print(isinstance(joao, Homem))
    print(luiz.olhos)

