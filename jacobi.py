# matriz = [ [int(input("digite um number")) for i in range(x)] for j in range(x)]


def jacobi(matriz):
  for i in range(len(matriz)):
    divisor = matriz[i][i]
    for j in range(len(matriz[i])):
      if j == i:
        matriz[i][j] = 0
      elif j == len(matriz[i])-1:
        matriz[i][j] /= divisor
      else:
        matriz[i][j] = (-matriz[i][j]/divisor)
  
  for i in range(i):
    for j in range(j):
  
    x = 1/matriz[i][i]
  
  
  return matriz

x = [
  [10, -1, 2, 0, 6],
  [-1, 11, -1, 3, 25],
  [2, -1, 10, -1, -11],
  [0, 3, -1, 8, 15]
  ]

x = jacobi(x)
print(*x)