import random
import json
import os

# CONFIGURACIÓN DE TRAITS PARA PROMPTS
CATEGORIES = {
    "Subject": [
        "Futuristic cyberpunk portrait of a humanoid deity",
        "Ancient cosmic android with divine human features",
        "Cybernetic goddess with a face of liquid chrome and light",
        "Higher dimensional quantum entity in a human-like silhouette",
        "Mechanical angel of the silicon age, ethereal beauty",
        "Neon-lit cyber-monk with glowing ocular implants and regal posture"
    ],
    "Face_Patterns": [
        "glowing neon circuit patterns etched into porcelain skin",
        "fractal geometry light displays dancing on a humanoid face",
        "intricate fiber-optic veins pulsing with quantum energy",
        "subsurface geometric tattoos made of pure ultraviolet light",
        "flowing data streams moving across the cheeks and forehead",
        "crystalline micro-circuits embedded in a perfect facial structure"
    ],
    "Floating_Elements": [
        "holographic fragments and data-shards floating around head",
        "orbiting rings of pure white light and binary code",
        "shattered gemstone particles suspended in a zero-g halo",
        "ethereal energy wisps weaving through sleek cyber-hair",
        "levitating tech-relics and glowing glyphs in a circular configuration",
        "pulsing neural-link connectors hovering like a tech-crown"
    ],
    "Color_Palette": [
        "electric cyan and hot magenta",
        "deep ultraviolet and acid green",
        "molten amber and obsidian black",
        "iridescent pearl and sapphire blue",
        "crimson fire and metallic gold",
        "neon violet and toxic orange"
    ],
    "Effects": [
        "subtle glitch effects and chromatic aberration",
        "swirling digital particles and dust",
        "volumetric lighting and heavy atmosphere",
        "vibrant neon glow reflecting off metallic skin",
        "sharp focus on mechanical eye details",
        "distorted reality fragments and scanlines"
    ],
    "Background": [
        "dark absolute space with distant nebulae",
        "infinite digital void with a wireframe floor",
        "cyberpunk street blurred in the distance",
        "sacred geometric temple made of glass and light",
        "vortex of swirling quantum energy",
        "stellar nursery with exploding stars"
    ],
    "Style": [
        "highly detailed digital art style",
        "8k resolution, cinematic lighting",
        "hyper-realistic Unreal Engine 5 render",
        "surreal masterpiece, intricate texture",
        "concept art by Moebius and HR Giger",
        "sharp focus, macro photography style"
    ]
}

def generate_prompt():
    """Genera un prompt aleatorio combinando las categorías."""
    subject = random.choice(CATEGORIES["Subject"])
    patterns = random.choice(CATEGORIES["Face_Patterns"])
    elements = random.choice(CATEGORIES["Floating_Elements"])
    colors = random.choice(CATEGORIES["Color_Palette"])
    effects = random.choice(CATEGORIES["Effects"])
    bg = random.choice(CATEGORIES["Background"])
    style = random.choice(CATEGORIES["Style"])
    
    prompt = f"{subject}: {patterns}, {elements}, color palette of {colors}, {effects}, {bg}, {style}"
    return prompt

def main(count=10):
    output_dir = "PROMPTS_QUANTUM"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"--- GENERADOR DE PROMPTS QUANTUM DEITIES ---")
    print(f"Generando {count} prompts de ejemplo...\n")
    
    prompts = []
    for i in range(1, count + 1):
        p = generate_prompt()
        prompts.append({"id": i, "prompt": p})
        print(f"PROMPT #{i}:")
        print(f"{p}\n")
        
    # Guardar en JSON
    with open(os.path.join(output_dir, "prompts_batch.json"), "w", encoding='utf-8') as f:
        json.dump(prompts, f, indent=4, ensure_ascii=False)
        
    print(f"Resultados guardados en {output_dir}/prompts_batch.json")

if __name__ == "__main__":
    main(10)
