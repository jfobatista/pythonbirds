"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por duas classes
1) Motor
2) Direção
O motor tera a reponsabilidade de controlar a velocidade
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, incrementa a velocidade em 1 unidade
3) Método frear, decrementa a velocidade em 2 unidades
A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes
atributos
1) Valor de direção com valores possíveis:Norte, Sul, Leste, Oeste
2) Método girar_a_direita
3) Método girar_a_esquerda
    N
O       L
    S
Exemplo:
    
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Oeste'
"""
from motor import Motor
from direcao import Direcao


class Carro:
    def __init__(self, direcao, motor):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        return self.motor.acelerar()

    def frear(self):
        return self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor

    def girar_a_esquerda(self):
        return self.direcao.girar_a_esquerda()

    def girar_a_direita(self):
        return self.direcao.girar_a_direita()

