from formula import *
from functions import *

class ManipulacaoEntrada:

    def __init__(self):
	    pass

    def stringToDict(self, entrada):
        professor= []
        semestre=[]
        cadeira=[]
        separa = entrada.split()
        contador=0
        quant_cadeiras = []
        arry_prof=[]
        dict_semestr = {}
        array_semestr = []
        dict_disciplin = {}
        sem=0
        prof=0

        #separa os professores
        for palavras in separa:
            contador=contador+1
            if palavras[-1]==',':
                professor.append(separa[contador])
        #print(professor)

        #sepra os semestres
        semestre= entrada.split('\n')
        for p in professor:
            for palavras2 in semestre:
                if p in palavras2:
                    semestre.remove(palavras2)
            contador+=1
        #print(semestre)

        #separa as cadeiras de professores
        separa=entrada.split(',')
        axl=[]
        contador=0

        for d in separa:
            axl.append(separa[contador].split('\n'))
            contador+=1
        for h in axl:
            for j in h:
                cadeira.append(j)
        for a in cadeira:
            for pro in professor:
                if a == ' '+pro :
                    cadeira.remove(a)

        for a in cadeira:
            for pro in semestre:
                if a == pro :
                    cadeira.remove(a)

        #quantas cadeiras tem em cada semestre
        separa= entrada.split()
        x=0
        axl=[]
        for se in semestre[::-1]:
            for sep in separa[::-1]:
                if ',' in sep:
                    x+=1
                if se == sep:
                    for qt in axl:
                        x=x-qt
                    axl.append(x)
            x=0
        for ax in axl[::-1]:
            quant_cadeiras.append(ax)

        #transforma cada parte em dict
        for se in range(len(semestre)):
            cad =int(quant_cadeiras[se])
            sem=0
            while sem != cad :
                dic_cadeiras={'professor': professor[prof],'disciplina' : cadeira[prof]}
                arry_prof.append(dic_cadeiras)
                sem+=1
                prof+=1
            array_semestr.append({semestre[se]:arry_prof})
            arry_prof=[]
        return array_semestr
