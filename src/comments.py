import main
import json
import os
from pathlib import Path
import random
import comments
import percents

def describirAtaque(categoriaAtaque, intensidad, coments):
    return  random.choice(coments["ataque"][categoriaAtaque].get(intensidad))

def describirDaño(categoriaAtaque, intensidad, coments):
    return random.choice(coments["recibe"][categoriaAtaque].get(intensidad))

def narrar(c1,c2,comentarios, categorias):
    #Obteniendo Strings de narración de combate.
    golpeador = percents.quienPega(c1, c2)
    golpeado = c1 if golpeador == c2 else c2
    ataque = golpeador.get("ultimoAtaque")
    categoriaGolpe = categorias["characters"][golpeador.get("nombre")]["Move_Set"].get(ataque)
    intensidad = categorias["characters"][golpeador.get("nombre")]["Move_Set"][ataque].get("Intensidad")

    descripcionAtaque = describirAtaque(categoriaGolpe, intensidad, comentarios)
    descripcionDaño = describirDaño(golpeador.get("Nombre"), categoriaGolpe, intensidad)

    #Me falta depurar y añadir más formas de estructurar las frases posibles(Ya continuaré...)
    print(f"{golpeador.get("Nombre")} {descripcionAtaque} {golpeado.get("Nombre")} {descripcionDaño}.")

if __name__ == "__main__":
    narrar()