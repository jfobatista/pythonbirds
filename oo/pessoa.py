class Pessoa():
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(id(p))
    try:
        print(p.cumprimentar(2)) #objeto é passado implicitamente por conta do self
    except TypeError:
        print('\033[31mVocê passou mais parâmetros do que o necessário.\033[m')
    else:
        print('Deu certo!')