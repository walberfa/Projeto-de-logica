from formula import *


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



def stringToDict(entrada):
    professor= []
    semestre=[]
    cadeira=[]
    separa = string.split()
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
    semestre= string.split('\n')
    for p in professor:
        for palavras2 in semestre:
            if p in palavras2:
                semestre.remove(palavras2)
        contador+=1
    #print(semestre)

    #separa as cadeiras
    separa=string.split(',')
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
    separa= string.split()
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

def and_all(formula):
	formula_final = formula[0]
	del formula[0]
	for form in formula:
		formula_final = And(formula_final, form)
	return formula_final

def or_all(formula):
	formula_final = formula[0]
	del formula[0]
	for form in formula:
		formula_final = Or(formula_final, form)
	return formula_final

def and_all(formula):
	formula_final = formula[0]
	del formula[0]
	for form in formula:
		formula_final = And(formula_final, form)
	return formula_final

def or_all(formula):
	formula_final = formula[0]
	del formula[0]
	for form in formula:
		formula_final = Or(formula_final, form)
	return formula_final

# Disciplinas do mesmo professor não podem ocorrer no mesmo horário
def professor_horario(aulas):
	restricoes = []
	for semestreAtual in aulas:
		for profAtual_disciplina in semestreAtual[str(list(semestreAtual.keys())[0])]:
			for horario in range(1, 11):
				for semestre in aulas:
					if semestreAtual == semestre:
						continue
					for professor_disciplina in semestre[str(list(semestre.keys())[0])]:	
						if profAtual_disciplina["professor"] == professor_disciplina["professor"]:
							restricoes.append(Not(And(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual_disciplina["professor"] + "_" + profAtual_disciplina["disciplina"]),
													Atom(str(list(semestre.keys())[0]) + "_" + str(horario) + "_" + professor_disciplina["professor"] + "_" + professor_disciplina["disciplina"]))))
	return and_all(restricoes)


# Disciplinas do mesmo semenstre não podem ocorrer no mesmo horário
def disciplina_horario(aulas):
	restricoes = []
	for horario in range(1, 11):
		for semestreAtual in aulas:
			for profAtual_disciplina in semestreAtual[str(list(semestreAtual.keys())[0])]:
				for prof_disciplina in semestreAtual[str(list(semestreAtual.keys())[0])]:
					if profAtual_disciplina == prof_disciplina:
						continue
					restricoes.append(Not(And(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual_disciplina["professor"] + "_" + profAtual_disciplina["disciplina"]),
											Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + prof_disciplina["professor"] + "_" + prof_disciplina["disciplina"]))))
	return and_all(restricoes)



# Aulas alocadas em somente um horário
def aulas_horario_not_and(aulas):
	restricoes = []
	for semestreAtual in aulas:
		for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
			for horarioAtual in range(1, 11):
				for horario in range(horarioAtual + 1, 11):
					if horarioAtual == horario:
						continue
					restricoes.append(Not(And(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horarioAtual) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]),
											Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]))))
	return and_all(restricoes)

#A disciplina tem que estar em algum horário
def aulas_horario_or(aulas):
	restricoes = []
	for semestreAtual in aulas:
		for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
			for horarioAtual in range(1, 11):
				for horario in range(horarioAtual + 1, 11):
					if horarioAtual == horario:
						continue
					restricoes.append(Or(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horarioAtual) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]),
											Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"])))	
	return or_all(restricoes)

aulas = stringToDict(string)
formula_disciplina_horario = And(aulas_horario_or(aulas), aulas_horario_not_and(aulas))
final_formula = And(And(professor_horario(aulas), disciplina_horario(aulas)), formula_disciplina_horario)
print(final_formula)