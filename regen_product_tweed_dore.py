from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/product/le_tweed_dore'

PERSONA = (
    "Model is a refined Korean K-drama-coded woman in her mid-to-late 20s, slim graceful figure, "
    "natural elegant beauty, full face visible and softly lit, a slick low chignon or smooth low "
    "ponytail, small 5-7mm pearl drop earrings (NOT chunky), serene confident expression. "
)

LOOK_SETTING = (
    "Setting: ALDORE Parisian maison private salon — soft cream walls with delicate Haussmannian "
    "wall mouldings, warm light-oak herringbone parquet, a tall arched French window with sheer "
    "ivory linen curtains glowing with soft afternoon daylight, a single gold-framed Parisian "
    "mirror suggested in the background, a small champagne-gold side table with a single white "
    "camellia bouquet partially visible. Clean, airy, magazine-grade luxury interior. "
)

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, soft pearl, "
    "with discreet black grosgrain accents only. Absolutely NO camel, NO cognac, NO brown, "
    "NO beige-brown, NO olive, NO khaki, NO burgundy, NO wine, NO red. "
)

JACKET_DESCRIPTION = (
    "She wears the ALDORE 'Le Tweed Doré' signature jacket: a STRUCTURED TAILORED CREAM BOUCLÉ "
    "TWEED BLAZER with subtle metallic CHAMPAGNE-GOLD FLECKS woven through (Le Fil Doré), single-"
    "breasted, fitted at the waist, sharp shoulder line. NOTCH LAPEL with fine BLACK GROSGRAIN "
    "trim along the lapel edge, front placket, pocket flaps, and cuffs. THREE sculpted CHAMPAGNE-"
    "GOLD signature buttons (camellia-engraved) down the front. Two flap pockets at the hip. "
    "Subtle gold filament fringe at the hem and sleeve cuffs (Le Fil Doré). "
)

TAILORING_RULE = (
    "STRICTLY structured tailored haute couture — Parisian tailoring at its finest, sharp "
    "shoulder line, defined waistline, clean precise lines. NOT loose, NOT casual, NOT "
    "loungewear, NOT pajamas. Sculptural and authoritative. "
)

PORTRAIT_TECH_3X4 = (
    "Camera: full-length editorial fashion portrait, vertical 3:4 portrait composition, ~50mm "
    "look, model centered or slightly off-center, eye-level, soft natural Parisian afternoon "
    "daylight, shallow depth of field, model tack-sharp, background softly blurred. "
    "Style: ALDORE SS27 lookbook editorial, Chanel haute-couture-coded heritage glamour, ultra "
    "realistic, subtle film grain, magazine-grade. "
    "Strictly: NO text, NO logos, NO signage, NO watermark, NO Pinterest UI icons, NO accessories "
    "beyond what is described. "
)

DETAIL_TECH_1X1 = (
    "Camera: SQUARE 1:1 macro composition, luxury detail still-life, ~85mm look, soft Parisian "
    "afternoon daylight from above-left, subtle directional shadow, very shallow depth of field "
    "with the hero detail tack-sharp. Background is soft warm cream-ivory bouclé tweed surface "
    "(unless described otherwise). "
    "Style: Chanel-coded couture detail editorial, ultra realistic, subtle film grain, "
    "magazine-grade. STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos, NO signage, "
    "NO watermark, NO Pinterest UI icons, NO sewing tools beyond what is described. "
)

ATELIER_TECH_16X9 = (
    "Camera: HORIZONTAL 16:9 cinematic landscape composition, intimate atelier scene, ~50mm "
    "look, soft warm Parisian afternoon daylight from above-left, shallow depth of field with "
    "the working hands and the garment tack-sharp, the rest softly defocused. "
    "Style: Chanel-coded couture atelier editorial — magazine-grade, ultra realistic, subtle "
    "film grain. STRICTLY: NO FACES, NO MODEL'S FACE, NO portraits — show ONLY the WORKING "
    "HANDS (and forearms in a white atelier coat or pristine white shirt sleeve) cropped tightly. "
    "NO text, NO logos, NO signage, NO watermark, NO Pinterest UI icons. "
)

images = [
    # ---------- HERO + GALLERY (model wearing) ----------
    {
        "path": f"{base}/hero_main.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: signature jacket PDP hero. "
            + PERSONA + JACKET_DESCRIPTION +
            "Underneath the jacket: a glimpse of an ivory silk shell camisole and a tone-on-tone "
            "cream silk pencil pant. A delicate single-strand pearl necklace, a single white "
            "camellia brooch on the lapel. Cream pointed-toe leather pumps. "
            "She stands in a confident editorial pose, three-quarter angle to camera, one hand "
            "lightly resting at the hip, the other relaxed at her side, weight on one leg, the "
            "jacket the clear hero of the frame. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
        ),
    },
    {
        "path": f"{base}/gallery_front.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: gallery view, FRONT. "
            + PERSONA + JACKET_DESCRIPTION +
            "Underneath: ivory silk shell + cream silk pencil pant. Cream pumps. "
            "She stands in a clean catalog pose facing CAMERA HEAD-ON (front view), arms "
            "relaxed at her sides, the entire jacket visible from collar to hip, the THREE "
            "champagne-gold buttons and BLACK GROSGRAIN front placket clearly readable. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
        ),
    },
    {
        "path": f"{base}/gallery_threequarter.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: gallery view, THREE-QUARTER. "
            + PERSONA + JACKET_DESCRIPTION +
            "Underneath: ivory silk shell + cream silk pencil pant. Cream pumps. "
            "She stands in a clean catalog pose at slight THREE-QUARTER ANGLE (showing both "
            "front placket and a hint of side seam), one hand resting in the front pocket flap, "
            "head turned slightly toward camera, the lapel and side panel of the jacket clearly "
            "readable. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
        ),
    },
    {
        "path": f"{base}/gallery_back.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: gallery view, BACK. "
            + PERSONA + JACKET_DESCRIPTION +
            "Underneath: ivory silk shell + cream silk pencil pant. Cream pumps. "
            "She stands FACING AWAY from camera (BACK VIEW), arms relaxed at her sides, the "
            "BACK of the structured tweed blazer visible — clean center back seam, sharp "
            "tailored shoulder line, fine BLACK GROSGRAIN trim along the back hem, subtle "
            "gold filament fringe at the hem. Her slick low chignon visible at the nape of "
            "the neck. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
        ),
    },

    # ---------- CLOTH MACRO (full-width hero) ----------
    {
        "path": f"{base}/cloth_macro.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: 'The Cloth Speaks' full-width hero macro. "
            "Hero subject: an EXTREME EDITORIAL MACRO close-up of a draped piece of CREAM IVOIRE "
            "BOUCLÉ TWEED FABRIC, the iconic LE TWEED DORÉ — soft cream wool bouclé loops, "
            "subtle nubby texture, with FINE METALLIC CHAMPAGNE-GOLD FILAMENT THREADS woven "
            "through the warp (Le Fil Doré) catching warm directional Parisian afternoon light. "
            "The fabric is softly draped with one organic fold running diagonally across the "
            "frame, the gold filaments tack-sharp and luminous against the matte cream wool. "
            "On the right edge of the composition, a sliver of FINE BLACK GROSGRAIN ribbon trim "
            "is visible, contrasting against the cream tweed (the maison's signature trim). "
            "Negative space at the center to allow editorial text overlay. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO mannequins, NO text, NO logos, NO "
            "watermark, NO Pinterest UI icons. Pure couture cloth still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 wide cinematic landscape composition, ~85mm macro look, "
            "very shallow depth of field, gold filaments tack-sharp, fabric softly modeled by "
            "warm directional sidelight from above-left. "
            "Style: Chanel-coded couture campaign cloth editorial, ultra realistic, subtle "
            "film grain, magazine-grade luxury hero macro."
        ),
    },

    # ---------- DETAIL MACROS (4 signature codes) ----------
    {
        "path": f"{base}/detail_button.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: signature CHAMPAGNE-GOLD CAMELLIA BUTTON "
            "macro. "
            "Hero subject: an EXTREME MACRO close-up of a SINGLE SCULPTED CHAMPAGNE-GOLD BUTTON "
            "engraved with the maison's CAMELLIA motif (a 5-petal flower carved in soft "
            "low-relief on the button face), hand-stitched onto the cream bouclé tweed front "
            "placket of the jacket. The metallic gold catches warm afternoon light, the button "
            "tack-sharp at center frame. Around the base of the button you can see the FINE "
            "GOLD HAND-STITCHING THREAD (Le Fil Doré) securing it with a delicate cross-stitch. "
            "A glimpse of FINE BLACK GROSGRAIN ribbon trim runs vertically along the placket "
            "edge to the side. "
            + PALETTE_RULES + DETAIL_TECH_1X1
        ),
    },
    {
        "path": f"{base}/detail_grosgrain.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: signature BLACK GROSGRAIN TRIM macro. "
            "Hero subject: an EXTREME MACRO close-up of a CUFF EDGE of the cream bouclé tweed "
            "jacket, where the FINE BLACK GROSGRAIN RIBBON TRIM runs precisely along the cuff "
            "border — the matte black ribbed grosgrain texture tack-sharp, contrasting "
            "luminously against the cream bouclé tweed. The grosgrain is hand-stitched in "
            "place with tiny invisible stitches. The tweed surface visible above shows subtle "
            "cream wool bouclé loops with a few CHAMPAGNE-GOLD FILAMENT threads catching light. "
            "A small glimpse of cream silk LINING is visible at the inside edge of the cuff. "
            + PALETTE_RULES + DETAIL_TECH_1X1
        ),
    },
    {
        "path": f"{base}/detail_filament.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: signature LE FIL DORÉ macro. "
            "Hero subject: an EXTREME MACRO close-up of the cream bouclé tweed weave itself, "
            "showing the maison's iconic LE FIL DORÉ — fine CHAMPAGNE-GOLD METALLIC FILAMENT "
            "THREADS WOVEN THROUGH the cream wool bouclé warp. The composition fills the frame "
            "with the textured weave: warm cream wool bouclé loops, occasional pristine ivory "
            "silk slubs, and the sparse luminous gold filaments running horizontally and "
            "vertically through the weave catching warm directional light. The texture is "
            "tack-sharp, you can almost feel the fabric. "
            + PALETTE_RULES + DETAIL_TECH_1X1
        ),
    },
    {
        "path": f"{base}/detail_fringe.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: signature LE FIL DORÉ FRINGE macro. "
            "Hero subject: an EXTREME MACRO close-up of the HEM EDGE of the cream bouclé tweed "
            "jacket, where a SUBTLE GOLD FILAMENT FRINGE — a fine, refined fringe of FINE "
            "CHAMPAGNE-GOLD METALLIC THREADS approximately 8-12mm long — runs along the bottom "
            "edge of the jacket. The fringe is delicate and editorial (NOT heavy, NOT bohemian "
            "— a refined Spring/Summer fringe). The cream bouclé tweed body sits above it, the "
            "fringe catching warm directional light, glowing luminously. A discreet line of "
            "FINE BLACK GROSGRAIN ribbon runs at the very top of the fringe attachment. "
            + PALETTE_RULES + DETAIL_TECH_1X1
        ),
    },

    # ---------- ATELIER (cropped hands) ----------
    {
        "path": f"{base}/atelier_button.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: 'Construction Atelier' scene I. "
            "Atelier scene: a couture seamstress's HANDS ONLY (cropped tightly at the wrists, "
            "in pristine WHITE atelier coat sleeves or rolled-up white silk shirt cuffs) are "
            "carefully HAND-STITCHING a single sculpted CHAMPAGNE-GOLD CAMELLIA BUTTON onto "
            "the cream bouclé tweed front placket. One hand holds the tweed fabric steady, the "
            "other holds a slim couture HAND SEWING NEEDLE threaded with FINE GOLD SILK THREAD "
            "(Le Fil Doré), passing it carefully through the button's shank. The work is "
            "intimate, precise. A small VINTAGE PIN CUSHION with a few sewing pins, a small "
            "champagne-gold thimble, and a few extra gold buttons rest on the cream worktable "
            "beside. "
            "Atelier worktable: smooth cream-ivory surface, soft Parisian afternoon daylight "
            "from a tall window off to the left. Magazine-grade couture atelier intimacy. "
            + PALETTE_RULES + ATELIER_TECH_16X9
        ),
    },
    {
        "path": f"{base}/atelier_stitching.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: 'Construction Atelier' scene II. "
            "Atelier scene: a couture seamstress's HANDS ONLY (cropped tightly at the wrists, "
            "in pristine WHITE atelier coat sleeves) are carefully HAND-STITCHING a length of "
            "FINE BLACK GROSGRAIN RIBBON TRIM onto the EDGE of the cream bouclé tweed jacket "
            "lapel. One hand holds the lapel and grosgrain ribbon precisely aligned, the other "
            "guides a slim couture sewing needle threaded with INVISIBLE CREAM-COLORED COTTON "
            "SILK THREAD, performing a tiny refined slip-stitch along the grosgrain edge. The "
            "stitching is meticulous, Parisian couture-grade. A spool of fine cream thread, a "
            "small spool of black grosgrain ribbon partially unwound, and a slim pair of "
            "champagne-gold-handled couture scissors rest beside on the cream worktable. "
            "Atelier worktable: smooth cream-ivory surface, soft Parisian afternoon daylight "
            "from a tall window off to the left. Magazine-grade couture atelier intimacy. "
            + PALETTE_RULES + ATELIER_TECH_16X9
        ),
    },

    # ---------- HOW TO WEAR (styling cross-references) ----------
    {
        "path": f"{base}/style_skirt.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: How to Wear I — with the matching "
            "Tailleur Doré pencil midi skirt (the full Tailleur look). "
            + PERSONA + JACKET_DESCRIPTION +
            "Bottom: a matching CREAM BOUCLÉ TWEED PENCIL MIDI SKIRT (same Le Tweed Doré fabric "
            "with subtle gold flecks), fitted at the natural waist, narrow through the hips, "
            "ending mid-calf with a fine BLACK GROSGRAIN trim at the hem and a discreet back "
            "vent. The full SUIT is in matching cream bouclé tweed. "
            "Inside the blazer: a glimpse of ivory silk shell camisole. A delicate single-"
            "strand pearl necklace. A single white camellia brooch at the lapel. Cream "
            "pointed-toe leather pumps. She stands in a confident editorial power pose, hands "
            "in pockets, feet shoulder-width apart, full-length visible. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
        ),
    },
    {
        "path": f"{base}/style_trouser.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré: How to Wear II — styled with cream silk "
            "tapered trousers for a softer Parisian-tailoring proposition. "
            + PERSONA + JACKET_DESCRIPTION +
            "Bottom: a pair of CREAM IVORY SILK TAPERED TROUSERS with a clean creased line, "
            "sharp tapered to the ankle, soft sheen. "
            "Inside the blazer: a glimpse of ivory silk shell camisole. Single strand of pearls, "
            "small pearl drop earrings. White camellia brooch on the lapel. Cream satin pointed-"
            "toe pumps barely peeking from the trouser hem. She stands in a graceful editorial "
            "pose, hand resting at her side, weight on one leg, full-length visible. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH_3X4
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

print(f"\nProduct Le Tweed Doré {total}컷 생성 완료.")
