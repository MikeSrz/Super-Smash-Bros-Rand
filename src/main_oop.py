import os
import time
import discord
from discord.ext import commands
import SBRsecrets
import asyncio
from models import Player
from data_loader import DataLoader
from game_logic import quien_pega, ejecutar_turno
from narration import Narrator
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents = intents)


async def limpiar_canal(ctx: commands.Context, limit: int = 100):
    await ctx.channel.purge(limit=limit)


def main():
    # Cargar datos
    data_loader = DataLoader()
    narrador = Narrator(data_loader.obtener_comentarios())

    #Comando Presentacion
    @bot.command()
    async def iniciar(ctx: commands.Context):
        # Permitir que cualquier usuario en el canal responda (j1 y j2 pueden ser diferentes)
        def check(message: discord.Message) -> bool:
            return message.channel == ctx.channel and not message.author.bot

        async def preguntarLuchador(data_loader: DataLoader, num: int) -> tuple:
            # Normalizar la lista de personajes a minúsculas para comparaciones
            personajes = [p.lower() for p in data_loader.listar_personajes()]
            insultos = ["gilipollas", "retrasado", "mongolo", "bujarrilla", "bujarron"]

            while True:
                await ctx.send(f"Escribe el nombre del jugador {num}:")
                c: discord.Message = await bot.wait_for("message", timeout=60.0, check=check)
                texto = c.content.strip().lower()
                if texto in personajes:
                    jugador = data_loader.crear_jugador(c.content.strip(), num, c.author.name)
                    return jugador, c.author
                await ctx.send(f"Escribe el nombre bien, {random.choice(insultos)}")
        # Empieza el programa: purgar canal y mostrar bienvenida
        await limpiar_canal(ctx)
        await ctx.send("=" * 80)
        await ctx.send("Bienvenido a Super Smash Bros Rand")
        await ctx.send("El simulador de peleas de la version Super Smash Bros Melee")
        await ctx.send("con sus personajes iniciales.")
        await ctx.send("=" * 80)
        
        # Mostrar personajes disponibles
        
        await ctx.send("Personajes jugables:")
        personajes = data_loader.listar_personajes()
        for i, p in enumerate(personajes, 1):
            await ctx.send(f"{i}. {p.capitalize()}")
        await ctx.send("=" * 80)
        try:
            j1, j1_usuario = await preguntarLuchador(data_loader, 1)
            j2, j2_usuario = await preguntarLuchador(data_loader, 2)
        except asyncio.TimeoutError:
            # Si el usuario no responde a tiempo, abortamos el comando
            await ctx.send("Tiempo agotado al esperar la respuesta. Repite el comando cuando estés listo.")
            return
        except Exception as e:
            # Cualquier otro error lo mostramos y salimos para evitar que
            # j1/j2 queden sin definir y provoquen UnboundLocalError.
            await ctx.send(f"Error al seleccionar jugadores: {e}")
            return
        
        # Cuenta regresiva
        await ctx.send("¡QUE EMPIECE EL COMBATE EN:")
        for i in range(3, 0, -1):
            await ctx.send(str(i))
            await asyncio.sleep(1.5)
        await limpiar_canal(ctx)
            
        # Bucle principal del combate
        while j1.esta_vivo() and j2.esta_vivo():
            
            atacante, defensor = quien_pega(j1, j2)
            # Ejecutar turno
            resultado = ejecutar_turno(atacante, defensor)
            # Mostrar estado actual
            await ctx.send(narrador.mostrar_estado(j1, j2))
            await ctx.send("=" * 80) 
            # Narrar el turno
            narracion = narrador.narrar_turno(resultado)
            await ctx.send(narracion)
            await asyncio.sleep(6)
            # Purgar mensajes intermedios para mantener el canal limpio
            await limpiar_canal(ctx)

        # Fin del combate
        await ctx.send("=" * 80)
        await ctx.send("¡FIN DEL COMBATE!")
        await ctx.send("=" * 80)

        # Determinar ganador
        if j1.esta_vivo():
            ganador = j1
            perdedor = j2
        else:
            ganador = j2
            perdedor = j1

        mencionGanador = j1_usuario.mention if ganador is j1 else j2_usuario.mention
        mencionPerdedor = j1_usuario.mention if perdedor is j1 else j2_usuario.mention
        await ctx.send(f"🏆 {mencionGanador} ¡{ganador.nombreJugador} ES EL GANADOR! 🏆")
        await ctx.send(f"{ganador.nombre.capitalize()} ha sobrevivido con {ganador.vidas} {'vida' if ganador.vidas == 1 else 'vidas'} restante{'s' if ganador.vidas != 1 else ''} a un {ganador.porcentaje:.1f}%")
        await ctx.send(f"{mencionPerdedor} JAJAJAJAJA chupala")
    
    @bot.event
    async def on_ready():
        print(f"Estoy dentro {bot.user}")
    bot.run(SBRsecrets.token)


if __name__ == "__main__":
    main()
