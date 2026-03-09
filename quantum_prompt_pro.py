import random
import json
import os
from datetime import datetime

ATOMIC_TRAITS = {
    "Entity_Faces": [
        "Synthetic Sovereign", "Cybernetic Guardian", "Quantum Muse", "Silicon Sentinel", 
        "Celestial Construct", "Neural Empress", "Holographic Arbiter", "Post-human Entity",
        "Data-stream Node", "Glitch Titan", "Techno-Core", "Bio-mechanical Prime", 
        "Titanium Valkyrie", "Void-Walker Unit", "Omniscient Neural Hub"
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
        "volumetric fog, 8k neon flares", "dense digital haze, light-streaks",
        "crystalline snow falling upwards, zero-g", "chromatic aberration, event horizon",
        "subtle glitch-art distortions", "bokeh of data-shards and hexagons",
        "dramatically backlit by a dying blue giant", "cinematic rain reflecting emerald neon",
        "biological luminescence", "quantum entanglement lighting, spooky action at a distance",
        "nebular cosmic glow", "electric storm backlighting", "strobe lighting, ion discharges",
        "dramatic chiaroscuro neon highlights", "ethereal plasma rim-lighting"
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

def generate_midjourney_prompt(mode="FACES"):
    entity = random.choice(ATOMIC_TRAITS["Entity_Faces" if mode == "FACES" else "Entity_Abstract"])
    style = random.choice(ATOMIC_TRAITS["Style_Artist"])
    colors = random.choice(ATOMIC_TRAITS["Color_Theory"])
    energy = random.choice(ATOMIC_TRAITS["Energy_FX"])
    lighting = random.choice(ATOMIC_TRAITS["Lighting_Atmosphere"])
    
    if mode == "FACES":
        base = random.choice(ATOMIC_TRAITS["Facial_Base"])
        circuits = random.choice(ATOMIC_TRAITS["Circuitry_Integration"])
        eyes = random.choice(ATOMIC_TRAITS["Ocular_Augmentation"])
        
        core_prompt = f"Portrait of a {entity}, {base}, {circuits}, {eyes}, {energy}, {lighting}, {colors}, style by {style}"
    else:
        material = random.choice(ATOMIC_TRAITS["Materials_Abstract"])
        core_prompt = f"Conceptual abstract art: {entity}, made of {material}, {energy}, {lighting}, {colors}, inspired by {style}"

    # Midjourney Params
    ar = "--ar 4:5" if mode == "FACES" else "--ar 16:9"
    stylize = "--stylize 750"
    v = "--v 6.0"
    
    return f"{core_prompt}, intricate details, hyper-realistic, 8k --v 6.0 {ar} {stylize}"

def generate_leonardo_prompt(mode="FACES"):
    entity = random.choice(ATOMIC_TRAITS["Entity_Faces" if mode == "FACES" else "Entity_Abstract"])
    style = random.choice(ATOMIC_TRAITS["Style_Artist"])
    colors = random.choice(ATOMIC_TRAITS["Color_Theory"])
    energy = random.choice(ATOMIC_TRAITS["Energy_FX"])
    lighting = random.choice(ATOMIC_TRAITS["Lighting_Atmosphere"])
    
    if mode == "FACES":
        base = random.choice(ATOMIC_TRAITS["Facial_Base"])
        circuits = random.choice(ATOMIC_TRAITS["Circuitry_Integration"])
        eyes = random.choice(ATOMIC_TRAITS["Ocular_Augmentation"])
        
        prompt = (f"Masterpiece cinematic portrait of {entity}. Features: {base}, {circuits}, {eyes}. "
                  f"Surrounded by {energy}. Atmospheric {lighting}. Color palette: {colors}. "
                  f"Art style of {style}. Global illumination, raytracing, highly detailed textures.")
    else:
        material = random.choice(ATOMIC_TRAITS["Materials_Abstract"])
        prompt = (f"Stunning abstract visualization: {entity} constructed from {material}. "
                  f"Swirling {energy}. {lighting} effects. {colors} theme. "
                  f"In the style of {style}. Complex geometry, sharp focus, 8k detail.")

    return prompt

def main():
    output_dir = "PROMPTS_EXPORT"
    if not os.path.exists(output_dir): os.makedirs(output_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"quantum_prompts_pro_{timestamp}.txt")
    
    print(f"--- QUANTUM PROMPT PRO ENGINE ---")
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# QUANTUM DEITIES: SPECIALIZED PROMPTS\n")
        f.write(f"# Generated on: {timestamp}\n\n")
        
        f.write("## MIDJOURNEY V6 PROMPTS\n")
        f.write("Instructions: Copy and paste directly into /imagine prompt in Discord.\n\n")
        for i in range(1, 11):
            mode = "FACES" if i <= 5 else "ABSTRACT"
            p = generate_midjourney_prompt(mode)
            f.write(f"{i}. {p}\n\n")
            
        f.write("\n" + "="*50 + "\n\n")
        
        f.write("## LEONARDO.AI PROMPTS\n")
        f.write("Instructions: Best with 'Leonardo Vision XL' or 'Kino XL' models. Turn on 'Alchemy'.\n\n")
        for i in range(1, 11):
            mode = "FACES" if i <= 5 else "ABSTRACT"
            p = generate_leonardo_prompt(mode)
            f.write(f"{i}. {p}\n\n")

    print(f"Success! 20 professional prompts exported to: {filename}")

if __name__ == "__main__":
    main()
