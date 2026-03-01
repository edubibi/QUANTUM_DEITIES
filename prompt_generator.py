import random
import json
import os

# --- CONFGURACIÓN ATÓMICA DE TRAITS (V4.0 - PROMPT ENGINE) ---
# Se divide en micro-componentes para generar prompts ultra-detallados

ATOMIC_TRAITS = {
    "Entity_Type": [
        "Android Archangel", "Cybernetic Seraphim", "Quantum Muse", "Silicon Deity", 
        "Celestial Android", "Neural Empress", "Holographic Monk", "Post-human Messiah",
        "Synthetic Goddess", "Data-stream Cherub", "Glitch Titan", "Techno-Oracle"
    ],
    "Facial_Base": [
        "sculpted porcelain face", "translucent bio-engineered skin", "shifting liquid mercury visage",
        "matte obsidian composite features", "iridescent synth-flesh", "matte white carbon fiber",
        "humanoid face of brushed titanium", "perfectly symmetrical synthetic skin", "veined marble cyber-face"
    ],
    "Circuitry_Integration": [
        "subsurface golden circuitry pulsing with warm light", "glowing neon neural pathways",
        "intricate fiber-optic capillaries", "micro-laser etched fractal patterns",
        "embedded crystalline processors along the jawline", "liquid light conduits flowing like tears",
        "ultraviolet data-sigils glowing beneath the surface", "active nanite swarms forming temporary scars"
    ],
    "Ocular_Augmentation": [
        "multi-faceted diamond ocular lenses", "glowing sapphire optic sensors",
        "void-black sensory implants with rotating rings", "burning amber laser-array eyes",
        "liquid nitrogen cooled ocular chambers", "holographic iris projecting status codes",
        "mechanical pupils contracting with clockwork precision", "eyeless facial structure with sensor-nodes"
    ],
    "Energy_Manifestation": [
        "vortex of swirling quantum energy particles", "ethereal wisps of plasma energy",
        "cascading binary code rain in the atmosphere", "halos of rotating geometric light",
        "molecular dust particles suspended in a temporal field", "aurora-like data streams",
        "pulsing ion-fields creating a corona effect", "shimmering heat-distortion from over-clocked cores"
    ],
    "Floating_Relics": [
        "orbiting shards of obsidian and gold", "levitating tech-crown made of floating antennas",
        "shattered gemstone debris in a zero-g field", "rotating rings of pure ultraviolet light",
        "floating data-scrolls and holographic glyphs", "suspended micro-probes following the head",
        "deconstructed mechanical wings made of light-layers", "hovering neural-link connectors"
    ],
    "Atmospheric_Mood": [
        "volumetric fog illuminated by neon flares", "dense digital haze with light-streaks",
        "crystalline snow falling upwards", "chromatic aberration at the edges of reality",
        "subtle glitch-art distortions in the air", "bokeh of data-shards and hexagons",
        "dramatically backlit by a dying star", "cinematic rain reflecting neon signs"
    ],
    "Cinematography": [
        "extreme close-up macro photography", "telephoto lens portrait with shallow depth of field",
        "low angle heroic shot", "symmetrical composition", "wide angle cinematic still",
        "highly detailed textured render", "8k resolution, photorealistic Unreal Engine 5 style",
        "masterpiece by Moebius and HR Giger", "sharp focus on microscopic mechanical ports"
    ],
    "Color_Theory": [
        "cyberpunk cyan and electric magenta", "toxic green and deep ultraviolet",
        "regal gold and matte black", "iridescent opal and midnight blue",
        "crimson pulse and metallic chrome", "blood orange and cold steel gray"
    ]
}

def build_atomic_prompt():
    """Ensambla un prompt granular seleccionando micro-traits."""
    entity = random.choice(ATOMIC_TRAITS["Entity_Type"])
    base = random.choice(ATOMIC_TRAITS["Facial_Base"])
    circuits = random.choice(ATOMIC_TRAITS["Circuitry_Integration"])
    eyes = random.choice(ATOMIC_TRAITS["Ocular_Augmentation"])
    energy = random.choice(ATOMIC_TRAITS["Energy_Manifestation"])
    relics = random.choice(ATOMIC_TRAITS["Floating_Relics"])
    mood = random.choice(ATOMIC_TRAITS["Atmospheric_Mood"])
    camera = random.choice(ATOMIC_TRAITS["Cinematography"])
    colors = random.choice(ATOMIC_TRAITS["Color_Theory"])
    
    # Estructura del Prompt: Sujeto Central -> Detalles -> Ambiente -> Estilo
    prompt = (
        f"Portrait of a {entity} with a {base}, "
        f"{circuits}, {eyes}, "
        f"surrounded by {energy} and {relics}. "
        f"Lighting: {mood}, palette of {colors}. "
        f"Technical style: {camera}, intricate details, hyper-realistic, high fidelity."
    )
    return prompt

def main(count=100):
    output_dir = "PROMPTS_QUANTUM"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    print(f"--- GENERADOR 'ATÓMICO' DE PROMPTS QUANTUM DEITIES V4.0 ---")
    print(f"Generando {count} prompts complejos...\n")
    
    prompts_data = []
    for i in range(1, count + 1):
        p = build_atomic_prompt()
        prompts_data.append({"id": i, "prompt": p})
        if i <= 5: # Mostrar solo los 5 primeros en consola
            print(f"ATOMIC PROMPT #{i}:")
            print(f"{p}\n")
            
    # Guardar en JSON (Versión masiva para Tedd/Manolo)
    with open(os.path.join(output_dir, "atomic_prompts_batch.json"), "w", encoding='utf-8') as f:
        json.dump(prompts_data, f, indent=4, ensure_ascii=False)
        
    # Actualizar el Visor HTML para incluir estos nuevos prompts
    update_viewer(prompts_data[:20]) # Pasamos los primeros 20 para el visor rápido
    
    print(f"Resultados guardados en {output_dir}/atomic_prompts_batch.json")

def update_viewer(prompts):
    """Actualiza o regenera el visor HTML con los nuevos prompts atómicos."""
    # (El código del visor se puede inyectar aquí o crear un script separado)
    # Por simplicidad, aviso que el JSON ya está listo.
    pass

if __name__ == "__main__":
    main(50) # Generamos 50 para empezar fuerte
