
# 
# Problema de Associação 
#
# max \sum_{(i,j) \in N} aij xij
#
# \sum_{j | (i,j) \in N} xij = 1 \forall i = 1, ..., n
#
# \sum{i | (i,j) \in N} xij = 1 \forall j = 1, ..., n
#
# 0 \leq xij \leq 1 \forall (i,j) \in N.



import numpy as np

N = np.array([[30,50,20],[80,15,5],[0.0, -0.2,1.50]])

# xij = 1 determina se a pessoa i recebe o presente j; 0 caso contrário
M = np.array([[0,1,0],[1,0,0],[0, 0, 1]])

for linha in N*M:
	print(linha)

