# Agent-Mode

Repositorio de ejemplo para trabajar de manera dinámica con ChatGPT Agent Mode.

## Configuración

1. Crear un entorno virtual (opcional):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

El script `agent_example.py` muestra cómo interactuar con la API de OpenAI.
Configura la variable de entorno `OPENAI_API_KEY` con tu clave y ejecuta:

```bash
python agent_example.py "Hola"
```

Esto enviará el mensaje a la API y mostrará la respuesta.

