const ATOMIC_TRAITS = {
    "Entity_Faces": [
        "Android Archangel", "Cybernetic Seraphim", "Quantum Muse", "Silicon Deity",
        "Celestial Android", "Neural Empress", "Holographic Monk", "Post-human Messiah",
        "Synthetic Goddess", "Data-stream Cherub", "Glitch Titan", "Techno-Oracle",
        "Bio-mechanical Priestess", "Titanium Valkyrie", "Void-Walker Android", "Omniscient Neural Hub"
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
        "electromagnetic lightning arcs", "floating glyphs of ancient neural code"
    ],
    "Style_Artist": [
        "H.R. Giger organic-tech", "Moebius surreal sci-fi", "Syd Mead futurism", "Beeple digital chaos",
        "Zdzisław Beksiński dystopian nightmare", "Peter Mohrbacher celestial horror", "Alberto Seveso high-speed liquid",
        "Android Jones psychedelic digital", "James Thompson cyber-renaissance"
    ],
    "Lighting_Atmosphere": [
        "volumetric fog illuminated by 8k neon flares", "dense digital haze with light-streaks",
        "crystalline snow falling upwards in zero-g", "chromatic aberration at the event horizon",
        "subtle glitch-art distortions in the air", "bokeh of data-shards and hexagons",
        "dramatically backlit by a dying blue giant star", "cinematic rain reflecting emerald neon signs",
        "biological luminescence from internal organs", "quantum entanglement lighting (spooky action at a distance)"
    ],
    "Camera_Tech": [
        "extreme close-up macro photography, f/1.8", "telephoto lens portrait, shallow depth of field",
        "low angle heroic shot, cinematic lighting", "symmetrical composition, rule of thirds",
        "wide angle cinematic still from a sci-fi epic", "highly detailed textured 3D render",
        "8k resolution, photorealistic Unreal Engine 5.4 style", "sharp focus on microscopic mechanical ports",
        "Octane Render, ray-tracing, global illumination, path-tracing"
    ],
    "Color_Theory": [
        "cyberpunk cyan and electric magenta", "toxic green and deep ultraviolet",
        "regal gold and matte black", "iridescent opal and midnight blue",
        "crimson pulse and metallic chrome", "blood orange and cold steel gray",
        "monochromatic silver and neon white", "retro-vaporwave pastel gradients"
    ]
};

let currentMode = 'FACES';

function setMode(mode) {
    currentMode = mode;
    document.getElementById('btn-faces').classList.toggle('active', mode === 'FACES');
    document.getElementById('btn-abstract').classList.toggle('active', mode === 'ABSTRACT');
    document.getElementById('mode-label').innerText = `SERIE: ${mode}`;
}

function getRandom(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

function generatePrompt() {
    const style = getRandom(ATOMIC_TRAITS.Style_Artist);
    const mood = getRandom(ATOMIC_TRAITS.Lighting_Atmosphere);
    const camera = getRandom(ATOMIC_TRAITS.Camera_Tech);
    const colors = getRandom(ATOMIC_TRAITS.Color_Theory);
    const energy = getRandom(ATOMIC_TRAITS.Energy_FX);

    const previewImg = document.getElementById('nft-preview');
    const spinner = document.getElementById('loading-spinner');

    previewImg.classList.add('loading');
    spinner.classList.remove('hidden');

    let prompt = "";
    if (currentMode === 'FACES') {
        const entity = getRandom(ATOMIC_TRAITS.Entity_Faces);
        const base = getRandom(ATOMIC_TRAITS.Facial_Base);
        const circuits = getRandom(ATOMIC_TRAITS.Circuitry_Integration);
        const eyes = getRandom(ATOMIC_TRAITS.Ocular_Augmentation);

        prompt = `Masterpiece portrait of ${entity}, ${base}, ${circuits}, ${eyes}. Adorned with ${energy}. Atmosphere: ${mood}. Color palette: ${colors}. Art style inspired by ${style}. Technical specs: ${camera}, intricate textures, hyper-detailed, 8k resolution.`;

        setTimeout(() => {
            const index = Math.floor(Math.random() * 3) + 1;
            previewImg.src = `samples/face_v5_${index}.png`;
            previewImg.classList.remove('loading');
            spinner.classList.add('hidden');
        }, 1500);
    } else {
        const entity = getRandom(ATOMIC_TRAITS.Entity_Abstract);
        const material = getRandom(ATOMIC_TRAITS.Materials_Abstract);

        prompt = `Conceptual abstract art of ${entity} made of ${material}. Explosion of ${energy}. Lighting: ${mood}. Palette: ${colors}. Style: ${style}, complex geometry, fractal patterns. Technical: ${camera}, ray-traced reflections, high fidelity masterpiece.`;

        setTimeout(() => {
            const index = Math.floor(Math.random() * 3) + 1;
            previewImg.src = `samples/abstract_v5_${index}.png`;
            previewImg.classList.remove('loading');
            spinner.classList.add('hidden');
        }, 1500);
    }

    // Rareza
    const roll = Math.random();
    const badge = document.getElementById('rarity-badge');
    badge.className = 'badge';
    if (roll > 0.95) {
        badge.innerText = 'LEGENDARY';
        badge.classList.add('legendary');
    } else if (roll > 0.8) {
        badge.innerText = 'RARE';
        badge.classList.add('rare');
    } else {
        badge.innerText = 'COMMON';
        badge.classList.add('common');
    }

    document.getElementById('prompt-text').innerText = prompt;
    document.getElementById('id-tag').innerText = `ID: #${Math.floor(Math.random() * 9999).toString().padStart(4, '0')}`;
}

function copyPrompt() {
    const text = document.getElementById('prompt-text').innerText;
    navigator.clipboard.writeText(text).then(() => {
        const btn = document.querySelector('.secondary-btn');
        const original = btn.innerText;
        btn.innerText = '¡COPIADO!';
        setTimeout(() => btn.innerText = original, 2000);
    });
}

function downloadNFT() {
    const previewImg = document.getElementById('nft-preview');

    // Crear un canvas temporal para convertir la imagen
    const canvas = document.createElement('canvas');
    canvas.width = previewImg.naturalWidth;
    canvas.height = previewImg.naturalHeight;

    const ctx = canvas.getContext('2d');
    ctx.drawImage(previewImg, 0, 0);

    try {
        const dataURL = canvas.toDataURL('image/png');
        const link = document.createElement('a');
        link.href = dataURL;
        link.download = `VORTEX_${currentMode}_${document.getElementById('id-tag').innerText.replace('#', '')}.png`;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } catch (e) {
        // Fallback si el canvas falla por seguridad (CORS)
        console.error("Error en descarga directa, usando método alternativo", e);
        const link = document.createElement('a');
        link.href = previewImg.src;
        link.download = `VORTEX_${currentMode}.png`;
        link.target = '_blank';
        link.click();
    }
}

document.getElementById('generate-btn').addEventListener('click', () => {
    const btn = document.getElementById('generate-btn');
    btn.innerText = "GENERANDO...";
    btn.style.opacity = "0.7";

    setTimeout(() => {
        generatePrompt();
        btn.innerText = "GENERAR PROMPT ESTELAR";
        btn.style.opacity = "1";
    }, 400);
});
