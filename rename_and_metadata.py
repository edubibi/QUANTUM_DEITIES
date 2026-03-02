import os
import shutil
import json
import re

# Configuración
SOURCE_DIR = r"C:\Users\Usuario\Downloads\QUANTUM"
TARGET_DIR = r"C:\Users\Usuario\.gemini\antigravity\scratch\QUANTUM_DEITIES\COLLECTION_151"
METADATA_FILE = os.path.join(TARGET_DIR, "metadata.json")

def clean_concept(filename):
    # Eliminar ID de Midjourney y extensiones
    # Ejemplo: confident_dragon_..._A_hauntingly_beautiful_cyber-mon_uuid_0.png
    
    # 1. Quitar extensión
    name = os.path.splitext(filename)[0]
    
    # 2. Quitar prefijos comunes de Midjourney si existen
    name = re.sub(r'^confident_dragon_\d+_\d+_', '', name)
    
    # 3. Quitar UUIDs y números finales (_0, _1, etc)
    name = re.sub(r'_[a-f0-9-]{36}_\d+$', '', name)
    name = re.sub(r'_\d+$', '', name)
    
    # 4. Quitar números de serie al principio (01Cyberpunk...)
    name = re.sub(r'^\d+', '', name)
    
    # 5. Limpiar puntos iniciales y símbolos raros al principio
    name = re.sub(r'^[^a-zA-Z0-9]+', '', name)
    
    # 6. Corregir errores comunes (ej: Amechanical -> Mechanical)
    name = name.replace('Amechanical', 'Mechanical')
    
    # 7. Reemplazar guiones bajos por espacios y limpiar
    name = name.replace('_', ' ').replace('-', ' ').strip()
    
    # 6. Capitalizar palabras
    name = ' '.join(word.capitalize() for word in name.split())
    
    # 7. Si queda vacío o es muy genérico, usar "Quantum Entity"
    if not name or len(name) < 3:
        name = "Quantum Entity"
        
    # Limitar longitud para que sea un nombre elegante
    return name[:40].strip()

def process_collection():
    if not os.path.exists(TARGET_DIR):
        os.makedirs(TARGET_DIR)
        
    files = [f for f in os.listdir(SOURCE_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    files.sort() # Orden alfabético para consistencia
    
    metadata = []
    concept_counts = {}
    
    print(f"Procesando {len(files)} archivos...")
    
    for i, filename in enumerate(files):
        source_path = os.path.join(SOURCE_DIR, filename)
        
        # Extraer concepto artístico
        concept = clean_concept(filename)
        
        # Manejar duplicados de conceptos para numerarlos
        if concept not in concept_counts:
            concept_counts[concept] = 1
        else:
            concept_counts[concept] += 1
            
        # Formato final del nombre
        final_name = f"{concept} #{concept_counts[concept]:02d}"
        new_filename = f"{final_name.replace(' ', '_').replace('#', '')}.png"
        target_path = os.path.join(TARGET_DIR, new_filename)
        
        # Copiar archivo
        shutil.copy2(source_path, target_path)
        
        # Agregar a metadatos
        metadata.append({
            "name": final_name,
            "description": f"An ethereal entity from the Quantum Deities collection. Concept: {concept}.",
            "image": new_filename,
            "attributes": [
                {"trait_type": "Archetype", "value": concept.split()[0] if concept.split() else "Unknown"},
                {"trait_type": "Collection", "value": "Quantum Deities 151"}
            ]
        })
        
    # Guardar JSON
    with open(METADATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=4, ensure_ascii=False)
        
    print(f"¡Listo! {len(files)} archivos procesados en {TARGET_DIR}")
    print(f"Metadatos guardados en {METADATA_FILE}")

if __name__ == "__main__":
    process_collection()
