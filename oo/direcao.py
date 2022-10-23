class Direcao:
    rotacao_a_direita_dict = {
        'Norte': 'Leste', 'Leste': 'Sul', 'Sul': 'Oeste', 'Oeste': 'Norte'
    }
    rotacao_a_esquerda_dict = {
        'Norte': 'Oeste', 'Leste': 'Norte', 'Sul': 'Leste', 'Oeste': 'Sul'
    }

    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda_dict[self.valor]

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita_dict[self.valor]
