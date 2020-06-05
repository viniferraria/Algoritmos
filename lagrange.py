def lagrange(x, fx_values, x_values):
    resultado = 0
    for k in range(len(x_values)):
        temp_x = 1
        temp_y = 1
        for i in range(len(x_values)):
            if i != k:
                temp_x *= (x - x_values[i])
                temp_y *= (x_values[k] - x_values[i])
        resultado += (temp_x/temp_y) * fx_values[k]
    return resultado



def main():
    func1 = list(map(float, input().split()))[0:5] 
    func2 = list(map(float, input().split()))[0:5]
    func3 = list(map(float, input().split()))[0:5]
    func4 = list(map(float, input().split()))[0:5]