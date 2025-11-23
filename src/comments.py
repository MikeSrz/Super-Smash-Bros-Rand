import main
import json
import os
from pathlib import Path
import random
import comments
import percents

def describirAtaque(categoriasAtaque, intensidad, coments):
    return  random.choice(coments["ataque"][categoriasAtaque].get(intensidad))

def describirDaño(categoriaAtaque, intensidad, coments):
    return random.choice(coments["recibe"][categoriaAtaque].get(intensidad))

def narrar(c1,c2,comentarios, categorias):
    #Obteniendo Strings de narración de combate.
    golpeador = percents.quienPega(c1, c2)
    golpeado = c1 if golpeador == c2 else c2
    ataque = golpeador.get("ultimoAtaque") #
    categoriasGolpe = categorias["characters"][golpeador.get("Nombre")]["Move_Set"].get(ataque)
    intensidad = categorias["characters"][golpeador.get("Nombre")]["Move_Set"][ataque].get("Intensidad")

    descripcionAtaque = describirAtaque(categoriasGolpe, intensidad, comentarios)
    descripcionDaño = describirDaño( categoriasGolpe, intensidad, comentarios)

    #Me falta depurar y añadir más formas de estructurar las frases posibles(Ya continuaré...)

    print(f"{golpeador.get('Nombre')} {descripcionAtaque} {golpeado.get('Nombre')} {descripcionDaño}.")


if __name__ == "__main__":
    #Pruebas
    base = Path(__file__).resolve().parent
    rutaComentarios = base / ".." / "comments.json"
    rutaCategorias = base / ".." / "moveset_categories.json"
    with rutaCategorias.open("r",encoding="utf-8") as categories_json, rutaComentarios.open("r",encoding="utf-8") as comments_json :
        datosCategorias = json.load(categories_json)
        comentarios = json.load(comments_json)

    print(datosCategorias["Characters"]["mario"]["Move_Set"]["Especial_Neutral_Fireball"].get("Intensidad"))
    print(f"Mario {random.choice(comentarios["ataque"]["proyectil"]["baja"]).replace("{proyectil}", "bolas de fuego")}")