from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/journal'

PERSONA = (
    "Model is a refined Korean K-drama-coded woman in her mid-to-late 20s, slim graceful figure, "
    "natural elegant beauty, full face visible and softly lit, a slick low chignon or smooth low "
    "ponytail, small 5-7mm pearl drop earrings (NOT chunky), serene confident expression. "
)

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, soft pearl, "
    "with discreet black grosgrain accents only where described. Absolutely NO camel, NO "
    "cognac, NO brown, NO beige-brown, NO olive, NO khaki, NO burgundy, NO wine, NO red, "
    "NO navy. "
)

EDITORIAL_TECH = (
    "Style: ALDORE Journal magazine editorial, Chanel haute-couture-coded heritage glamour "
    "meets quiet contemplative Parisian editorial. Ultra realistic, subtle film grain, "
    "magazine-grade. STRICTLY: NO text, NO logos, NO signage, NO watermark, NO Pinterest "
    "UI icons. "
)

VINTAGE_SEPIA_RULE = (
    "Style: ARCHIVAL VINTAGE SEPIA-TONED photograph from a 1940s couture archive — "
    "slightly faded, archival quality, subtle film grain, soft cinematic contrast, warm "
    "sepia tones. NO modern color saturation. "
)

images = [
    # ---------- 1. HERO — magazine cover-style ----------
    {
        "path": f"{base}/journal_hero.jpg",
        "prompt": (
            "ALDORE Journal — Issue No. 14, 'L'Heure Tranquille', Spring/Summer 2027 cover image. "
            "Editorial cinematic wide-frame for the magazine cover. "
            + PERSONA +
            "She wears the maison's signature CREAM BOUCLÉ TWEED JACKET with subtle metallic "
            "champagne-gold filaments woven through (Le Tweed Doré), with FINE BLACK GROSGRAIN "
            "TRIM along the lapel and three sculpted CHAMPAGNE-GOLD CAMELLIA BUTTONS down the "
            "front. A glimpse of an ivory silk shell underneath. A small white camellia brooch "
            "on the lapel, single-strand pearl necklace, pearl drop earrings, slick low chignon. "
            "She is positioned on the LEFT THIRD of the frame, three-quarter angle to camera, "
            "looking softly off-frame toward the upper-right with a contemplative expression, "
            "ONE HAND raised to chest level holding a single fresh WHITE CAMELLIA bloom near "
            "her collarbone, the other relaxed at her side. The image is SHOULDER-UP TO MID-"
            "TORSO framing (a cover-coded portrait). "
            "Setting behind her: the ALDORE Parisian maison private salon — soft cream Haussmannian "
            "wall mouldings, a sliver of a tall arched French window letting in soft Parisian "
            "afternoon daylight, the warm golden glow of the salon receding into atmospheric "
            "depth. The right two-thirds of the frame is intentionally calmer (negative space "
            "for the cover masthead and headline overlay). "
            + PALETTE_RULES + EDITORIAL_TECH +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition (the magazine cover is "
            "displayed as a wide hero), ~85mm portrait lens, shallow depth of field with the "
            "model and camellia tack-sharp, the salon softly modeled behind. Subtle filmic grain."
        ),
    },

    # ---------- 2. FEATURED STORY — Le Geste Doré (atelier scene) ----------
    {
        "path": f"{base}/journal_featured.jpg",
        "prompt": (
            "ALDORE Journal — Featured Story: 'Le Geste Doré' (The Gold Gesture). A wide "
            "atmospheric editorial documentary moment inside the Atelier Rue de Sèvres. "
            "FOREGROUND (lower-right of frame, tack-sharp): a couture seamstress's HANDS ONLY "
            "(cropped tightly at the wrists in pristine WHITE atelier coat sleeves) hand-"
            "stitching a sculpted CHAMPAGNE-GOLD CAMELLIA BUTTON onto the cream bouclé tweed "
            "front placket of a jacket-in-progress. The hands are in slow, precise motion "
            "with a slim couture sewing needle threaded with FINE GOLD SILK THREAD. "
            "MIDGROUND (softly defocused): a couture worktable with the rest of the cream "
            "tweed jacket spread out, a small spool of black grosgrain ribbon, a pair of "
            "champagne-gold-handled couture scissors, a small pin cushion, and a single white "
            "CAMELLIA bloom resting at the edge of the table. "
            "BACKGROUND (deeper out-of-focus): the wider atelier interior — cream Haussmannian "
            "walls, a tall arched French window letting in soft afternoon daylight, the silhouette "
            "of an antique couture dress form with another tweed jacket draped on it, soft "
            "atmospheric depth. "
            "The mood: documentary, intimate, the maison at work — the kind of editorial moment "
            "a fashion magazine would publish to show 'the gold gesture' that defines the maison. "
            "NO FACES, NO MODEL'S FACE — only the working hands cropped tightly. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~50mm look, shallow "
            "depth of field with hands in tack-sharp focus at lower-right, the rest softly "
            "blooming. Subtle directional warm afternoon light from above-left. " + EDITORIAL_TECH
        ),
    },

    # ---------- 3. CARD: Behind the Seams (atelier overhead worktable) ----------
    {
        "path": f"{base}/journal_card_atelier.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'Behind the Seams'. "
            "An EDITORIAL OVERHEAD-LEANING still-life of a couture worktable in the maison's "
            "Atelier Rue de Sèvres: a smooth cream-ivory worktable with TWO HAND-DRAWN COUTURE "
            "FASHION CROQUIS on cream paper (pencil sketches of a tweed jacket and a long "
            "evening gown with a peplum waist, classic 1948-coded silhouettes — purely visual, "
            "NO readable text or logos), a folded swatch of CREAM BOUCLÉ TWEED with subtle "
            "champagne-gold flecks, a small spool of FINE GOLD SILK THREAD, a partially "
            "unwound spool of fine BLACK GROSGRAIN ribbon, a pair of slim CHAMPAGNE-GOLD "
            "couture scissors resting diagonally, a small pin cushion with vintage couture "
            "pins, and a few sculpted CHAMPAGNE-GOLD CAMELLIA BUTTONS arranged in a small "
            "neat line. "
            "Soft Parisian afternoon daylight from a tall window off to the left, gentle "
            "directional shadows, warm contemplative mood. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO mannequins, NO readable text, NO "
            "logos. Pure editorial atelier still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, slightly elevated three-quarter "
            "overhead angle, the croquis sketches tack-sharp at center frame, very shallow "
            "depth of field on the surrounding objects, ~50mm look. " + EDITORIAL_TECH
        ),
    },

    # ---------- 4. CARD: From the 1948 Archives (vintage letter still-life) ----------
    {
        "path": f"{base}/journal_card_archive.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'From the 1948 Archives'. "
            "A VINTAGE ARCHIVAL EDITORIAL still-life: an aged 1948 HANDWRITTEN LETTER on "
            "cream-ivory paper laid open on a smooth cream table surface, the elegant 1940s "
            "French calligraphy gracefully visible but PURELY ILLEGIBLE / unreadable (just "
            "the visual texture of vintage script, NO actual readable text). The letter has a "
            "vintage sepia-aged tone, slightly yellowed at the edges. "
            "Beside the letter: an aged 1948 ENVELOPE addressed in calligraphy (also "
            "unreadable), an ARCHIVAL VINTAGE SEPIA PHOTOGRAPH (small, 4×6cm, showing only "
            "an out-of-focus glimpse of an atelier interior — NO face visible), a small "
            "vintage couture wax seal stamp in champagne-gold metal, a glimpse of CREAM "
            "BOUCLÉ TWEED swatch, a single dried WHITE CAMELLIA bloom (preserved). "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO readable text or logos. Pure vintage "
            "archive editorial still-life. "
            + VINTAGE_SEPIA_RULE +
            "Camera: HORIZONTAL 4:3 landscape composition, slightly elevated three-quarter "
            "overhead angle, the vintage letter and photograph tack-sharp at center, very "
            "shallow depth of field, soft directional warm light. " + EDITORIAL_TECH
        ),
    },

    # ---------- 5. CARD: A Walk in the 6e (Paris exterior) ----------
    {
        "path": f"{base}/journal_card_paris.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'A Walk in the 6e'. "
            "An EDITORIAL EXTERIOR PARIS 6e arrondissement street scene at golden hour: a "
            "graceful HAUSSMANNIAN FACADE — CREAM-IVORY LIMESTONE building with classic "
            "ornate Parisian wrought-iron balcony railings on the upper floors, tall arched "
            "French windows with sheer ivory linen curtains visible, a polished BRASS DOOR "
            "PLAQUE beside a discreet wooden double door (the brass plaque visible but its "
            "engraved text purposely soft / unreadable, NO actual readable text or logos). "
            "A SINGLE tall planter of WHITE CAMELLIAS sits beside the door, lit by warm "
            "late-afternoon sunlight raking across the limestone. The cobblestone sidewalk "
            "in the foreground is soft cream-grey, polished by years of footsteps. "
            "NO PEOPLE, NO modern cars, NO modern signage — pure timeless 6e arrondissement "
            "atmosphere. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~35mm slightly wide architectural "
            "framing, slight three-quarter angle on the facade showing both the door and a "
            "slice of the street, eye-level, sharp focus on the door and camellias, soft "
            "atmospheric depth on the building rising up. " + EDITORIAL_TECH
        ),
    },

    # ---------- 6. CARD: The White Camellia (flower macro) ----------
    {
        "path": f"{base}/journal_card_camellia.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'La Camélia Blanche — A Maison Story'. "
            "An EDITORIAL MACRO STILL-LIFE of fresh WHITE CAMELLIAS: three ivory-white camellia "
            "blooms with multiple layered pristine creamy-white petals arranged in a perfect "
            "spiral, freshly cut and resting on a smooth CHAMPAGNE-GOLD ROUND TRAY, with a few "
            "loose camellia petals scattered around them. The petals are tack-sharp, dewy and "
            "luminous in soft Parisian morning daylight, pearl-white catching gentle directional "
            "light from above-left. "
            "On the side of the tray: a single FINE BLACK GROSGRAIN RIBBON tied loosely around "
            "one of the camellia stems (the maison's signature touch). The cream-ivory "
            "background surface is softly out of focus. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos. Pure flower still-"
            "life editorial. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~85mm macro look, slight three-"
            "quarter overhead angle, very shallow depth of field with the central camellia "
            "tack-sharp, soft directional morning light. " + EDITORIAL_TECH
        ),
    },

    # ---------- 7. CARD: The Quiet Hour Film ----------
    {
        "path": f"{base}/journal_card_film.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'The Making of The Quiet Hour Film'. "
            + PERSONA +
            "Atmospheric BLUE HOUR cinematic film still — she wears a STRUCTURED IVORY "
            "SATIN COUTURE COLUMN GOWN (strapless sweetheart bustier, fitted through bust and "
            "waist, falling straight to floor — NOT slip, NOT bias-cut). Single-strand pearl "
            "necklace, pearl drop earrings, slick low chignon. "
            "She stands in profile near a tall arched French window of the maison's salon at "
            "BLUE HOUR (early evening) — soft cool DUSK-BLUE Parisian twilight outside diffused "
            "by sheer ivory linen curtains, a single warm GLOWING CHAMPAGNE-GOLD TABLE LAMP on "
            "a console behind her casting a warm halo. Her face is softly lit by the dual cool-"
            "and-warm light, fully visible in profile or slight three-quarter, with a "
            "contemplative expression. The salon recedes into deep cinematic atmosphere. "
            "The mood: a film still from a slow couture campaign film. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~50mm cinematic look, shallow "
            "depth of field with model tack-sharp and fully lit, salon softly modeled, "
            "subtle filmic anamorphic feel. " + EDITORIAL_TECH
        ),
    },

    # ---------- 8. CARD: Interview — Première d'Atelier (cropped hands sewing detail) ----------
    {
        "path": f"{base}/journal_card_interview.jpg",
        "prompt": (
            "ALDORE Journal — article thumbnail: 'Interview: Madame the Première d'Atelier'. "
            "An EDITORIAL DOCUMENTARY close-up of a couture seamstress's HANDS ONLY (cropped "
            "tightly at the wrists in pristine WHITE atelier coat sleeves) carefully HAND-"
            "BASTING a row of small ROUND IVORY SEED PEARLS along the bust edge of a "
            "structured ivory satin couture bustier bodice (not a slip — clearly a structured "
            "couture bodice with internal boning visible at the seam). One hand holds the "
            "bodice steady, the other guides a slim couture sewing needle threaded with FINE "
            "GOLD SILK THREAD, securing each tiny pearl with a delicate stitch. The pearls "
            "glow softly, the satin catches gentle light. "
            "Atelier worktable surface visible: cream-ivory, with a small spool of fine cream "
            "thread and a small box of seed pearls. "
            "Soft Parisian afternoon daylight from above-left, intimate magazine-grade "
            "atelier moment. "
            "NO FACES, NO MODEL'S FACE — only the working hands. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~85mm look, very shallow depth "
            "of field with hands and pearls tack-sharp, intimate framing. " + EDITORIAL_TECH
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

print(f"\nJournal {total}컷 생성 완료.")
