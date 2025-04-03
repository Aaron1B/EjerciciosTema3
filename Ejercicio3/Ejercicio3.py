naves = [
    {"nombre": "Cometa Veloz", "longitud": 50, "tripulantes": 4, "pasajeros": 6},
    {"nombre": "Titán del Cosmos", "longitud": 55, "tripulantes": 6, "pasajeros": 7},
    {"nombre": "nave1", "longitud": 45, "tripulantes": 4, "pasajeros": 5},
    {"nombre": "nave2", "longitud": 60, "tripulantes": 5, "pasajeros": 4},
    {"nombre": "nave3", "longitud": 50, "tripulantes": 4, "pasajeros": 6},
    {"nombre": "nave4", "longitud": 48, "tripulantes": 5, "pasajeros": 5},
    {"nombre": "nave5", "longitud": 59, "tripulantes": 6, "pasajeros": 7},
    {"nombre": "nave6", "longitud": 40, "tripulantes": 3, "pasajeros": 3},
    {"nombre": "GXnave7", "longitud": 45, "tripulantes": 4, "pasajeros": 5},
    {"nombre": "nave8", "longitud": 52, "tripulantes": 5, "pasajeros": 6},
    
]


naves_ordenadas = sorted(naves, key = lambda x: (x["nombre"], - x["longitud"] ))

for nave in naves_ordenadas:
    print(nave)

seleccion_naves = ["Cometa Veloz", "Titán del Cosmos"]
for nave in naves:
    if nave["nombre"] in seleccion_naves:
        print(nave)

naves_pasajeros = sorted(naves, key=lambda nave: nave['pasajeros'], reverse=True)

naves_pasajeros_ordenada =  naves_pasajeros[:5]
for nave in naves_pasajeros_ordenada:
    print(nave)

naves_tripulantes = sorted(naves, key =lambda nave: nave['tripulantes'], reverse=True)
naves_tripulantes_ordenada = naves_tripulantes[0]
for nave in naves_tripulantes_ordenada:
    print(nave)

naves_gx = [nave for nave in naves if nave["nombre"].startswith("GX")]
for nave in naves_gx:
    print(nave)

naves_6 = [nave for nave in naves if nave["tripulantes"]  >= 6]
for nave in naves_6:
    print(nave)

nave_pequeña = min(naves, key =lambda nave: nave["longitud"])
nave_grande = max(naves, key = lambda nave: nave["longitud"])
print(nave_pequeña)
print(nave_grande)





