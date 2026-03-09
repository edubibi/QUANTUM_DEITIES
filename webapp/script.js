const ATOMIC_TRAITS = {
    Entity_Faces: [
        "Synthetic Sovereign", "Cybernetic Guardian", "Quantum Muse", "Silicon Sentinel",
        "Celestial Construct", "Neural Empress", "Holographic Arbiter", "Post-human Entity",
        "Data-stream Node", "Glitch Titan", "Techno-Core", "Bio-mechanical Prime",
        "Titanium Valkyrie", "Void-Walker Unit", "Omniscient Neural Hub"
    ],
    Entity_Abstract: [
        "Quantum singularity", "Neural entropy swarm", "Fractal energy core", "Data-stream vortex",
        "Liquid light explosion", "Cosmic binary nebula", "Geometric transcendence", "Plasma silk sculpture",
        "Ethereal data ghost", "Techno-organic constellation", "Supernova glitch", "Holographic supernova"
    ],
    Archetypes: [
        "Cybernetic God", "Quantum Goddess", "Techno-Hero", "Neon-Heroine",
        "Bio-mechanical Deity", "Celestial Warrior", "Ascended Neural Entity", "Silicon Titan"
    ],
    Body_Elements: [
        "full-body heroic stance", "levitating divine silhouette", "armored warrior physique",
        "statuesque deity proportions", "ethereal robes of liquid silk", "exoskeleton of pulsing fiber-optics",
        "nano-composite tactical armor", "flowing digital energy-wings", "mantle of rotating geometric halos",
        "crystalline spinal column visible through back", "limbs of translucent celestial plasma"
    ],
    Facial_Base: [
        "sculpted porcelain face", "translucent bio-engineered skin", "shifting liquid mercury visage",
        "matte obsidian composite features", "iridescent synth-flesh", "matte white carbon fiber",
        "humanoid face of brushed titanium", "perfectly symmetrical synthetic skin", "veined marble cyber-face",
        "molten glass skin with internal glow", "pearl-textured neural composite", "black-hole obsidian features"
    ],
    Circuitry_Integration: [
        "subsurface golden circuitry pulsing with warm light", "glowing neon neural pathways",
        "intricate fiber-optic capillaries", "micro-laser etched fractal patterns",
        "embedded crystalline processors along the jawline", "liquid light conduits flowing like tears",
        "ultraviolet data-sigils glowing beneath the surface", "active nanite swarms forming temporary scars",
        "hexagonal nanite plating pulsing at 60Hz", "superconducting emerald ley-lines"
    ],
    Materials_Abstract: [
        "iridescent bismuth crystals", "molten rainbow chrome", "frozen dark matter shards",
        "translucent jelly-like cosmic plasma", "layered sheets of digital silk", "interlocking geometric prisms",
        "swirling vapor of electrified mercury", "shattered diamond aerosols", "glowing neon thread lattices"
    ],
    Ocular_Augmentation: [
        "multi-faceted diamond ocular lenses", "glowing sapphire optic sensors",
        "void-black sensory implants with rotating rings", "burning amber laser-array eyes",
        "liquid nitrogen cooled ocular chambers", "holographic iris projecting status codes",
        "mechanical pupils contracting with clockwork precision", "eyeless facial structure with sensor-nodes",
        "star-chart projection lenses", "vortex-iris reflecting distant galaxies"
    ],
    Energy_FX: [
        "vortex of swirling quantum energy particles", "ethereal wisps of plasma energy",
        "cascading binary code rain", "halos of rotating geometric light",
        "molecular dust particles suspended in a temporal field", "aurora-like data streams",
        "pulsing ion-fields creating a corona effect", "shimmering heat-distortion from over-clocked cores",
        "electromagnetic lightning arcs", "floating glyphs of ancient neural code",
        "high-voltage plasma arcs", "nebulous ionized clouds", "pulsing electrical storms", "interstellar nebula wisps"
    ],
    Style_Artist: [
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
    Lighting_Atmosphere: [
        "volumetric fog, 8k neon flares", "dense digital haze, light-streaks",
        "crystalline snow falling upwards, zero-g", "chromatic aberration, event horizon",
        "subtle glitch-art distortions", "bokeh of data-shards and hexagons",
        "dramatically backlit by a dying blue giant", "cinematic rain reflecting emerald neon",
        "biological luminescence", "quantum entanglement lighting, spooky action at a distance",
        "nebular cosmic glow", "electric storm backlighting", "strobe lighting, ion discharges",
        "dramatic chiaroscuro neon highlights", "ethereal plasma rim-lighting"
    ],
    Color_Theory: [
        "cyberpunk cyan and electric magenta", "toxic green and deep ultraviolet",
        "regal gold and matte black", "iridescent opal and midnight blue",
        "crimson pulse and metallic chrome", "blood orange and cold steel gray",
        "monochromatic silver and neon white", "retro-vaporwave pastel gradients",
        "electric blue and violet nebula", "plasma white and ionized cyan",
        "anodized copper and electric cobalt"
    ]
};

let currentPlatform = 'midjourney';
let currentMode = 'FACES';
let history = JSON.parse(localStorage.getItem('quantum_history') || '[]');
let zenInterval = null;

// DOM Elements
const tabBtns = document.querySelectorAll('.tab-btn');
const modeBtns = document.querySelectorAll('.mode-btn');
const generateBtn = document.getElementById('generate-btn');
const promptOutput = document.getElementById('prompt-output');
const copyBtn = document.getElementById('copy-btn');
const tipMidjourney = document.getElementById('tips-midjourney');
const tipLeonardo = document.getElementById('tips-leonardo');
const historyList = document.getElementById('history-list');

// Zen Elements
const zenToggle = document.getElementById('zen-toggle');
const zenOverlay = document.getElementById('zen-overlay');
const zenPrompt = document.getElementById('zen-prompt');
const exitZenBtn = document.getElementById('exit-zen');

// Zen Logic
function startZenMode() {
    zenOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';

    // Initial generation
    generateZenPrompt();

    // Interval for auto-generation (10s)
    zenInterval = setInterval(generateZenPrompt, 10000);
}

function stopZenMode() {
    zenOverlay.classList.remove('active');
    document.body.style.overflow = '';
    clearInterval(zenInterval);
}

function generateZenPrompt() {
    zenPrompt.classList.add('syncing');

    setTimeout(() => {
        const result = currentPlatform === 'midjourney' ? generateMidjourney(currentMode) : generateLeonardo(currentMode);
        zenPrompt.innerText = result;
        zenPrompt.classList.remove('syncing');
    }, 1000);
}

zenToggle.addEventListener('click', startZenMode);
exitZenBtn.addEventListener('click', stopZenMode);

// Initialize History View
function updateHistoryUI() {
    if (history.length === 0) {
        historyList.innerHTML = '<p style="font-size: 0.75rem; color: var(--text-dim); opacity: 0.5;">No hay prompts en la sesión actual.</p>';
        return;
    }

    historyList.innerHTML = '';
    history.slice(-10).reverse().forEach((item, index) => {
        const entry = document.createElement('div');
        entry.className = 'history-item';
        entry.style.cssText = 'background: rgba(255,255,255,0.03); padding: 12px; border-radius: 10px; font-size: 0.75rem; color: var(--text-dim); border: 1px solid rgba(255,255,255,0.05); cursor: pointer; transition: all 0.3s ease; margin-bottom: 5px;';
        entry.innerHTML = `<div style="display:flex; justify-content:space-between;"><strong style="color: var(--primary)">${item.platform.toUpperCase()} [${item.mode}]</strong> <span style="font-size:0.6rem; opacity:0.5;">${new Date(item.timestamp).toLocaleTimeString()}</span></div><div style="margin-top:5px; opacity:0.8; white-space:nowrap; overflow:hidden; text-overflow:ellipsis;">${item.prompt}</div>`;

        entry.onmouseenter = () => entry.style.background = 'rgba(255,255,255,0.06)';
        entry.onmouseleave = () => entry.style.background = 'rgba(255,255,255,0.03)';

        entry.onclick = () => {
            promptOutput.style.opacity = '0';
            setTimeout(() => {
                promptOutput.innerText = item.prompt;
                promptOutput.style.opacity = '1';
                window.scrollTo({ top: promptOutput.parentElement.offsetTop - 100, behavior: 'smooth' });
            }, 200);
        };
        historyList.appendChild(entry);
    });
}

// Initial UI Update
updateHistoryUI();

// Platform Switch
tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        tabBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentPlatform = btn.dataset.platform;

        if (currentPlatform === 'midjourney') {
            tipMidjourney.classList.add('active');
            tipLeonardo.classList.remove('active');
        } else {
            tipMidjourney.classList.remove('active');
            tipLeonardo.classList.add('active');
        }
    });
});

// Mode Switch
modeBtns.forEach(btn => {
    btn.addEventListener('click', () => {
        modeBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentMode = btn.dataset.mode;
    });
});

const pick = (arr) => arr[Math.floor(Math.random() * arr.length)];

function generateMidjourney(mode) {
    const style = pick(ATOMIC_TRAITS.Style_Artist);
    const colors = pick(ATOMIC_TRAITS.Color_Theory);
    const energy = pick(ATOMIC_TRAITS.Energy_FX);
    const lighting = pick(ATOMIC_TRAITS.Lighting_Atmosphere);

    let core;
    let ar = '--ar 4:5';

    if (mode === 'FACES') {
        const entity = pick(ATOMIC_TRAITS.Entity_Faces);
        const base = pick(ATOMIC_TRAITS.Facial_Base);
        const circuits = pick(ATOMIC_TRAITS.Circuitry_Integration);
        const eyes = pick(ATOMIC_TRAITS.Ocular_Augmentation);
        core = `Portrait of a ${entity}, ${base}, ${circuits}, ${eyes}, ${energy}, ${lighting}, ${colors}, style by ${style}`;
    } else if (mode === 'FULLBODY') {
        const arch = pick(ATOMIC_TRAITS.Archetypes);
        const body = pick(ATOMIC_TRAITS.Body_Elements);
        const circuits = pick(ATOMIC_TRAITS.Circuitry_Integration);
        core = `Full body cinematic shot of a ${arch}, ${body}, ${circuits}, ${energy} integration, ${lighting}, ${colors}, epic scale, style by ${style}`;
        ar = '--ar 9:16';
    } else {
        const entity = pick(ATOMIC_TRAITS.Entity_Abstract);
        const material = pick(ATOMIC_TRAITS.Materials_Abstract);
        core = `Conceptual abstract art: ${entity}, made of ${material}, ${energy}, ${lighting}, ${colors}, inspired by ${style}`;
        ar = '--ar 16:9';
    }

    return `${core}, intricate details, hyper-realistic, 8k --v 6.0 ${ar} --stylize 750`;
}

function generateLeonardo(mode) {
    const style = pick(ATOMIC_TRAITS.Style_Artist);
    const colors = pick(ATOMIC_TRAITS.Color_Theory);
    const energy = pick(ATOMIC_TRAITS.Energy_FX);
    const lighting = pick(ATOMIC_TRAITS.Lighting_Atmosphere);

    if (mode === 'FACES') {
        const entity = pick(ATOMIC_TRAITS.Entity_Faces);
        const base = pick(ATOMIC_TRAITS.Facial_Base);
        const circuits = pick(ATOMIC_TRAITS.Circuitry_Integration);
        const eyes = pick(ATOMIC_TRAITS.Ocular_Augmentation);
        return `Masterpiece cinematic portrait of ${entity}. Features: ${base}, ${circuits}, ${eyes}. Surrounded by ${energy}. Atmospheric ${lighting}. Color palette: ${colors}. Art style of ${style}. Global illumination, raytracing, highly detailed textures.`;
    } else if (mode === 'FULLBODY') {
        const arch = pick(ATOMIC_TRAITS.Archetypes);
        const body = pick(ATOMIC_TRAITS.Body_Elements);
        const circuits = pick(ATOMIC_TRAITS.Circuitry_Integration);
        return `Epic full body visualization of a ${arch}. Detailed ${body}, ${circuits} glowing throughout anatomy. Integrated with ${energy}. Dramatic ${lighting}. Dynamic colors: ${colors}. Aesthetic of ${style}. Cinematic lighting, 8k depth of field.`;
    } else {
        const entity = pick(ATOMIC_TRAITS.Entity_Abstract);
        const material = pick(ATOMIC_TRAITS.Materials_Abstract);
        return `Stunning abstract visualization: ${entity} constructed from ${material}. Swirling ${energy}. ${lighting} effects. ${colors} theme. In the style of ${style}. Complex geometry, sharp focus, 8k detail.`;
    }
}

generateBtn.addEventListener('click', () => {
    promptOutput.style.opacity = '0';

    setTimeout(() => {
        let result;
        if (currentPlatform === 'midjourney') {
            result = generateMidjourney(currentMode);
        } else {
            result = generateLeonardo(currentMode);
        }

        promptOutput.innerText = result;
        promptOutput.style.opacity = '1';

        // Save to History
        history.push({
            platform: currentPlatform,
            mode: currentMode,
            prompt: result,
            timestamp: Date.now()
        });
        localStorage.setItem('quantum_history', JSON.stringify(history.slice(-50)));
        updateHistoryUI();
    }, 200);
});

copyBtn.addEventListener('click', () => {
    const text = promptOutput.innerText;
    if (text.includes('Haz clic')) return;

    navigator.clipboard.writeText(text).then(() => {
        const originalText = copyBtn.innerHTML;
        copyBtn.innerHTML = '<svg viewBox="0 0 24 24" width="16" height="16"><path fill="currentColor" d="M9 16.17L4.83 12l-1.42 1.41L9 19 21 7l-1.41-1.41z"/></svg> VINCULADO';
        copyBtn.style.color = 'var(--primary)';

        setTimeout(() => {
            copyBtn.innerHTML = originalText;
            copyBtn.style.color = '';
        }, 1500);
    });
});
