from aluno import Aluno
from disciplina import Disciplina

#criar / instenciar 1 aluno
aluno1 = Aluno("joão", "123456", "Ciência da Computação")

#criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "André")
dsa = Disciplina("Data Structures", "Erick")

#Matricular o aluno nas disciplinas
aluno1.matricular(sers)
aluno1.matricular(dsa)
#print(aluno1.disciplina[1].nome)

#Atribuir a(s) nota (s) de cada disciplina ao aluno
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 3)

print(aluno1.calcular_media_d(sers))