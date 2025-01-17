# Problema:
# max  3x1 + 5x2 
# s.t.
# 	x1 <= 4
#       x2 <= 6
# 	3x1 + 2x2 <= 18

from __future__ import print_function
from ortools.linear_solver import pywraplp
import random

#solver considerando o Google's Linear Optimization Programming system (GLOP)
solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Definição dos parâmetros
# n   = |C| (Cardinal do conjunto C - Número de elementos do conjunto )
# Ei  = [Ea, Eb, Ec, ..., En] - Limite superior para cada elemento de C
# Li  = [La, Lb, Lc, ..., Ln] - Coeficientes da função objetivo para cada elemento de C
# Ti  = [Ta, Tb, Tc, ..., Tn] - Valor proporcional para cada elemento de C
# T   = Valor do somatório de Ti's

#2 Passo - Parametrização

#n = int(input())
#ub = [float(input()) for i in range(n)]
#f = [float(input()) for i in range(n)]
#ti = [float(input()) for i in range(n)]
#T = float(input())

N = 100 #random.randint(1,4)
Li = [random.randint(1,10) for i in range(N)]
Ei = [random.randint(4,8) for i in range(N)]
T = random.randint(10, 20)
Ti = [random.randint(1,4) for i in range(N)]
LB = [0 for i in range(N)]

#N = 2
#Ei = [4, 6]
#Li = [3, 5]
#Ti = [3,2]
#T = 18
#LB = [0,0]

print("Li =", Li)
print("Ei =", Ei)
print("T = ", T)
print("Ti =", Ti)
print("LB =", LB)


def modelo_otimo(N, Li, Ei, T, Ti, LB):
	#Passo 3 - variáveis de decisão
	xi = [solver.NumVar(-solver.infinity(), solver.infinity(), f'x{i+1}') for i in range(N)]

	#Passo 4 - Restrições
	r = 0
	for i in range(N):
		ct = solver.Constraint(-solver.infinity(), Ei[i], f'ct{r}')
		r += 1
		ct.SetCoefficient(xi[i], 1)

	ct = solver.Constraint(-solver.infinity(), T, f'ct{r}')
	r += 1

	for i in range(N):
		ct.SetCoefficient(xi[i], Ti[i]) # Sum Tixi

	for i in range(N):
		ct = solver.Constraint(0, solver.infinity(), f'ct{r}') #xi > 0
		r += 1
		ct.SetCoefficient(xi[i], 1) # xi > 0

	# Passo 5 - Definir função Objetivo
	objective = solver.Objective()

	for i in range(N):
		objective.SetCoefficient(xi[i], Li[i]) # LiXi

	objective.SetMaximization()


	# Passo 6 - Executar e imprimir
	res = solver.Solve()

	if res == 0:

		#Imprimiremos a solucao
		print('Solucao:')
		print('Valor objetivo =', objective.Value())

		for i in range(N):
			print(xi[i], "=", xi[i].solution_value())
	else:
		print("Problema Insoluvel")

modelo_otimo(N, Li, Ei, T, Ti, LB)
