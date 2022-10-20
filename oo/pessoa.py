class Pessoa:
    def __init__(self, nome=None, idade=35): #criando parâmetro nome
        self.nome = nome #atributo é o self.nome, parâmetro é apenas o nome ou variável dentro do escopo
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa('Luiz')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    try:
        print(p.cumprimentar(2))  # objeto é passado implicitamente por conta do self
    except TypeError:
        print('\033[31mVocê passou mais parâmetros do que o necessário.\033[m')
    else:
        print('Deu certo!')

    print(p.nome)
    p.nome = 'João'
    print(p.nome)
    print(p.idade)
