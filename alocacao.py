from formula import *
from functions import *
from dictTostr import*

class FormulaFinal:

    def __init__(self):
	    pass

    def and_all(self, formula):
        formula_final = formula[0]
        del formula[0]
        for form in formula:
            formula_final = And(formula_final, form)
        return formula_final

    def or_all(self,formula):
        formula_final = formula[0]
        del formula[0]
        for form in formula:
            formula_final = Or(formula_final, form)
        return formula_final

    # Disciplinas do mesmo professor não podem ocorrer no mesmo horário
    def professor_horario(self, aulas):
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
        return self.and_all(restricoes)


    # Disciplinas do mesmo semenstre não podem ocorrer no mesmo horário
    def disciplina_horario(self, aulas):
        restricoes = []
        for horario in range(1, 11):
            for semestreAtual in aulas:
                for profAtual_disciplina in semestreAtual[str(list(semestreAtual.keys())[0])]:
                    for prof_disciplina in semestreAtual[str(list(semestreAtual.keys())[0])]:
                        if profAtual_disciplina == prof_disciplina:
                            continue
                        restricoes.append(Not(And(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual_disciplina["professor"] + "_" + profAtual_disciplina["disciplina"]),
                                                Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + prof_disciplina["professor"] + "_" + prof_disciplina["disciplina"]))))
        return self.and_all(restricoes)

    # Aulas alocadas em somente um horário
    def aulas_horario_not_and(self,aulas):
        restricoes = []
        for semestreAtual in aulas:
            for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
                for horarioAtual in range(1, 11):
                    for horario in range(horarioAtual + 1, 11):
                        if horarioAtual == horario:
                            continue
                        restricoes.append(Not(And(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horarioAtual) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]),
                                                Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]))))
        return self.and_all(restricoes)

    #A disciplina tem que estar em algum horário
    def aulas_horario_or(self,aulas):
        restricoes = []
        for semestreAtual in aulas:
            for profAtual in semestreAtual[str(list(semestreAtual.keys())[0])]:
                for horarioAtual in range(1, 11):
                    for horario in range(horarioAtual + 1, 11):
                        if horarioAtual == horario:
                            continue
                        restricoes.append(Or(Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horarioAtual) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"]),
                                                Atom(str(list(semestreAtual.keys())[0]) + "_" + str(horario) + "_" + profAtual["professor"] + "_" + profAtual["disciplina"])))	
        return self.or_all(restricoes)

    #retorna formula final
    def formula_final(self, aulas):
        formula_disciplina_horario = And(self.aulas_horario_or(aulas), self.aulas_horario_not_and(aulas))
        final_formula = And(And(self.professor_horario(aulas), self.disciplina_horario(aulas)), formula_disciplina_horario)
        return final_formula