
import json
from pathlib import Path
from typing import Dict, List
from models import Character, Move, Player


class DataLoader:
    """Carga y gestiona los datos del juego"""

    def __init__(self):
        self.base = Path(__file__).resolve().parent
        self.personajes: Dict[str, Character] = {}
        self.comentarios: dict = {}
        self._cargar_datos()

    def _cargar_datos(self):
        """Carga todos los datos JSON necesarios"""
        # Rutas de los archivos
        ruta_personajes = self.base / ".." / "characters.json"
        ruta_categorias = self.base / ".." / "moveset_categories.json"
        ruta_comentarios = self.base / ".." / "comments.json"

        # Cargar JSONs
        with ruta_personajes.open("r", encoding="utf-8") as f:
            datos_personajes = json.load(f)

        with ruta_categorias.open("r", encoding="utf-8") as f:
            datos_categorias = json.load(f)

        with ruta_comentarios.open("r", encoding="utf-8") as f:
            self.comentarios = json.load(f)

        # Convertir datos a objetos Character
        for nombre, datos in datos_personajes["Characters"].items():
            movimientos = []
            categorias_personaje = datos_categorias["Characters"][nombre]["Move_Set"]

            for nombre_mov, daño in datos["Move_Set"].items():
                # Obtener tipo e intensidad de moveset_categories.json
                categoria = categorias_personaje[nombre_mov]
                tipo = categoria.get("Tipo", "fisico")
                intensidad = categoria.get("Intensidad", "media")

                movimiento = Move(nombre_mov, daño, tipo, intensidad)
                movimientos.append(movimiento)

            personaje = Character(nombre, datos["KO_percent"], movimientos)
            self.personajes[nombre] = personaje

    def obtener_personaje(self, nombre: str) -> Character:
        """Obtiene un personaje por nombre"""
        return self.personajes.get(nombre.lower())

    def listar_personajes(self) -> List[str]:
        """Retorna una lista con los nombres de todos los personajes"""
        return list(self.personajes.keys())

    def crear_jugador(self, nombre_personaje: str, numero_jugador: int, nombre_del_jugador: str) -> Player:
        """Crea un jugador con el personaje especificado"""
        personaje = self.obtener_personaje(nombre_personaje)
        if personaje is None:
            raise ValueError(f"Personaje '{nombre_personaje}' no encontrado")
        return Player(personaje, numero_jugador, nombre_del_jugador)

    def obtener_comentarios(self) -> dict:
        """Retorna los comentarios cargados"""
        return self.comentarios
