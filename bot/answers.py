# /start
HOW_TO_USAGE = """
    Bienvenido! Este bot responde a la pregunta quién juega hoy?
    
    Los comandos con que me puedes llamar son:
    
    /todo
        Entrega todos los eventos disponibles
    /hoy 
        Entrega los eventos del día (a la hora de Chile)
    /fecha <fecha>
        Entrega los eventos para la fecha dada, debe estar en formato YYYY-MM-DD
    /cuando <palabra>
        Entrega los eventos que contienen la palabra en el nombre del evento, canal o liga.
    /set_alias <tu equipo> <tu alias en una sola palabra>
        Agrega un alias para tu equipo favorito, para que puedas buscarlo más fácilmente.
    /version
        Entrega la versión del bot.
    
    Si eres ñoño como yo, te encantará saber cuales son las tecnologías usadas:
    - Python
    - FastAPI
    - GraphQL
    """

# /fecha
DATE_WITHOUT_ARGS = """
    Debes enviar /fecha <fecha> en formato YYYY-MM-DD
"""

DATE_WITH_NO_COINCIDENCES = """
    No hay eventos agendados aún para {} unu. Prueba con otra fecha
"""

# /cuando
WHEN_WITHOUT_ARGS = """
    Debes enviar /cuando <una palabra>
"""

WHEN_WITH_NO_COINCIDENCES = """
    No se encontraron eventos que contengan {} unu.
    Prueba escribiéndolo de otra forma.
"""

# /todo
ALL_WITH_NO_COINCIDENCES = """
    No hay eventos disponibles, prueba más tarde {}.
"""

# /version

VERSION = """
    0.3.0
"""

# /set_alias

ALIAS_ADDED_SUCCESSFULLY = """
    Alias agregado correctamente!
"""

ALIAS_WITHOUT_ARGS = """
    Debes enviar /set_alias <tu equipo> <tu alias en una sola palabra>
"""