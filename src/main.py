import json
import os
from pathlib import Path
import time
import comments
import percents

def main():
    base = Path(__file__).resolve().parent
    ruta = base / ".." / "characters.json"
    os.system("cls")
    print("Bienvenido a Super Smash Bros Rand, el simulador de peleas de la version Super Smash Bros Melee con sus personajes inciales.")
    print("Personajes jugables:")
    with ruta.open("r",encoding="utf-8") as file:
        datos = json.load(file)
    personajes = list(datos["Characters"].keys())
    counter = 1
    for p in personajes:
        print(f"{counter}.{p.capitalize()}")
        counter+=1
    j1 = percents.preguntarLuchador(personajes,datos,1)
    j2 = percents.preguntarLuchador(personajes,datos,2)
        
    agilizador = 0 #Mi idea es que las primeras 4 interacciones haya algunas funciones como la de "seMuere" que no compruebe ya que es una perdida de eficiencia
    print("QUE EMPIECE EL COMBATE EN:")
    print("3")
    time.sleep(1.5)
    print("2")
    time.sleep(1.5)
    print("1")
    time.sleep(1.5)
    os.system("cls")
    print(j1)
    # while True:
    #     # print(comments.comentarios())
    #     print(f"{c1} {porcentajeDeC1}% | {vidasDeC1} restantes |")
    #     print(f"{c2} {porcentajeDeC2}% | {vidasDeC2} restantes |")
    #     if agilizador <=4:
    #         agilizador+=1

                
    
        
if __name__ == "__main__":
    main()