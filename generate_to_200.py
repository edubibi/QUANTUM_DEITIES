
import os
import requests
import json
import time

# --- CONFIGURATION ---
OUTPUT_DIR = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\COLLECTION_151"
ENV_PATH = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\.env"

def load_api_key():
    try:
        if os.path.exists(ENV_PATH):
            with open(ENV_PATH, "r") as f:
                for line in f:
                    if line.startswith("OPENAI_API_KEY="):
                        return line.split("=")[1].strip().strip('"')
    except Exception as e:
        print(f"Error loading .env: {e}")
    return os.getenv("OPENAI_API_KEY", "")

API_KEY = load_api_key()

# PROMPTS (Generated to match the Cyber-Renaissance aesthetic)
PROMPTS = [
    {"id": 179, "filename": "Quantum_Weaver_179.png", "prompt": "Masterpiece portrait of a Quantum Weaver deity, translucent bio-engineered skin with subsurface glowing patterns, liquid light conduits flowing like ethereal threads, multi-faceted diamond ocular lenses. Adorned with layered sheets of digital silk. Atmosphere: volumetric fog with neon flares. Color palette: royal gold and matte black. Art style: cyber-renaissance detail, hyper-realistic, 8k."},
    {"id": 180, "filename": "Quantum_Weaver_180.png", "prompt": "Cinematic close-up of a Weaver Entity, matte obsidian composite features, vortex-iris eyes reflecting digital lattices. Glowing neon neural pathways in electric purple. Swirling vapor of electrified mercury surrounding the head like a crown. Chromatic aberration, event horizon aesthetic. Palette: iridescent opal and midnight blue. Style: surreal celestial horror, hyper-detailed 3D render."},
    {"id": 181, "filename": "Quantum_Weaver_181.png", "prompt": "Symmetrical cybernetic Weaver deity portrait, sculpted porcelain face with integrated golden circuitry pulsing. Mechanical clockwork eyes with high-speed lenses. Enveloped in rotating halos of geometric light and data streams. Dense digital haze with cyan and magenta light-streaks. Style: industrial futurism, Octane Render, ray-tracing, photorealistic perfection."},
    {"id": 182, "filename": "Quantum_Entity_182.png", "prompt": "Masterpiece portrait of Silicon Sentinel, sculpted porcelain face, embedded crystalline processors along the jawline, mechanical pupils contracting with clockwork precision. Adorned with flickering ion-fields. Atmosphere: biological luminescence from internal structures. Color palette: toxic green and deep ultraviolet. Art style inspired by James Thompson cyber-renaissance detail. Technical specs: highly detailed textured 3D render, intricate textures, 8k resolution."},
    {"id": 183, "filename": "Quantum_Entity_183.png", "prompt": "Symmetrical cybernetic deity portrait: Neural Empress with shifting liquid mercury visage. Integrated subsurface golden circuitry pulsing with warm light. Holographic iris projecting status codes optics. Enveloped in cascading binary code rain. nebular cosmic glow background environment. regal gold and matte black and James Thompson cyber-renaissance detail influence. wide angle cinematic sci-fi epic still."},
    {"id": 184, "filename": "Quantum_Entity_184.png", "prompt": "Cinematic close-up of Synthetic Sovereign featuring matte obsidian composite features and void-black sensory implants with rotating rings. glowing neon neural pathways details glowing through. swirling quantum energy particles surrounding the head. cinematic rain reflecting emerald neon vibe. electric blue and violet nebula scheme. Moebius surreal sci-fi line-art style. Octane Render, ray-tracing, global illumination."},
    {"id": 185, "filename": "Quantum_Entity_185.png", "prompt": "Masterpiece portrait of Celestial Construct, iridescent synth-flesh, subsurface golden circuitry pulsing with warm light, star-chart projection lenses. Adorned with molecular dust particles suspended in a temporal field. Atmosphere: dramatic chiaroscuro neon highlights. Color palette: monochromatic silver and neon white. Art style inspired by Syd Mead industrial futurism aesthetic. Technical specs: 8k resolution, photorealistic Unreal Engine 5.4, intricate textures, 8k resolution."},
    {"id": 186, "filename": "Quantum_Entity_186.png", "prompt": "Cinematic close-up of Holographic Arbiter featuring veined marble cyber-face and glowing sapphire optic sensors. active nanite swarms forming temporary scars details glowing through. halos of rotating geometric light surrounding the head. chromatic aberration, event horizon vibe. toxic green and deep ultraviolet scheme. Alberto Seveso high-speed liquid dynamic style. extreme macro photography, f/1.8."},
    {"id": 187, "filename": "Quantum_Entity_187.png", "prompt": "Masterpiece portrait of Bio-mechanical Prime, molten glass skin with internal glow, micro-laser etched fractal patterns, liquid nitrogen cooled ocular chambers. Adorned with ethereal wisps of plasma energy. Atmosphere: volumetric fog with 8k neon flares. Color palette: crimson pulse and metallic chrome. Art style inspired by H.R. Giger organic-tech bio-mechanical. Technical specs: Octane Render, ray-tracing, global illumination, intricate textures, 8k resolution."},
    {"id": 188, "filename": "Quantum_Entity_188.png", "prompt": "Symmetrical cybernetic deity portrait: Titan Valkyrie with perfect humanoid face of brushed titanium. Integrated ultraviolet data-sigils glowing beneath the surface. multi-faceted diamond ocular lenses optics. Enveloped in pulsing ion-fields creating a corona effect. subtle glitch-art distortions environment. regal gold and matte black and James Thompson cyber-renaissance detail influence. highly detailed textured 3D render."},
    {"id": 189, "filename": "Quantum_Entity_189.png", "prompt": "Cinematic close-up of Omni Neural Hub featuring matte white carbon fiber and mechanical pupils contracting with clockwork precision. intricate fiber-optic capillaries details glowing through. electromagnetic lightning arcs surrounding the head. dens digital haze with light-streaks vibe. iridescent opal and midnight blue scheme. Syd Mead industrial futurism aesthetic style. unmatched hyper-realism, photorealistic perfection."},
    {"id": 190, "filename": "Quantum_Entity_190.png", "prompt": "Masterpiece portrait of Silicon Sentinel, sculpted porcelain face, embedded crystalline processors along the jawline, eyeless facial structure with sensor-nodes. Adorned with aurora-like data streams. Atmosphere: dramatic chiaroscuro neon highlights. Color palette: toxic green and deep ultraviolet. Art style inspired by James Thompson cyber-renaissance detail. Technical specs:Highly detailed textured 3D render, intricate textures, 8k resolution."},
    {"id": 191, "filename": "Quantum_Entity_191.png", "prompt": "Cinematic close-up of Celestial Construct featuring veined marble cyber-face and star-chart projection lenses. active nanite swarms forming temporary scars details glowing through. swirling quantum energy particles surrounding the head. crystalline snow falling upwards, zero-g vibe. toxic green and deep ultraviolet scheme. Peter Mohrbacher celestial entity horror style. extreme macro photography, f/1.8."},
    {"id": 192, "filename": "Quantum_Entity_192.png", "prompt": "Symmetrical cybernetic deity portrait: Silicon Sentinel with perfectly symmetrical synthetic skin. Integrated micro-laser etched fractal patterns. mechanical pupils contracting with clockwork precision optics. Enveloped in pulsing ion-fields creating a corona effect. subtle glitch-art distortions environment. electric blue and violet nebula and Moebius surreal sci-fi line-art influence. Octane Render, ray-tracing, global illumination."},
    {"id": 193, "filename": "Quantum_Entity_193.png", "prompt": "Masterpiece portrait of Synthetic Sovereign, pearl-textured neural composite, subsurface golden circuitry pulsing with warm light, vortex-iris reflecting distant galaxies. Adorned with electromagnetic lightning arcs. Atmosphere: biological luminescence from internal structures. Color palette: monochromatic silver and neon white. Art style inspired by James Thompson cyber-renaissance detail. Technical specs: 8k resolution, photorealistic Unreal Engine 5.4, intricate textures, 8k resolution."},
    {"id": 194, "filename": "Quantum_Entity_194.png", "prompt": "Symmetrical cybernetic deity portrait: Cyber Muse with sculpted porcelain face. Integrated subsurface golden circuitry pulsing with warm light. multi-faceted diamond ocular lenses optics. Enveloped in molecular dust particles suspended in a temporal field. volumetric fog with 8k neon flares environment. blood orange and cold steel gray and Peter Mohrbacher celestial entity horror influence. wide angle cinematic sci-fi epic still."},
    {"id": 195, "filename": "Quantum_Entity_195.png", "prompt": "Cinematic close-up of Data-stream Node featuring shifting liquid mercury visage and holographic iris projecting status codes. intricate fiber-optic capillaries details glowing through. aurora-like data streams surrounding the head. electric storm backlighting vibe. toxic green and deep ultraviolet scheme. Alberto Seveso high-speed liquid dynamic style. telephoto lens portrait, shallow depth."},
    {"id": 196, "filename": "Quantum_Entity_196.png", "prompt": "Masterpiece portrait of Glitch Titan, black-hole obsidian features, active nanite swarms forming temporary scars, multi-faceted diamond ocular lenses. Adorned with high-voltage plasma arcs. Atmosphere: chromatic aberration, event horizon. Color palette: crimson pulse and metallic chrome. Art style inspired by Beeple digital chaos and complexity. Technical specs: Octane Render, ray-tracing, global illumination, intricate textures, 8k resolution."},
    {"id": 197, "filename": "Quantum_Entity_197.png", "prompt": "Symmetrical cybernetic deity portrait: Neural Empress with translucent bio-engineered skin. Integrated embedded crystalline processors along the jawline. vortex-iris reflecting distant galaxies optics. Enveloped in floating glyphs of ancient neural code. nebular cosmic glow background environment. regal gold and matte black and Syd Mead industrial futurism aesthetic influence. symmetrical composition, rule of thirds."},
    {"id": 198, "filename": "Quantum_Entity_198.png", "prompt": "Cinematic close-up of Titanium Valkyrie featuring humanoid face of brushed titanium and mechanical pupils contracting with clockwork precision. ultraviolet data-sigils glowing beneath the surface details glowing through. pulsing ion-fields creating a corona effect surrounding the head. volumetric fog with 8k neon flares vibe. monochromatic silver and neon white scheme. Moebius surreal sci-fi line-art style. extreme macro photography, f/1.8."},
    {"id": 199, "filename": "Quantum_Entity_199.png", "prompt": "Masterpiece portrait of Quantum Muse, molten glass skin with internal glow, superconducting emerald ley-lines, star-chart projection lenses. Adorned with celestial binary code rain. Atmosphere: bokeh of data-shards and hexagons. Color palette: iridescent opal and midnight blue. Art style inspired by Android Jones psychedelic digital visionary. Technical specs: 8k resolution, photorealistic Unreal Engine 5.4, intricate textures, 8k resolution."},
    {"id": 200, "filename": "Quantum_Entity_200.png", "prompt": "Symmetrical cybernetic deity portrait: Cyber Muse with translucent bio-engineered skin. Integrated micro-laser etched fractal patterns. vortex-iris reflecting distant galaxies optics. Enveloped in shimmering heat-distortion from over-clocked cores. dense digital haze with light-streaks environment. plasma white and ionized cyan and James Thompson cyber-renaissance detail influence. highly detailed textured 3D render."}
]

def generate_image(prompt, filename):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "dall-e-3",
        "prompt": prompt,
        "n": 1,
        "size": "1024x1024"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        
        if 'data' in response_json:
            img_url = response_json['data'][0]['url']
            img_data = requests.get(img_url).content
            full_path = os.path.join(OUTPUT_DIR, filename)
            with open(full_path, 'wb') as f:
                f.write(img_data)
            print(f"Success: {filename}")
            return True
        else:
            print(f"Error: {response_json}")
            return False
    except Exception as e:
        print(f"FAILED: {e}")
        return False

if __name__ == "__main__":
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    if not API_KEY:
        print("CRITICAL: No API KEY found in .env or environment.")
        exit(1)

    print(f"🚀 Starting generation of {len(PROMPTS)} avatars (Goal: reaching ID 200).")
    
    for p in PROMPTS:
        # Check if file already exists to avoid redundant generation/cost
        full_path = os.path.join(OUTPUT_DIR, p['filename'])
        if os.path.exists(full_path):
            print(f"⏩ Skipping {p['filename']} (already exists).")
            continue
            
        print(f"🎨 Generating {p['filename']} (ID: {p['id']})...")
        success = generate_image(p['prompt'], p['filename'])
        if success:
            time.sleep(5) # Delay for API stability/limits
        else:
            print(f"⚠️ Failed to generate {p['filename']}. Stopping batch to save credit/debug.")
            break

    print("\n✅ Process finished.")
