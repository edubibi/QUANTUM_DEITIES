import random
import json
import os
import requests
import base64
import time
from datetime import datetime

# --- CONFIGURACIÓN DE APIS (Opcional - Requiere Claves) ---
# Intentamos cargar la clave de un archivo local si existe
def load_env_key():
    try:
        if os.path.exists(".env"):
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith("OPENAI_API_KEY="):
                        return line.split("=")[1].strip().strip('"')
    except:
        pass
    return os.getenv("OPENAI_API_KEY", "")

OPENAI_API_KEY = load_env_key()
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY", "")

ATOMIC_TRAITS = {
    "Entity_Faces": [
        "Synthetic Sovereign", "Cybernetic Guardian", "Quantum Muse", "Silicon Sentinel", 
        "Celestial Construct", "Neural Empress", "Holographic Arbiter", "Post-human Entity",
        "Synthetic Sovereign", "Data-stream Node", "Glitch Titan", "Techno-Core",
        "Bio-mechanical Prime", "Titanium Valkyrie", "Void-Walker Unit", "Omniscient Neural Hub"
    ],
    "Entity_Abstract": [
        "Quantum singularity", "Neural entropy swarm", "Fractal energy core", "Data-stream vortex",
        "Liquid light explosion", "Cosmic binary nebula", "Geometric transcendence", "Plasma silk sculpture",
        "Ethereal data ghost", "Techno-organic constellation", "Supernova glitch", "Holographic supernova"
    ],
    "Facial_Base": [
        "sculpted porcelain face", "translucent bio-engineered skin", "shifting liquid mercury visage",
        "matte obsidian composite features", "iridescent synth-flesh", "matte white carbon fiber",
        "humanoid face of brushed titanium", "perfectly symmetrical synthetic skin", "veined marble cyber-face",
        "molten glass skin with internal glow", "pearl-textured neural composite", "black-hole obsidian features"
    ],
    "Circuitry_Integration": [
        "subsurface golden circuitry pulsing with warm light", "glowing neon neural pathways",
        "intricate fiber-optic capillaries", "micro-laser etched fractal patterns",
        "embedded crystalline processors along the jawline", "liquid light conduits flowing like tears",
        "ultraviolet data-sigils glowing beneath the surface", "active nanite swarms forming temporary scars",
        "hexagonal nanite plating pulsing at 60Hz", "superconducting emerald ley-lines"
    ],
    "Materials_Abstract": [
        "iridescent bismuth crystals", "molten rainbow chrome", "frozen dark matter shards",
        "translucent jelly-like cosmic plasma", "layered sheets of digital silk", "interlocking geometric prisms",
        "swirling vapor of electrified mercury", "shattered diamond aerosols", "glowing neon thread lattices"
    ],
    "Ocular_Augmentation": [
        "multi-faceted diamond ocular lenses", "glowing sapphire optic sensors",
        "void-black sensory implants with rotating rings", "burning amber laser-array eyes",
        "liquid nitrogen cooled ocular chambers", "holographic iris projecting status codes",
        "mechanical pupils contracting with clockwork precision", "eyeless facial structure with sensor-nodes",
        "star-chart projection lenses", "vortex-iris reflecting distant galaxies"
    ],
    "Energy_FX": [
        "vortex of swirling quantum energy particles", "ethereal wisps of plasma energy",
        "cascading binary code rain", "halos of rotating geometric light",
        "molecular dust particles suspended in a temporal field", "aurora-like data streams",
        "pulsing ion-fields creating a corona effect", "shimmering heat-distortion from over-clocked cores",
        "electromagnetic lightning arcs", "floating glyphs of ancient neural code",
        "high-voltage plasma arcs", "nebulous ionized clouds", "pulsing electrical storms", "interstellar nebula wisps"
    ],
    "Style_Artist": [
        "H.R. Giger organic-tech bio-mechanical", 
        "Moebius surreal sci-fi line-art",
        "Syd Mead industrial futurism aesthetic",
        "Beeple digital chaos and complexity",
        "Zdzisław Beksiński dystopian nightmare",
        "Peter Mohrbacher celestial entity horror",
        "Alberto Seveso high-speed liquid dynamic",
        "Android Jones psychedelic digital visionary",
        "James Thompson cyber-renaissance detail"
    ],
    "Lighting_Atmosphere": [
        "volumetric fog with 8k neon flares", "dense digital haze with light-streaks",
        "crystalline snow falling upwards, zero-g", "chromatic aberration, event horizon",
        "subtle glitch-art distortions", "bokeh of data-shards and hexagons",
        "dramatically backlit by a dying blue giant", "cinematic rain reflecting emerald neon",
        "biological luminescence from internal structures", "quantum entanglement lighting spooky action",
        "nebular cosmic glow background", "electric storm backlighting", "strobe lighting from ion discharges",
        "dramatic chiaroscuro neon highlights", "ethereal plasma source rim-lighting"
    ],
    "Camera_Tech": [
        "extreme macro photography, f/1.8", "telephoto lens portrait, shallow depth",
        "low angle heroic shot, cinematic lighting", "symmetrical composition, rule of thirds",
        "wide angle cinematic sci-fi epic still", "highly detailed textured 3D render", 
        "8k resolution, photorealistic Unreal Engine 5.4", "sharp focus on microscopic mechanical ports",
        "Octane Render, ray-tracing, global illumination",
        "unmatched hyper-realism, photorealistic perfection"
    ],
    "Color_Theory": [
        "cyberpunk cyan and electric magenta", "toxic green and deep ultraviolet",
        "regal gold and matte black", "iridescent opal and midnight blue",
        "crimson pulse and metallic chrome", "blood orange and cold steel gray",
        "monochromatic silver and neon white", "retro-vaporwave pastel gradients",
        "electric blue and violet nebula", "plasma white and ionized cyan",
        "anodized copper and electric cobalt"
    ]
}

def generate_quantum_prompt(mode="FACES"):
    """Genera un prompt de Máxima Calidad (v6.0 - Leonardo Edition)."""
    style = random.choice(ATOMIC_TRAITS["Style_Artist"])
    mood = random.choice(ATOMIC_TRAITS["Lighting_Atmosphere"])
    camera = random.choice(ATOMIC_TRAITS["Camera_Tech"])
    colors = random.choice(ATOMIC_TRAITS["Color_Theory"])
    energy = random.choice(ATOMIC_TRAITS["Energy_FX"])
    
    if mode == "FACES":
        entity = random.choice(ATOMIC_TRAITS["Entity_Faces"])
        base = random.choice(ATOMIC_TRAITS["Facial_Base"])
        circuits = random.choice(ATOMIC_TRAITS["Circuitry_Integration"])
        eyes = random.choice(ATOMIC_TRAITS["Ocular_Augmentation"])
        
        templates = [
            f"Masterpiece portrait of {entity}, {base}, {circuits}, {eyes}. Adorned with {energy}. Atmosphere: {mood}. Color palette: {colors}. Art style inspired by {style}. Technical specs: {camera}, intricate textures, 8k resolution.",
            f"Cinematic close-up of {entity} featuring {base} and {eyes}. {circuits} details glowing through. {energy} surrounding the head. {mood} vibe. {colors} scheme. {style} style. {camera}.",
            f"Symmetrical cybernetic deity portrait: {entity} with {base}. Integrated {circuits}. {eyes} optics. Enveloped in {energy}. {mood} environment. {colors} and {style} influence. {camera}."
        ]
        prompt = random.choice(templates)
    else: # Mode ABSTRACT
        entity = random.choice(ATOMIC_TRAITS["Entity_Abstract"])
        material = random.choice(ATOMIC_TRAITS["Materials_Abstract"])
        
        templates = [
            f"Conceptual abstract art: {entity} constructed from {material}. Explosion of {energy}. Lighting: {mood}. Palette: {colors}. Style: {style}, complex geometry. {camera}.",
            f"Non-representational masterpiece: {material} forming a {entity}. Chaotic {energy} flow. {mood} lighting. {colors} colors. Inspired by {style}. {camera}.",
            f"Geometric transcendence of {entity} with {material} textures. Reactive {energy} fields. {mood} atmosphere. Vibrant {colors}. {style} aesthetics. {camera}."
        ]
        prompt = random.choice(templates)
    return prompt

def api_generate_image(prompt, filename, provider="OPENAI"):
    output_path = os.path.join("VORTEX_1_0", "images")
    if not os.path.exists(output_path): os.makedirs(output_path)
    full_path = os.path.join(output_path, f"{filename}.png")
    
    if provider == "OPENAI" and OPENAI_API_KEY:
        try:
            url = "https://api.openai.com/v1/images/generations"
            headers = {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"}
            data = {"model": "dall-e-3", "prompt": prompt, "n": 1, "size": "1024x1024"}
            
            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
            
            if 'data' in response_json:
                img_url = response_json['data'][0]['url']
                img_data = requests.get(img_url).content
                with open(full_path, 'wb') as f: f.write(img_data)
                return full_path
            else:
                print(f"Error Detallado OpenAI: {response_json}")
        except Exception as e: print(f"Error OpenAI: {e}")
    return None

def main(count=10, mode="BOTH", run_api=False):
    output_dir = "VORTEX_2_0"
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    print(f"--- VORTEX 1.0 ENGINE ---")
    prompts_data = []
    for i in range(1, count + 1):
        actual_mode = mode if mode != "BOTH" else ("FACES" if i % 2 == 0 else "ABSTRACT")
        p = generate_quantum_prompt(actual_mode)
        filename = f"quantum_{actual_mode.lower()}_{i}_{datetime.now().strftime('%H%M%S')}"
        entry = {"id": i, "mode": actual_mode, "prompt": p}
        if run_api:
            img_path = api_generate_image(p, filename)
            if img_path: 
                entry["image"] = img_path
                print(f"[{i}/{count}] Imagen generada: {filename}")
            time.sleep(2) # Pequeña pausa para estabilidad
        prompts_data.append(entry)
    with open(os.path.join(output_dir, "quantum_v5_batch.json"), "w", encoding='utf-8') as f:
        json.dump(prompts_data, f, indent=4, ensure_ascii=False)
    print(f"¡Éxito! {count} items procesados.")

if __name__ == "__main__":
    # GRAN LOTE VORTEX 1.0: Generando 100 imágenes originales
    main(100, mode="BOTH", run_api=True)
