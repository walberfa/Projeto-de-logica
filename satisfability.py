from formula import *
from functions import *
from dictTostr import *
from alocacao import *

class Funcoes:
    arrayAtom = []
    def __init__(self):
	    pass

    def atom(self, formula):
        if isinstance(formula, Atom):
            arrayAtom.append(formula.name)
            return arrayAtom
        if isinstance(formula, Not):
            return self.atom(formula.inner)
        if isinstance(formula, Implies) or isinstance(formula, And) or isinstance(formula, Or):
            return self.atom(formula.left), self.atom(formula.right)

    def truthValueOf(self, formula, definition):
        if isinstance(formula, Atom):
            return definition.get(formula.name)

        if isinstance(formula, Not):
            if self.truthValueOf(formula.inner, definition) != None:
                return not self.truthValueOf(formula.inner, definition)  
            else:
                None
        if isinstance(formula, And):
            return self.truthValueOf(formula.left, definition) and self.truthValueOf(formula.right, definition)

        if isinstance(formula, Or):
            return self.truthValueOf(formula.left, definition) or self.truthValueOf(formula.right, definition)

        if isinstance(formula, Implies):
            if self.truthValueOf(formula.left, definition) == False or self.truthValueOf(formula.right, definition) == True:
                return True
            elif self.truthValueOf(formula.left, definition) == True and self.truthValueOf(formula.right, definition) == False:
                return False
        return None

    def replaceBinary(self, valor):
	    return bin(valor).replace("0b", "")

    def stringToBoolean(self, string, trueValues=["yes", "1", "t", "true"]):
	    return string in trueValues

    def satisfability(self, formula):
        atomicas = formula.atoms()
        qntd_atoms = len(atomicas)
        qntd_valoracao = 2**qntd_atoms
        arrayValues = []
        for valor in range(qntd_valoracao):
            binary = self.replaceBinary(valor)
            arrayValues = [self.stringToBoolean(bit) for bit in binary]
            addFalse = [False] * (qntd_atoms - len(arrayValues))
            valoracaoFinal = addFalse + arrayValues
            dict_valoracoes = dict(zip(atomicas, valoracaoFinal))
        if self.truthValueOf(formula, dict_valoracoes):
            print("É satisfatível")
        else:
            print("Não é satisfatível")
