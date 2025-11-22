import main
import json
import os
from pathlib import Path
import random
import comments
import percents

def comentarios(c1,c2):
    golpeador = percents.quienPega(c1,c2)
    golpeado = c1 if golpeador == c2 else c2
    # ESTRUCTURA DE COME NTARIO
    # c2 = golpeado c1 = golpeador
    # Plantilla 1. [[ "c1["nombre"]+ c1["movimiento"] + mensaje generico +  c2["nombre"] + comportamiento_daño,+ c2["daño"]"] ,
    #     "Luigi" "ha realizado un green missil" + ha alcanzado a + "Kirby" +   "Sale volando por los aires." + "70 %"
    #      Plantilla 2. [[c1["movimiento"] + c2["nombre"] + mensaje genérico + c2["nombre"] +  comportamiento_daño + c2["daño"],
    #       "Bola de fuego de " +  "Mario" + "Ha impactado a" + "Kirby" + ", se retuerce de dolor" + "70%"
    #      Plantilla 3. [[c2["nombre"]
    base = Path(__file__).resolve().parent
    ruta = base / ".." / "comments.json"
    with ruta.open("r",encoding="utf-8") as file:
        comments = json.load(file)


if __name__ == "__main__":