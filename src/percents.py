import json
from pathlib import Path
import random
import comments

def preguntarLuchador(personajes, datos, num):
    base = Path(__file__).resolve().parent
    ruta = base / ".." / "characters.json"
    jugador = {
        "Vidas" : 3,
        "Porcentaje" : 0
    }
    with ruta.open("r",encoding="utf-8") as file:    
        while True:
            c = input(f"Escribe el nombre del jugador {num}: ").lower()
            if c in personajes:
                jugador["Nombre"] = c
                jugador.update(datos["Characters"][c])
                return jugador
            print("Escribe bien el nombre gilipollas, dale a enter y ponlo bien anda")
            input("") 

def porcentajeAleatorio():
    x = random.randint(0,100)
    return x

def quienTieneMasVida(p1,p2):
    return max(p1,p2)

def quienPega(c1,c2,cc=None):
    # Contador de combo
    x = random.randint(1,2)
    if x == 1:
        return c1
    if x == 2:
        return c2
def cuantoDañoHace(personaje):
    #Hay que cambiar esta funcion para que en el MAIN cree la lista moveSet y asi no tenga que abrir el archivo todas las veces
    # El parametro de porcentaje lo vamos a usar cuando metamos lo del rage    
    base = Path(__file__).resolve().parent
    ruta = base / ".." / "characters.json"
    with ruta.open("r",encoding="utf-8") as file:
        datos = json.load(file)
        moveSet = list(datos["Characters"][personaje]["Move_Set"].keys())
        movimiento = random.choice(moveSet)
        dañoDelMovimiento = datos["Characters"][personaje]["Move_Set"].get(movimiento)
    return dañoDelMovimiento
def seMuere(personaje):
    
    if porcentaje>=kp:
        match porcentaje:
            case x if 100 <= x <= 103:
                if porcentajeAleatorio() <= 20:
                    return True
                else:
                    return False

            case x if 104 <= x <= 107:
                if porcentajeAleatorio() <= 22:
                    return True
                else:
                    return False

            case x if 108 <= x <= 111:
                if porcentajeAleatorio() <= 24:
                    return True
                else:
                    return False

            case x if 112 <= x <= 115:
                if porcentajeAleatorio() <= 26:
                    return True
                else:
                    return False

            case x if 116 <= x <= 119:
                if porcentajeAleatorio() <= 28:
                    return True
                else:
                    return False

            case x if 120 <= x <= 123:
                if porcentajeAleatorio() <= 30:
                    return True
                else:
                    return False

            case x if 124 <= x <= 127:
                if porcentajeAleatorio() <= 32:
                    return True
                else:
                    return False

            case x if 128 <= x <= 131:
                if porcentajeAleatorio() <= 34:
                    return True
                else:
                    return False

            case x if 132 <= x <= 135:
                if porcentajeAleatorio() <= 36:
                    return True
                else:
                    return False

            case x if 136 <= x <= 139:
                if porcentajeAleatorio() <= 38:
                    return True
                else:
                    return False

            case x if 140 <= x <= 143:
                if porcentajeAleatorio() <= 40:
                    return True
                else:
                    return False

            case x if 144 <= x <= 147:
                if porcentajeAleatorio() <= 42:
                    return True
                else:
                    return False

            case x if 148 <= x <= 151:
                if porcentajeAleatorio() <= 44:
                    return True
                else:
                    return False

            case x if 152 <= x <= 155:
                if porcentajeAleatorio() <= 46:
                    return True
                else:
                    return False

            case x if 156 <= x <= 159:
                if porcentajeAleatorio() <= 48:
                    return True
                else:
                    return False

            case x if 160 <= x <= 163:
                if porcentajeAleatorio() <= 50:
                    return True
                else:
                    return False

            case x if 164 <= x <= 167:
                if porcentajeAleatorio() <= 52:
                    return True
                else:
                    return False

            case x if 168 <= x <= 171:
                if porcentajeAleatorio() <= 54:
                    return True
                else:
                    return False

            case x if 172 <= x <= 175:
                if porcentajeAleatorio() <= 56:
                    return True
                else:
                    return False

            case x if 176 <= x <= 179:
                if porcentajeAleatorio() <= 58:
                    return True
                else:
                    return False

            case x if 180 <= x <= 183:
                if porcentajeAleatorio() <= 60:
                    return True
                else:
                    return False

            case x if 184 <= x <= 187:
                if porcentajeAleatorio() <= 62:
                    return True
                else:
                    return False

            case x if 188 <= x <= 191:
                if porcentajeAleatorio() <= 64:
                    return True
                else:
                    return False

            case x if 192 <= x <= 195:
                if porcentajeAleatorio() <= 66:
                    return True
                else:
                    return False

            case x if 196 <= x <= 199:
                if porcentajeAleatorio() <= 68:
                    return True
                else:
                    return False

            case x if 200 <= x <= 203:
                if porcentajeAleatorio() <= 70:
                    return True
                else:
                    return False

            case x if 204 <= x <= 207:
                if porcentajeAleatorio() <= 72:
                    return True
                else:
                    return False

            case x if 208 <= x <= 211:
                if porcentajeAleatorio() <= 74:
                    return True
                else:
                    return False

            case x if 212 <= x <= 215:
                if porcentajeAleatorio() <= 76:
                    return True
                else:
                    return False

            case x if 216 <= x <= 219:
                if porcentajeAleatorio() <= 78:
                    return True
                else:
                    return False

            case x if 220 <= x <= 223:
                if porcentajeAleatorio() <= 80:
                    return True
                else:
                    return False

            case x if 224 <= x <= 227:
                if porcentajeAleatorio() <= 82:
                    return True
                else:
                    return False

            case x if 228 <= x <= 231:
                if porcentajeAleatorio() <= 84:
                    return True
                else:
                    return False

            case x if 232 <= x <= 235:
                if porcentajeAleatorio() <= 86:
                    return True
                else:
                    return False

            case x if 236 <= x <= 239:
                if porcentajeAleatorio() <= 88:
                    return True
                else:
                    return False

            case x if 240 <= x <= 243:
                if porcentajeAleatorio() <= 90:
                    return True
                else:
                    return False

            case x if 244 <= x <= 247:
                if porcentajeAleatorio() <= 92:
                    return True
                else:
                    return False

            case x if 248 <= x <= 251:
                if porcentajeAleatorio() <= 94:
                    return True
                else:
                    return False

            case x if 252 <= x <= 255:
                if porcentajeAleatorio() <= 96:
                    return True
                else:
                    return False

            case x if 256 <= x <= 259:
                if porcentajeAleatorio() <= 98:
                    return True
                else:
                    return False

            case x if 260 <= x <= 263:
                if porcentajeAleatorio() <= 100:
                    return True
                else:
                    return False

if __name__ == "__main__":
    print(cuantoDañoHace("sheik"))
    print("Ejecucion completada")
        