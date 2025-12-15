import discord
from discord.ext import commands
import random
from models import Player
from data_loader import DataLoader

def quien_pega(p1: Player, p2: Player) -> tuple[Player, Player]:
    """
    Determina aleatoriamente quién ataca y quién defiende

    Args:
        p1: Jugador 1
        p2: Jugador 2

    Returns:
        tuple: (atacante, defensor)
    """
    
    if random.randint(1, 2) == 1:
        return p1, p2
    else:
        return p2, p1


def ejecutar_turno(atacante: Player, defensor: Player) -> dict:
    """
    Ejecuta un turno de combate

    Args:
        atacante: Jugador que ataca
        defensor: Jugador que defiende

    Returns:
        dict: Información del turno (movimiento, daño, ko)
    """
    
    # Incrementar combo del atacante y resetear el del defensor
    atacante.comboCounter(True)
    defensor.comboCounter(False)
    
    # El atacante realiza un ataque
    movimiento = atacante.atacar()

    # El defensor recibe el daño
    defensor.recibir_daño(movimiento.daño)

    # Verificar si hay KO
    ko = False
    if defensor.intentar_ko() or atacante.cc == 3:
        defensor.perder_vida()
        ko = True

    return {
        "atacante": atacante,
        "defensor": defensor,
        "movimiento": movimiento,
        "daño": movimiento.daño,
        "ko": ko,
        "porcentaje_final": defensor.porcentaje
    }
