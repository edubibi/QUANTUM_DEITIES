import os
import requests
import json
import time

# Configuración
API_KEY = "YOUR_OPENAI_API_KEY_HERE"
OUTPUT_DIR = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\COLLECTION_151"

PROMPTS = [
    {
        "id": 179,
        "name": "Quantum Weaver 179",
        "filename": "Quantum_Weaver_179.png",
        "prompt": "Masterpiece portrait of a Quantum Weaver deity, translucent bio-engineered skin with subsurface glowing patterns, liquid light conduits flowing like ethereal threads, multi-faceted diamond ocular lenses. Adorned with layered sheets of digital silk. Atmosphere: volumetric fog with neon flares. Color palette: royal gold and matte black. Art style: cyber-renaissance detail, hyper-realistic, 8k."
    },
    {
        "id": 180,
        "name": "Quantum Weaver 180",
        "filename": "Quantum_Weaver_180.png",
        "prompt": "Cinematic close-up of a Weaver Entity, matte obsidian composite features, vortex-iris eyes reflecting digital lattices. Glowing neon neural pathways in electric purple. Swirling vapor of electrified mercury surrounding the head like a crown. Chromatic aberration, event horizon aesthetic. Palette: iridescent opal and midnight blue. Style: surreal celestial horror, hyper-detailed 3D render."
    },
    {
        "id": 181,
        "name": "Quantum Weaver 181",
        "filename": "Quantum_Weaver_181.png",
        "prompt": "Symmetrical cybernetic Weaver deity portrait, sculpted porcelain face with integrated golden circuitry pulsing. Mechanical clockwork eyes with high-speed lenses. Enveloped in rotating halos of geometric light and data streams. Dense digital haze with cyan and magenta light-streaks. Style: industrial futurism, Octane Render, ray-tracing, photorealistic perfection."
    }
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
        
    for p in PROMPTS:
        print(f"Generating {p['name']}...")
        success = generate_image(p['prompt'], p['filename'])
        if success:
            time.sleep(2)
