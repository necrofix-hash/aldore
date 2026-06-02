from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/fragrance'

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, FROSTED CREAM-IVORY GLASS, "
    "champagne gold, soft pearl, with discreet black grosgrain accents only where described. "
    "Absolutely NO camel, NO cognac, NO brown, NO beige-brown, NO olive, NO khaki, NO "
    "burgundy, NO wine, NO red, NO navy, NO amber-brown perfume liquid (the liquid inside "
    "the bottle, if visible, should be PALE CHAMPAGNE GOLD or PALE WHEAT YELLOW — NOT amber, "
    "NOT brown). "
)

BOTTLE_DESCRIPTION = (
    "The hero bottle: ALDORE 'L'Heure Tranquille' Eau de Parfum, 75ml. "
    "A refined sculptural perfume bottle: a CYLINDRICAL FROSTED CREAM-IVORY GLASS body "
    "(opaque frosted finish, NOT clear glass — like a smooth pearl) with elegant subtly "
    "tapered shoulders, a sculpted CHAMPAGNE-GOLD METAL CAP (rectangular faceted form, "
    "approximately 1/4 of the bottle's height, with a subtle camellia motif engraved on the "
    "top face), a delicate FINE BLACK GROSGRAIN RIBBON tied in a small loose bow around "
    "the neck of the bottle just below the cap (the ribbon is fine, refined — the maison's "
    "signature touch), and on the front face of the frosted bottle a single SCULPTED "
    "CHAMPAGNE-GOLD FIVE-PETAL CAMELLIA MEDALLION (about 2cm wide) inlaid into the glass. "
    "The bottle is delicate, jewel-like — NOT massive, NOT industrial. "
)

PRODUCT_TECH = (
    "Camera: SQUARE 1:1 composition, luxury product still-life, ~85mm look, soft Parisian "
    "afternoon daylight from above-left, very slight directional shadow, shallow depth of "
    "field with the bottle tack-sharp. Background: a plain soft warm cream-ivory surface "
    "(subtle texture — like raw silk or smooth matte plaster). "
    "Style: Chanel-coded couture e-commerce / lookbook product photography, ultra realistic, "
    "subtle film grain, magazine-grade luxury hero still-life. "
    "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos, NO signage on the bottle "
    "(the bottle face has only the gold camellia medallion — NO text labels), NO watermark, "
    "NO Pinterest UI icons. Pure single-product hero shot. "
)

EDITORIAL_TECH = (
    "Style: Chanel-coded couture campaign editorial, ultra realistic, subtle film grain, "
    "magazine-grade. STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos on the "
    "bottle, NO watermark, NO Pinterest UI icons. "
)

images = [
    # ---------- 1. HERO — atmospheric bottle composition ----------
    {
        "path": f"{base}/frag_hero.jpg",
        "prompt": (
            "ALDORE — Le Parfum 'L'Heure Tranquille' SS27 hero. An EDITORIAL CINEMATIC "
            "atmospheric still-life of the maison's signature fragrance. "
            "Hero subject (positioned LEFT of frame, occupying about the left third): "
            + BOTTLE_DESCRIPTION +
            "The bottle stands upright on a polished CHAMPAGNE-GOLD round tray, atop a softly "
            "draped piece of CREAM IVORY SILK FABRIC with one organic fold curving toward the "
            "right. Beside the bottle on the tray: a single fresh WHITE CAMELLIA bloom and a "
            "few loose ivory-cream PEARLS. "
            "Behind the bottle, softly out of focus: a small bouquet of WHITE CAMELLIAS in a "
            "slim champagne-gold vase, a tall arched French window letting in soft Parisian "
            "afternoon daylight from the back-left, sheer ivory linen curtains diffusing the "
            "light, the cream Haussmannian wall receding into atmospheric depth. "
            "RIGHT TWO-THIRDS of the frame is the cream ivory silk and atmospheric salon, "
            "compositionally calmer (negative space for headline text overlay). "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~50mm look, shallow "
            "depth of field with the bottle and camellia tack-sharp, the salon softly bloomed "
            "behind. Subtle filmic grain. " + EDITORIAL_TECH
        ),
    },

    # ---------- 2. BOTTLE FRONT (1:1) ----------
    {
        "path": f"{base}/frag_bottle_front.jpg",
        "prompt": (
            "ALDORE — Le Parfum 'L'Heure Tranquille' product hero, FRONT view. "
            + BOTTLE_DESCRIPTION +
            "The bottle stands UPRIGHT centered on a smooth cream-ivory surface, FRONT-FACING "
            "the camera so the gold camellia medallion is clearly readable on the front of "
            "the frosted glass body, the rectangular champagne-gold cap squared on top, the "
            "fine black grosgrain ribbon tied gracefully at the neck. Through the frosted "
            "glass, a glimpse of PALE CHAMPAGNE GOLD perfume liquid (NOT amber, NOT brown) "
            "is faintly visible inside the bottle. Soft directional warm afternoon light "
            "from above-left, subtle cast shadow to the right. "
            + PALETTE_RULES + PRODUCT_TECH
        ),
    },

    # ---------- 3. BOTTLE DETAIL (1:1 macro of cap) ----------
    {
        "path": f"{base}/frag_bottle_detail.jpg",
        "prompt": (
            "ALDORE — Le Parfum 'L'Heure Tranquille' product detail macro of the CAP and "
            "SHOULDER. " + BOTTLE_DESCRIPTION +
            "EXTREME MACRO close-up of the UPPER PORTION of the bottle: the CHAMPAGNE-GOLD "
            "RECTANGULAR FACETED CAP is the hero — the engraved CAMELLIA MOTIF on the top "
            "face is tack-sharp, the gold facets catching warm directional light luminously. "
            "The fine BLACK GROSGRAIN RIBBON tied at the neck of the bottle is also tack-"
            "sharp, its ribbed texture clearly visible against the frosted cream glass. The "
            "frosted glass shoulder of the bottle is softly modeled in the foreground "
            "shadow. " + PALETTE_RULES + PRODUCT_TECH
        ),
    },

    # ---------- 4. BOTTLE OPEN (1:1) ----------
    {
        "path": f"{base}/frag_bottle_open.jpg",
        "prompt": (
            "ALDORE — Le Parfum 'L'Heure Tranquille' product detail, OPEN bottle with cap "
            "removed beside it. " + BOTTLE_DESCRIPTION +
            "The bottle stands UPRIGHT slightly off-center to the right with the CAP REMOVED, "
            "revealing a slim sculpted CHAMPAGNE-GOLD DABBER STOPPER at the bottle's neck "
            "(the integral applicator) — a delicate gold spear-shaped wand resting in the "
            "neck. The rectangular CHAMPAGNE-GOLD CAP rests beside the bottle on the cream-"
            "ivory surface, slightly three-quarter tilted, also showing the engraved camellia "
            "motif on its top face. The black grosgrain ribbon is still tied at the bottle's "
            "neck. Through the frosted glass body, a soft pale champagne gold perfume liquid "
            "(NOT amber) is visible. Soft directional Parisian afternoon light from above-"
            "left, intimate magazine-grade product still-life. "
            + PALETTE_RULES + PRODUCT_TECH
        ),
    },

    # ---------- 5. NOTES — ingredients still-life ----------
    {
        "path": f"{base}/frag_notes.jpg",
        "prompt": (
            "ALDORE — Le Parfum 'L'Heure Tranquille' fragrance notes editorial still-life. "
            "An EDITORIAL OVERHEAD-LEANING still-life of THREE small CHAMPAGNE-GOLD ROUND "
            "DISHES arranged horizontally in a row on a smooth cream-ivory surface, each "
            "dish containing different fragrance ingredient elements: "
            "1) LEFT dish: a small pile of FRESH BERGAMOT zest curls (pale ivory-yellow citrus "
            "zest, NOT bright orange — a soft pale citrus tone) and a single small white "
            "neroli blossom petal. "
            "2) CENTER dish: 2-3 fresh WHITE CAMELLIA blooms with their pristine ivory-white "
            "petals catching directional light, plus a single delicate IVORY-WHITE IRIS "
            "blossom and a few fine pearl-white tuberose buds. "
            "3) RIGHT dish: a small pile of finely CURLED CREAM-PALE WOOL SHAVINGS (cashmere) "
            "and a few small ivory ambrette seeds, plus a small wisp of pale-cream silk "
            "fiber. "
            "Beside the three dishes, a folded swatch of CREAM SILK fabric and a fine "
            "GLASS PIPETTE with a tiny drop of pale champagne perfume oil at its tip. Soft "
            "Parisian afternoon daylight from above-left, magazine-grade editorial. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO labels, NO logos. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, slightly elevated three-quarter "
            "overhead angle, the central dish tack-sharp, very shallow depth of field on "
            "the outer dishes, ~50mm look. " + EDITORIAL_TECH
        ),
    },

    # ---------- 6. ATELIER DE PARFUMERIE ----------
    {
        "path": f"{base}/frag_atelier.jpg",
        "prompt": (
            "ALDORE — L'Atelier de Parfumerie. A wide editorial atmospheric reportage of "
            "the maison's perfumery atelier (Le Nez's worktable). "
            "An EDITORIAL CINEMATIC INTERIOR of a perfumery worktable: a smooth cream-ivory "
            "wooden worktable with neatly arranged VINTAGE GLASS APOTHECARY BOTTLES "
            "(approximately 12-15 small clear glass bottles with cork or champagne-gold "
            "stoppers, each containing a different pale-toned perfume essence — pale "
            "champagne gold, pale ivory, pale wheat yellow tones, all clearly NOT brown / "
            "NOT amber), a small precision GLASS BURETTE on a champagne-gold stand, a few "
            "FINE GLASS PIPETTES resting in a small champagne-gold tray, an OPEN HANDWRITTEN "
            "PERFUME FORMULA NOTEBOOK on cream paper (the calligraphy purposely soft / "
            "unreadable, NO actual readable text or logos, just the visual texture of "
            "elegant French perfumer handwriting), a bouquet of FRESH WHITE CAMELLIAS in a "
            "slim champagne-gold vase, and one ALDORE 'L'Heure Tranquille' Le Parfum bottle "
            "(the same frosted cream glass cylinder with champagne-gold cap and black "
            "grosgrain ribbon as the hero product) standing finished off to one side. "
            "Soft Parisian afternoon daylight pouring in from a tall arched French window "
            "off to the left, casting long warm directional light across the worktable. "
            "Magazine-grade couture perfumery atelier intimacy. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text or logos on the bottles, NO "
            "Pinterest UI icons. " + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, slightly elevated "
            "three-quarter angle on the worktable, the central glass apothecary bottles "
            "tack-sharp, very shallow depth of field with the rest softly blooming, "
            "~50mm look. " + EDITORIAL_TECH
        ),
    },
]

total = len(images)
for i, item in enumerate(images, 1):
    fname = item['path'].split('/')[-1]
    print(f"[{i}/{total}] {fname} 생성 중...")
    response = client.models.generate_content(
        model='gemini-3-pro-image-preview',
        contents=item['prompt'],
        config=types.GenerateContentConfig(
            response_modalities=['TEXT', 'IMAGE']
        )
    )
    saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(item['path'], 'wb') as f:
                f.write(part.inline_data.data)
            print(f"     ✓ 저장: {fname}")
            saved = True
            break
    if not saved:
        print(f"     ✗ 이미지 없음: {fname}")

print(f"\nFragrance {total}컷 생성 완료.")
