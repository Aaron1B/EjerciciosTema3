def determinante_iterativo (matriz):
    a, b, c = matriz[0]
    d, e, f = matriz[1]     
    g, h, i = matriz[2]

    return (a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h)

print(determinante_iterativo( [
    [3, 1, 2],
    [4, 1, 6],
    [7, 5, 1]]))