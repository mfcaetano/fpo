# Problema:
# max  3x1 + 5x2 
# s.t.
# 	x1 <= 4
#       x2 <= 6
# 	3x1 + 2x2 <= 18

from __future__ import print_function
from ortools.linear_solver import pywraplp

#solver considerando o Google's Linear Optimization Programming system (GLOP)
solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

#Definição dos parâmetros
# n   = |C| (Cardinal do conjunto C - Número de elementos do conjunto )
# Ei  = [Ea, Eb, Ec, ..., En] - Limite superior para cada elemento de C
# Li  = [La, Lb, Lc, ..., Ln] - Coeficientes da função objetivo para cada elemento de C
# Ti  = [Ta, Tb, Tc, ..., Tn] - Valor proporcional para cada elemento de C
# T   = Valor do somatório de Ti's

#2 Passo - Parametrização
n = int(input())
ub = [float(input()) for i in range(n)]
f = [float(input()) for i in range(n)]
ti = [float(input()) for i in range(n)]
T = float(input())


#lb = [0,0]   # x1, x2 >= 0
#ub = [4,6]  # x1 <= 4; 2x2 <= 12 (normalizando x2)
#f = [3,5]    # 3x1 + 5x2
#a = [3,2]    # 3x1 + 2x2 <= 18
#b = [18]     # 3x1 + 2x2 <= 18

# Vamos criar as variaveis numericas do problema de otimizaçào
# Formato: solver.NumVar(limite inferior, limite superior, rotulo)
#x1 = solver.NumVar(lb[0], ub[0], 'x1')
#x2 = solver.NumVar(lb[1], ub[1], 'x2')

x = [solver.NumVar(0, ub[i], f'x{i+1}') for i in range(n)]

ct = solver.Constraint(-solver.infinity(), T, 'ct')

for i in range(n):
	ct.SetCoefficient(x[i], ti[i])

#ct.SetCoefficient(x1, a[0])
#ct.SetCoefficient(x2, a[1])

#definição função objetivo
objective = solver.Objective()

#objective.SetCoefficient(x1, f[0])
#objective.SetCoefficient(x2, f[1])
for i in range(n):
	objective.SetCoefficient(x[i], f[i])

objective.SetMaximization()

solver.Solve()

#Imprimiremos a solucao
print('Solucao:')
print('Valor objetivo =', "{:.1f}".format(objective.Value()))
for i in range(n):
    print(x[i], "=", "{:.1f}".format(x[i].solution_value()))