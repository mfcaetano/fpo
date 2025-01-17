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

#2 Passo - Parametrização
# Limiares Inferiores
lb = [0,0]   # x1, x2 >= 0
# Limiares Superiores
ub = [4,6]  # x1 <= 4; 2x2 <= 12 (normalizando x2)
# 3, 5 função objetivo
f = [3,5]    # 3x1 + 5x2
# Relacionamento
a = [3,2]    # 3x1 + 2x2 <= 18
b = [18]     # 3x1 + 2x2 <= 18

# Vamos criar as variaveis numericas do problema de otimizaçào
# Formato: solver.NumVar(limite inferior, limite superior, rotulo)
#3 Passo: Determinar as variáveis de decisão
x1 = solver.NumVar(lb[0], ub[0], 'x1')
x2 = solver.NumVar(lb[1], ub[1], 'x2')

#4 Passo: Determinar as restrições do Problema
# 3x1 + 2x2 <= 18
ct = solver.Constraint(-solver.infinity(), b[0], 'ct')
ct.SetCoefficient(x1, a[0])
ct.SetCoefficient(x2, a[1])

#5 Passo - Definição função objetivo
objective = solver.Objective()

objective.SetCoefficient(x1, f[0])
objective.SetCoefficient(x2, f[1])

objective.SetMaximization()

#6 Passo - Executar o Solver
solver.Solve()

#Imprimiremos a solucao
print('Solucao:')
print('Valor objetivo =', objective.Value())
print('x1 =', x1.solution_value())
print('x2 =', x2.solution_value())