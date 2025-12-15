"""
Clases del modelo para Super Smash Bros Rand
"""
import random
from typing import Dict, List


class Move:
    """Representa un movimiento de un personaje"""

    def __init__(self, nombre: str, daño: float, tipo: str, intensidad: str):
        self.nombre = nombre
        self.daño = daño
        self.tipo = tipo  # fisico, proyectil, magico, grapling, reflector
        self.intensidad = intensidad  # baja, media, alta, aturde

    def __repr__(self):
        return f"Move({self.nombre}, {self.daño}, {self.tipo}, {self.intensidad})"


class Character:
    """Representa un personaje del juego con sus estadísticas y movimientos"""

    def __init__(self, nombre: str, ko_percent: int, movimientos: List[Move]):
        self.nombre = nombre
        self.ko_percent = ko_percent
        self.movimientos = movimientos
        self._movimientos_dict = {mov.nombre: mov for mov in movimientos}

    def obtener_movimiento(self, nombre_movimiento: str) -> Move:
        """Obtiene un movimiento específico por nombre"""
        return self._movimientos_dict.get(nombre_movimiento)

    def movimiento_aleatorio(self) -> Move:
        """Selecciona un movimiento aleatorio"""
        return random.choice(self.movimientos)

    def __repr__(self):
        return f"Character({self.nombre}, KO%={self.ko_percent}, movimientos={len(self.movimientos)})"


class Player:
    """Representa un jugador en el combate"""

    def __init__(self, personaje: Character, numero_jugador: int, nombreJugador : str ,vidas: int = 2):
        self.personaje = personaje
        self.numero_jugador = numero_jugador
        self.vidas = vidas
        self.porcentaje = 0
        self.ultimo_ataque: Move = None
        self.cc = 0
        self.nombreJugador = nombreJugador

    @property
    def nombre(self) -> str:
        """Retorna el nombre del personaje del jugador"""
        return self.personaje.nombre

    @property
    def ko_percent(self) -> int:
        """Retorna el porcentaje de KO del personaje"""
        return self.personaje.ko_percent

    def recibir_daño(self, daño: float):
        """Aplica daño al jugador"""
        self.porcentaje += daño

    def perder_vida(self):
        """Reduce una vida y resetea el porcentaje"""
        self.vidas -= 1
        self.porcentaje = 0

    def comboCounter(self, pega: bool):
        """
        Actualiza el contador de combo
        
        Args:
            pega: True si el jugador pegó en este turno, False si no
        """
        if pega:
            self.cc += 1
        else:
            self.cc = 0
            
    def esta_vivo(self) -> bool:
        """Verifica si el jugador aún tiene vidas"""
        return self.vidas > 0

    def atacar(self) -> Move:
        """Realiza un ataque aleatorio"""
        movimiento = self.personaje.movimiento_aleatorio()
        self.ultimo_ataque = movimiento
        return movimiento

    def calcular_probabilidad_ko(self) -> float:
        """
        Calcula la probabilidad de KO basada en el porcentaje actual

        Returns:
            float: Probabilidad de 0.0 a 1.0
        """
        if self.porcentaje < self.ko_percent:
            return 0.0

        # Calcula en qué rango de 4% está el porcentaje
        diferencia = self.porcentaje - self.ko_percent
        rango = diferencia // 4

        # Probabilidad base es 20% (0.20) y aumenta 2% por cada rango de 4%
        probabilidad = 0.20 + (rango * 0.02)

        # Máximo 100%
        return min(probabilidad, 1.0)

    def intentar_ko(self) -> bool:
        """
        Intenta hacer un KO basado en la probabilidad actual

        Returns:
            bool: True si el jugador es eliminado
        """
        probabilidad = self.calcular_probabilidad_ko()
        if probabilidad > 0:
            aleatorio = random.random()
            return aleatorio <= probabilidad
        return False

    def __repr__(self):
        return f"Player({self.nombre}, {self.porcentaje}%, {self.vidas} vidas)"
