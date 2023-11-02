import json
import sys
import copy

def cargar_bd(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def guardar_bd(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def adivina(respuesta, rasgo):
    if respuesta == "si":
        res = True
    else:
        res = False

    to_remove = []
    for p in personajes["personajes"]:
        if p["descripcion"][rasgo] != res:
            to_remove.append(p)

    for p in to_remove:
        personajes["personajes"].remove(p)

preguntas: dict = cargar_bd('preguntas.json')
personajes: dict = cargar_bd('bd.json')
seguridad = copy.deepcopy(personajes)

num_preguntas = len(preguntas["preguntas"])

nuevo_personaje = {"nombre": None, "descripcion": {}}

print("Podre adivinar tu personaje de Avatar?")
for i in range(0, num_preguntas):
    pregunta = preguntas["preguntas"][i]
    buscar_rasgo = pregunta["rasgo"]
    respuesta = input(f"{pregunta['pregunta']} (si/no): ")
    adivina(respuesta, buscar_rasgo)
    nuevo_personaje["descripcion"][pregunta["rasgo"]] = respuesta.lower() == 's'
    
if len(personajes["personajes"]) == 1:
    print("\nTu personaje es " + personajes["personajes"][0]["nombre"])
    sys.exit()
else:
    aprende: str = input("Parece que no conozco a tu personaje, dime como se llama: ")

    if aprende.lower() != 'saltar':
        
        nuevo_personaje["nombre"] = aprende
    
        # Agrega el nuevo personaje a la lista de personajes
        seguridad["personajes"].append(nuevo_personaje)
        guardar_bd('bd.json', seguridad)
        print(f'Genial, ahora podre adivinar en un futuro a {aprende}')
