p1 = [(3, 2), (2, 1), (1, 0)]  # 3x^2 + 2x + 1
p2 = [(1, 1), (1, 0)]          # x + 1

def restar_polinomios(p1, p2):

    p1_dict = {exponente: coeficiente for coeficiente, exponente in p1}
    p2_dict = {exponente: coeficiente for coeficiente, exponente in p2}

    resultado = {}
    exponentes = set(p1_dict.keys()).union(set(p2_dict.keys()))

    for exponente in exponentes:
        co1 = p1_dict.get(exponente, 0)
        co2 = p2_dict.get(exponente, 0)
        resultado[exponente] = co1 - co2

    resultado_f = [(coeficiente, exponente) for exponente, coeficiente in resultado.items() if coeficiente != 0]

    return resultado_f

def dividir_polinomios(p1, p2):
    p1 = sorted(p1, key =lambda x: -x[1])
    p2 = sorted(p2, key =lambda x: -x[1])

    resultado = []
    grado_p1 = p1[0][1]
    grado_p2 = p2[0][0]

    while p1 and p1[0][1] >= grado_p1:
        co1 , exp1 = p1[0]

        coef_quotient = co1 / grado_p2
        exp_quotient = exp1 - grado_p1
        
        resultado.append((coef_quotient, exp_quotient))
        
        subtract_term = [(coef_quotient * coef, exp_quotient + exp) for coef, exp in p2]
        
        p1 = restar_polinomios(p1, subtract_term)
    
    return resultado

def eliminar(p, exp_e):
    return [(coef, exp) for coef, exp in p if exp != exp_e]

def existe(p, exp_e):
    return any(exp == exp_e for _, exp in p)

print(restar_polinomios(p1, p2))
print(dividir_polinomios(p1, p2))
print(eliminar(p1, 2))
print(existe(p1, 2))
