def f(n, x_values, fx_values):
    for i in range(1, n):
        for j in range(1, i):
            fx_values[i][j] = fx_values[i][j - 1]/ x_values[i] - x_values[i - j]
    return fx_values


def newton(x, x_values, fx_values):
    resultado = fx_values[0][0]
    fx = f(len(x_values), x_values, fx_values)
    for i in range(1, len(x_values)):
        temp_mult = 1
        for j in range(i - 1):
            temp_mult *= (x - x_values[j])
        resultado +=  fx[0][1] * temp_mult
    return resultado


#(x)
x_values = [1.0, 1.3 ,1.6, 1.9, 2.2] 

#f(x) 
fx_values = [
    [0.7651977] + [0] * (len(x_values) - 1),
    [0.6200860] + [0] * (len(x_values) - 1), 
    [0.4554022] + [0] * (len(x_values) - 1),
    [0.2818186] + [0] * (len(x_values) - 1),
    [0.1103623] + [0] * (len(x_values) - 1)
    ]

print(newton(1, x_values, fx_values))

print(fx_values)
