naves = [
    {"nombre": "Cometa Veloz", "longitud": 150, "tripulantes": 10, "pasajeros": 100},
    {"nombre": "Titán del Cosmos", "longitud": 200, "tripulantes": 20, "pasajeros": 150},
    {"nombre": "nave1", "longitud": 180, "tripulantes": 15, "pasajeros": 120},
    {"nombre": "nave2", "longitud": 250, "tripulantes": 30, "pasajeros": 200},
    {"nombre": "nave3", "longitud": 170, "tripulantes": 12, "pasajeros": 100},
    {"nombre": "nave4", "longitud": 160, "tripulantes": 18, "pasajeros": 120},
    {"nombre": "nave5", "longitud": 220, "tripulantes": 25, "pasajeros": 180},
    {"nombre": "nave6", "longitud": 140, "tripulantes": 8, "pasajeros": 60},
    {"nombre": "nave7", "longitud": 160, "tripulantes": 14, "pasajeros": 90},
    {"nombre": "nave8", "longitud": 190, "tripulantes": 22, "pasajeros": 110}
]

naves_ordenadas = sorted(naves, key = lambda x: (x["nombre"], - x["longitud"] ))

for nave in naves_ordenadas:
    print(nave)

seleccion_naves = ["Cometa Veloz", "Titán del Cosmos"]
for nave in naves:
    if nave["nombre"] in seleccion_naves:
        print(nave)

naves_pasajeros = sorted(naves, key=lambda nave: nave['tripulantes'], reverse=True)

naves_pasajeros_ordenada =  naves_pasajeros[:5]
for nave in naves_pasajeros_ordenada:
    print(nave)


