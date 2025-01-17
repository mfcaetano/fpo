from __future__ import print_function
from ortools.linear_solver import pywraplp


solver = pywraplp.Solver('simple_lp_program', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

lb = [0,0]
ub = [1,2]
f = [3,1]
a = [1,1]
b = [2]

# Vamos criar as variaveis numericas do problema de otimizaçào
# Formato: solver.NumVar(limite inferior, limite superior, rotulo)
x1 = solver.NumVar(lb[0], ub[0], 'x1')
x2 = solver.NumVar(lb[1], ub[1], 'x2')

ct = solver.Constraint(-solver.infinity(), b[0], 'ct')

ct.SetCoefficient(x1, a[0])
ct.SetCoefficient(x2, a[1])

#definição função objetivo
objective = solver.Objective()

objective.SetCoefficient(x1, f[0])
objective.SetCoefficient(x2, f[1])

objective.SetMaximization()

solver.Solve()

print("Solução:")
print('Valor objetivo =', objective.Value())
print('x1 =', x1.solution_value())
print('x2 = ', x2.solution_value())