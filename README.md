# AgendaFutbolTelegramBot

Puedes encontrarme en Telegram como @AgendaFutbolBot.

Un mini-proyecto que me ayuda a ahorrar tiempo al preguntarle a un bot por los partidos del día y no tener que ir a mi
página favorita a consultarlos directamente.

Además soporta filtrado por palabras y fechas, lo que lo hace más útil aún para búsquedas rápidas.

Está hecho como un bot para Telegram porque nunca había hecho uno antes y además porque paso la mayor parte del tiempo
ahí.

La documentación escrita hasta el momento corresponde a:

```
    /todo
        Entrega todos los eventos disponibles
    /hoy 
        Entrega los eventos del día (a la hora de Chile, timezone America/Santiago)
    /fecha <fecha>
        Entrega los eventos para la fecha dada, debe estar en formato YYYY-MM-DD
    /cuando <palabra>
        Entrega los eventos que contienen la palabra en el nombre del evento, canal o liga.
    /set_alias <tu equipo> <tu alias en una sola palabra>
        Agrega un alias para tu equipo favorito, para que puedas buscarlo más fácilmente.
    /version
        Entrega la versión del bot.
```

Si eres ñoño como yo, te encantará saber cuales son las tecnologías usadas:

- Python
- FastAPI
- GraphQL
- ORM (SQLAlchemy)
- SQLite

--- 
Cualquier cosa contactarme a david.escobar@ug.uchile.cl