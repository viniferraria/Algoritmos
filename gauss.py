# def pivotamento(matriz):
#     if matriz[0][0] == 0:
#         return "No unique solutions"
#     else:    
#         for i in range(1, len(matriz) - 1):
#             for j in range(i+1, len(matriz)):
#                 x = -(matriz[j][i]/matriz[i][i])
#                 for k in range(len(matriz)):
#                     matriz[j][k] += x * matriz[i][k]
#     return matriz

def pivotamento(matriz):
    for i in range(1, len(matriz) - 1):
        for j in range(i+1, len(matriz)):
            x = -(matriz[j][i]/matriz[i][i])
            for k in range(len(matriz)):
                matriz[j][k] += x * matriz[i][k]
    return matriz

matrix = [
    [2, 0, 0, 0, 3],
    [1, 1.5, 0, 0, 4.5],
    [0, -3, 0.5, 0, -6.6],
    [2, -2, 1, 1, 0.8]
]
x = pivotamento(matrix)
print(*x)