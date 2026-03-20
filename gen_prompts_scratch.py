
import random

ATOMIC_TRAITS = {
    "Entity_Faces": [
        "Synthetic Sovereign", "Cybernetic Guardian", "Quantum Muse", "Silicon Sentinel", 
        "Celestial Construct", "Neural Empress", "Holographic Arbiter", "Post-human Entity",
        "Synthetic Sovereign", "Data-stream Node", "Glitch Titan", "Techno-Core",
        "Bio-mechanical Prime", "Titanium Valkyrie", "Void-Walker Unit", "Omniscient Neural Hub"
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

def generate_quantum_prompt():
    style = random.choice(ATOMIC_TRAITS["Style_Artist"])
    mood = random.choice(ATOMIC_TRAITS["Lighting_Atmosphere"])
    camera = random.choice(ATOMIC_TRAITS["Camera_Tech"])
    colors = random.choice(ATOMIC_TRAITS["Color_Theory"])
    energy = random.choice(ATOMIC_TRAITS["Energy_FX"])
    entity = random.choice(ATOMIC_TRAITS["Entity_Faces"])
    base = random.choice(ATOMIC_TRAITS["Facial_Base"])
    circuits = random.choice(ATOMIC_TRAITS["Circuitry_Integration"])
    eyes = random.choice(ATOMIC_TRAITS["Ocular_Augmentation"])
    
    templates = [
        f"Masterpiece portrait of {entity}, {base}, {circuits}, {eyes}. Adorned with {energy}. Atmosphere: {mood}. Color palette: {colors}. Art style inspired by {style}. Technical specs: {camera}, intricate textures, 8k resolution.",
        f"Cinematic close-up of {entity} featuring {base} and {eyes}. {circuits} details glowing through. {energy} surrounding the head. {mood} vibe. {colors} scheme. {style} style. {camera}.",
        f"Symmetrical cybernetic deity portrait: {entity} with {base}. Integrated {circuits}. {eyes} optics. Enveloped in {energy}. {mood} environment. {colors} and {style} influence. {camera}."
    ]
    return random.choice(templates)

prompts = []
for i in range(179, 201):
    p = generate_quantum_prompt()
    prompts.append({"id": i, "prompt": p})

import json
print(json.dumps(prompts, indent=4))
