# Guía: Cómo obtener tu Clave API

Para que el generador haga fotos reales, necesitamos una "llave" (clave API) de los servicios de inteligencia artificial. La más recomendada es la de **OpenAI** (DALL-E 3).

### Pasos para conseguirla:

1. **Crear cuenta:** Ve a [platform.openai.com](https://platform.openai.com/) y regístrate.
2. **Añadir saldo:** Ve a la sección **Settings > Billing** y añade un poco de saldo (puedes empezar con $5 o $10). Cada imagen de alta calidad cuesta unos 0.04 - 0.08 centavos de dólar.
3. **Generar Clave:** Ve a **API Keys > Create new secret key**.
4. **Copia la clave:** Guárdala bien, solo se muestra una vez.

### Cómo poner la clave en tu App:

He preparado dos formas para que tú elijas:

- **Opción A (Fácil):** Pásame la clave por aquí y yo la pondré por ti en el archivo de configuración.
- **Opción B (Manual):** Abre el archivo `prompt_generator.py` y pon la clave en la línea 11:
  `OPENAI_API_KEY = "tu-clave-aqui"`

### ¿Cómo se guardan las fotos?

- **Desde la Web:** He añadido un botón **"DESCARGAR FOTO"** en el panel para que guardes las que más te gusten.
- **Automático:** Si usas el script de Python para generar 1,000 de golpe, las fotos se guardarán solas en la carpeta:
  `C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\output\images\`
