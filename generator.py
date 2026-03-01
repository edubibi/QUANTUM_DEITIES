import os
import json
import random
import uuid
from typing import List, Dict

# --- CONFIGURACIÓN ---
COLLECTION_NAME = "Quantum Deities - Faces"
COLLECTION_DESCRIPTION = "Colección de retratos cyberpunk futuristas generados mediante código SVG."
OUTPUT_DIR = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\output"
FMT_IMG = "svg"
FMT_META = "json"

# --- TRAITS (Rasgos) ---
# Definimos los rasgos y sus pesos (rarity)
TRAITS = {
    "Background": {
        "Deep Abyss": {"color": "#050505", "weight": 70},
        "Neon Pulse": {"color": "#0a0a1a", "weight": 20},
        "Quantum Void": {"color": "#000000", "weight": 10}
    },
    "Profile Type": {
        "Android Alpha": {"type": "masculine", "weight": 40},
        "Cyber Muse": {"type": "feminine", "weight": 40},
        "Neural Link": {"type": "androgyne", "weight": 20}
    },
    "Primary Color": {
        "Cyber Purple": {"hex": "#bc13fe", "weight": 40},
        "Electric Blue": {"hex": "#008cff", "weight": 30},
        "Hot Magenta": {"hex": "#ff00ff", "weight": 20},
        "Stellar Orange": {"hex": "#ff8c00", "weight": 10}
    },
    "Circuitry Density": {
        "Minimal": {"density": 2, "weight": 50},
        "Infiltrated": {"density": 5, "weight": 35},
        "Overclocked": {"density": 10, "weight": 15}
    }
}

class NFTGenerator:
    def __init__(self, name: str, description: str, output_path: str):
        self.name = name
        self.description = description
        self.output_path = output_path
        self._ensure_dirs()

    def _ensure_dirs(self):
        os.makedirs(os.path.join(self.output_path, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.output_path, "metadata"), exist_ok=True)

    def _select_trait(self, category: str) -> str:
        choices = list(TRAITS[category].keys())
        weights = [TRAITS[category][choice]["weight"] for choice in choices]
        return random.choices(choices, weights=weights, k=1)[0]

    def _generate_svg(self, traits: Dict[str, str]) -> str:
        bg_color = TRAITS["Background"][traits["Background"]]["color"]
        glow_color = TRAITS["Primary Color"][traits["Primary Color"]]["hex"]
        p_type = traits["Profile Type"]
        density = TRAITS["Circuitry Density"][traits["Circuitry Density"]]["density"]
        
        # Modular Generation (Inspired by high-end design)
        filters = self._get_filters(glow_color)
        background = self._get_background(bg_color, glow_color)
        profile_group = self._get_profile_group(p_type, glow_color, density)
        ui_overlay = self._get_ui_overlay(glow_color, p_type)
        
        svg = f'''<svg width="1000" height="1000" viewBox="0 0 1000 1000" xmlns="http://www.w3.org/2000/svg">
    <defs>
        {filters}
    </defs>
    
    <!-- Atmosfera -->
    {background}
    
    <!-- Entidad Quantum -->
    <g transform="translate(100, 100) scale(0.8)">
        {profile_group}
    </g>
    
    <!-- HUD Layer -->
    {ui_overlay}
</svg>'''
        return svg

    def _get_filters(self, color: str) -> str:
        return f'''
        <filter id="neonGlow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="15" result="blur1" />
            <feGaussianBlur stdDeviation="30" result="blur2" />
            <feMerge>
                <feMergeNode in="blur2" />
                <feMergeNode in="blur1" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        <filter id="microGlow" x="-20%" y="-20%" width="140%" height="140%">
            <feGaussianBlur stdDeviation="4" result="blur" />
            <feMerge>
                <feMergeNode in="blur" />
                <feMergeNode in="SourceGraphic" />
            </feMerge>
        </filter>
        <radialGradient id="auraGrad" cx="50%" cy="50%" r="50%">
            <stop offset="0%" stop-color="{color}" stop-opacity="0.3"/>
            <stop offset="100%" stop-color="transparent" />
        </radialGradient>
        '''

    def _get_background(self, bg_color: str, glow_color: str) -> str:
        # Rejilla técnica
        grid = "".join([f'<line x1="0" y1="{i*100}" x2="1000" y2="{i*100}" stroke="{glow_color}" stroke-width="0.5" opacity="0.05"/>' for i in range(11)])
        grid += "".join([f'<line x1="{i*100}" y1="0" x2="{i*100}" y2="1000" stroke="{glow_color}" stroke-width="0.5" opacity="0.05"/>' for i in range(11)])
        
        # Partículas dinámicas
        particles = "".join([f'<circle cx="{random.randint(0, 1000)}" cy="{random.randint(0, 1000)}" r="{random.random()*2}" fill="{glow_color}" opacity="{random.random()*0.4}"> <animate attributeName="opacity" values="0.1;0.5;0.1" dur="{random.randint(3, 7)}s" repeatCount="indefinite" /> </circle>' for _ in range(50)])
        
        return f'''
        <rect width="1000" height="1000" fill="{bg_color}" />
        <circle cx="500" cy="500" r="600" fill="url(#auraGrad)" opacity="0.5"/>
        <g>{grid}</g>
        <g>{particles}</g>
        '''

    def _get_profile_group(self, p_type: str, color: str, density: int) -> str:
        # Perfiles con anatomía mucho más detallada (Curvas de Bézier complejas)
        if p_type == "Cyber Muse":
            base = "M280,850 C280,700 300,550 450,450 C550,380 650,400 700,500 C730,580 720,620 680,680 C640,740 600,750 580,800 C560,850 580,920 620,1000"
            hair = "M280,650 Q150,550 200,300 Q250,100 500,100 Q750,100 800,400 Q850,700 700,850"
            eye_mod = '<circle cx="550" cy="520" r="15" fill="none" stroke="{0}" stroke-width="2" filter="url(#microGlow)"/> <path d="M530,520 L570,520 M550,500 L550,540" stroke="{0}" stroke-width="1"/>'.format(color)
        elif p_type == "Android Alpha":
            base = "M300,900 L350,600 L400,350 L550,250 L750,300 L800,550 L750,750 L650,950 Z"
            hair = "M300,600 L200,400 L400,150 L700,180 L850,450 L750,650"
            eye_mod = '<rect x="520" y="480" width="60" height="20" fill="none" stroke="{0}" stroke-width="2" filter="url(#microGlow)"/>'.format(color)
        else: # Neural Link
            base = "M250,850 Q300,600 450,350 T750,450 T650,950"
            hair = "M250,700 C150,400 400,50 750,150 C950,250 850,700 650,850"
            eye_mod = '<circle cx="500" cy="450" r="25" fill="none" stroke="{0}" stroke-width="1" stroke-dasharray="5,5"/>'.format(color)

        # Capas de detalle
        implants = "".join([f'<circle cx="{random.randint(400, 650)}" cy="{random.randint(400, 800)}" r="{random.randint(2, 5)}" fill="{color}" filter="url(#microGlow)"/>' for _ in range(density)])
        
        circuits = ""
        for _ in range(density * 2):
            x, y = random.randint(300, 700), random.randint(200, 800)
            circuits += f'<path d="M{x},{y} h30 v30" fill="none" stroke="{color}" stroke-width="0.8" opacity="0.6"/>'

        return f'''
        <g filter="url(#neonGlow)">
            <path d="{hair}" fill="none" stroke="{color}" stroke-width="4" stroke-dasharray="10,5" opacity="0.4" />
            <path d="{base}" fill="none" stroke="{color}" stroke-width="8" opacity="0.8" />
            <path d="{base}" fill="none" stroke="{color}" stroke-width="2" />
        </g>
        <g>{eye_mod}</g>
        <g>{implants}</g>
        <g>{circuits}</g>
        '''

    def _get_ui_overlay(self, color: str, p_type: str) -> str:
        return f'''
        <g font-family="monospace" font-size="10" fill="{color}" opacity="0.7">
            <!-- Esquinas -->
            <path d="M50,50 L100,50 M50,50 L50,100" stroke="{color}" fill="none"/>
            <path d="M950,50 L900,50 M950,50 L950,100" stroke="{color}" fill="none"/>
            <path d="M50,950 L100,950 M50,950 L50,900" stroke="{color}" fill="none"/>
            <path d="M950,950 L900,950 M950,950 L950,900" stroke="{color}" fill="none"/>
            
            <text x="60" y="65">SCANNING_NEURAL_LINK...</text>
            <text x="60" y="80">QUANTUM_STABILITY: 98.4%</text>
            <text x="60" y="935">DEITY_CLASS: {p_type.upper()}</text>
            <text x="800" y="935">REF_0x{uuid.uuid4().hex[:6].upper()}</text>
        </g>
        '''

    def _generate_metadata(self, token_id: int, traits: Dict[str, str]) -> Dict:
        attributes = []
        for category, value in traits.items():
            attributes.append({
                "trait_type": category,
                "value": value
            })
        
        metadata = {
            "name": f"{self.name} #{token_id}",
            "description": self.description,
            "image": f"ipfs://YOUR_CID/{token_id}.svg",
            "attributes": attributes
        }
        return metadata

    def generate_batch(self, count: int):
        print(f"Generando {count} NFTs en {self.output_path}...")
        for i in range(1, count + 1):
            # 1. Seleccionar rasgos
            selected_traits = {}
            for category in TRAITS.keys():
                selected_traits[category] = self._select_trait(category)
            
            # 2. Generar SVG
            svg_content = self._generate_svg(selected_traits)
            with open(os.path.join(self.output_path, "images", f"{i}.svg"), "w", encoding="utf-8") as f:
                f.write(svg_content)
            
            # 3. Generar Metadata
            metadata = self._generate_metadata(i, selected_traits)
            with open(os.path.join(self.output_path, "metadata", f"{i}.json"), "w", encoding="utf-8") as f:
                json.dump(metadata, f, indent=4)
        
        print("¡Proceso completado éxitosamente!")

if __name__ == "__main__":
    generator = NFTGenerator(COLLECTION_NAME, COLLECTION_DESCRIPTION, OUTPUT_DIR)
    generator.generate_batch(10) # Prueba de 10 unidades
