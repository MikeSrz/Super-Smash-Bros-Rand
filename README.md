# Super-Smash-Bros-Rand
Smash random Game
Un juego de smash basado en aleatoriedad, escalable

## Configuración del Bot de Discord

Para que el bot de Discord funcione, cada usuario necesita su propio token de Discord. Aquí te explico por qué y cómo configurarlo:

### 1. ¿Por qué un token propio?
Cada bot de Discord se registra como una aplicación única en Discord. El "token" es una clave secreta que Discord emite para esa aplicación específica. Este token es esencial por varias razones:
-   **Identificación y Autenticación:** El token permite que tu bot se autentique con la API de Discord, demostrando que es una aplicación legítima y autorizada para realizar acciones en nombre de tu bot (como enviar mensajes, leer canales, etc.).
-   **Seguridad:** Al usar un token único para cada instancia del bot (si se despliega por separado o si cada usuario lo ejecuta localmente), se aísla el acceso. Si un token se ve comprometido, solo afectará a esa instancia particular, no a todas. Es como una contraseña personal para tu bot.
-   **Permisos:** Los permisos del bot están asociados a su aplicación y, por lo tanto, a su token. Usar tu propio token asegura que tu bot tenga los permisos correctos para funcionar en tus servidores.

### 2. ¿Cómo debe ser el archivo `SBRsecrets.py`?
El archivo `SBRsecrets.py` es un módulo de Python simple que contiene tu token de Discord. Su estructura es la siguiente:

```python
token = "TU_TOKEN_AQUI"
```

Donde `TU_TOKEN_AQUI` debe ser reemplazado por el token real de tu bot de Discord. Este archivo **no debe ser compartido públicamente** y debe ser excluido de cualquier control de versiones (como `git`), por lo que es bueno que ya esté dentro de un archivo de "secrets".

### 3. ¿Dónde tienen que poner el token?
Debes crear o modificar el archivo llamado `SBRsecrets.py` y colocarlo en la siguiente ruta:

`Super-Smash-Bros-Rand/src/SBRsecrets.py`

Asegúrate de que el contenido del archivo sea exactamente `token = "TU_TOKEN_DE_DISCORD"`, reemplazando `TU_TOKEN_DE_DISCORD` con el valor real de tu token.

Con esto, el bot podrá leer tu token y conectarse a Discord correctamente.