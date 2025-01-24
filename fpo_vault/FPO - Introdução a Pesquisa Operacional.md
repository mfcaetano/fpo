
#### Programando com ORTOOS

Instalando: 
https://developers.google.com/optimization/install/python/pkg_linux?hl=pt-br


Estruturando as declarações de acordo com a seguinte lógica:

1. Importação de bibliotecas e definição do ORTools solver
2. Instanciamento de Parâmetros
3. Definição das variáveis de decisão
4. Criação das restrições do problema
5. Definição da funçao objetivo
6. Executar o solver

#### Problema Slides

![[Pasted image 20250124142311.png]]

N = {Aline, Pedro, Caetano}

|N| = Quantidade, Carninalidade = N = 3

M = {Piano, Caixa de Bombom, GameBoy}
|M| = 3 = N

|             | Piano (1) | Caixa de Bombom (2) | GameBoy (3) |
| ----------- | --------- | ------------------- | ----------- |
| Aline (1)   | 30        | 50                  | 20          |
| Pedro (2)   | 80        | 15                  | 5           |
| Caetano (3) | 0.0       | -0.2                | 1.50        |

Matrix Booleana - Solução Viável 

| 0   | 1   | 0   |
| --- | --- | --- |
| 1   | 0   | 0   |
| 0   | 0   | 1   |