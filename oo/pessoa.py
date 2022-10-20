class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35): #criando parâmetro nome
        self.nome = nome #atributo é o self.nome, parâmetro é apenas o nome ou variável dentro do escopo
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    luiz = Pessoa(nome='Luiz')
    joao = Pessoa(luiz, nome='Joao')
    print(Pessoa.cumprimentar(luiz))
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
    luiz.olhos = 1
    print(joao.sobrenome)
    print(joao.__dict__)
    print(luiz.__dict__)
    print(Pessoa.olhos)
    print(joao.olhos)
    print(luiz.olhos)
