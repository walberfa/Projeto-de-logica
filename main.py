from formula import *
from functions import *
from dictTostr import *
from alocacao import *
from satisfability import *


def main():
    #A entrada vai ser nessa string
    string = """s1
    Circuitos Digitais, Carlos
    Fundamentos de Programação, Daniel
    s2
    Laboratório de Programação, Samuel
    s3
    POO, Marcio
    Programação Linear, Ana
    s4
    Lógica para Computaçãp, João
    Comunicação de Dados, Jos ́e
    Estruturas de Dados, Tomás
    s5
    Análise de Algoritmos, Alice
    Grafos, Alice
    Sistemas Operacionais, Carlos
    Eletrônica, Santos
    Engenharia de Software, Marcio
    s6
    Linguagens de Programação, Fernanda
    Teoria da Computação, João
    Sistemas Embarcados, Santos
    Redes, Tomás"""

    strTodict = ManipulacaoEntrada()
    aulas = strTodict.stringToDict(string)
    formula = FormulaFinal()
    formula_final = formula.formula_final(aulas)
    satisfatibilidade = Funcoes()
    reposta_final = satisfatibilidade.satisfability(formula_final)