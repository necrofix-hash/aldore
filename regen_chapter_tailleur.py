from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection'

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

TAILORING_RULE = (
    "STRICTLY structured tailored haute couture daywear / eveningwear — Parisian tailoring at its "
    "finest, sharp shoulder line, defined waistline, clean precise lines. NOT loose, NOT casual, "
    "NOT loungewear, NOT pajamas. Sculptural and authoritative. "
)

PORTRAIT_TECH = (
    "Camera: full-length editorial fashion portrait, vertical 3:4 portrait composition, ~50mm look, "
    "model centered or slightly off-center, eye-level, soft natural Parisian afternoon daylight, "
    "shallow depth of field, model tack-sharp, background softly blurred. "
    "Style: ALDORE SS27 lookbook editorial, Chanel haute-couture-coded heritage glamour, ultra "
    "realistic, subtle film grain, magazine-grade. "
    "Strictly: NO text, NO logos, NO signage, NO watermark, NO accessories beyond what is described. "
)

images = [
    {
        "path": f"{base}/look_t_01.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 01: Le Tailleur Doré. The maison's flagship power suit. "
            + PERSONA +
            "She wears a CREAM BOUCLÉ TWEED POWER SUIT — TWO PIECES: "
            "1) A STRUCTURED TAILORED CREAM BOUCLÉ TWEED BLAZER with subtle metallic CHAMPAGNE-GOLD "
            "FLECKS woven through (Le Fil Doré). Single-breasted, fitted at the waist, sharp "
            "shoulder line, NOTCH LAPEL with fine BLACK GROSGRAIN trim along the lapel edge, "
            "front placket, pocket flaps, and cuffs. THREE sculpted CHAMPAGNE-GOLD signature "
            "buttons (camellia-engraved) down the front. Two flap pockets at the hip. "
            "2) A matching CREAM BOUCLÉ TWEED PENCIL MIDI SKIRT, fitted at the natural waist, "
            "narrow through the hips, ending mid-calf with a fine BLACK GROSGRAIN trim at the hem "
            "and a discreet back vent. "
            "Inside the blazer: a glimpse of ivory silk shell camisole. A delicate single-strand "
            "pearl necklace. A single white camellia brooch at the lapel. Cream pointed-toe "
            "leather pumps. She stands in a confident editorial power pose, hands in pockets, "
            "feet shoulder-width. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_t_02.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 02: Le Tailleur Bouclé. "
            + PERSONA +
            "She wears a youthful structured TWEED SUIT with prominent BLACK GROSGRAIN TRIM detailing: "
            "1) A FITTED STRUCTURED CREAM BOUCLÉ TWEED JACKET with bold contrasting BLACK GROSGRAIN "
            "borders along EVERY edge — the rounded collarless neckline, the front placket, all "
            "four pocket flaps, the cuffs, and the hem — the black grosgrain reads strongly against "
            "the cream tweed. Four sculpted CHAMPAGNE-GOLD signature buttons. "
            "2) A matching CREAM BOUCLÉ TWEED MIDI SKIRT, A-line silhouette, sitting at the "
            "natural waist, ending at mid-calf, BLACK GROSGRAIN border running along the hem. "
            "HERO ACCESSORY: a CREAM BOUCLÉ TWEED BUCKET HAT (also trimmed with a fine BLACK "
            "GROSGRAIN band around the brim base) tilted slightly forward — clean tailored "
            "couture bucket hat shape, NOT slouchy. Hair: smooth low chignon at the nape so "
            "the hat sits cleanly. "
            "A small white camellia brooch at the lapel. Pearl drop earrings. Cream slingback "
            "heels with black toe cap. She stands in a poised editorial pose, slight three-quarter "
            "angle. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_t_03.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 03: Le Tailleur Crème. A fluid silk tailoring proposition. "
            + PERSONA +
            "She wears a SILK SATIN TAILORED ENSEMBLE — entirely in cream ivoire silk, NOT tweed: "
            "1) A CREAM IVORY SILK SATIN BLAZER with a soft sheen, single-breasted, FITTED at the "
            "waist with a self-tie sash belt, soft tailored shoulder, PEAK LAPEL in matching silk "
            "satin, ONE sculpted CHAMPAGNE-GOLD button at the closure. The lapel and front edge "
            "trimmed with a fine BLACK GROSGRAIN piping. "
            "2) Matching CREAM IVORY SILK TAPERED TROUSERS with a clean creased line, sharp "
            "tapered to the ankle. "
            "Inside the blazer: an ivory silk shell camisole or just a deep décolletage glimpse, "
            "no shirt visible. A single small white camellia brooch on the lapel. Single strand "
            "of pearls. Cream satin pointed-toe pumps. She stands in a graceful editorial pose, "
            "hand resting at her side, head slightly tilted. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_t_04.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 04: Le Smoking Ivoire. The maison's couture tuxedo for women. "
            + PERSONA +
            "She wears a couture WOMEN'S TUXEDO (Le Smoking) entirely in IVORY: "
            "1) An IVORY WOOL SMOKING JACKET, single-breasted, ONE sculpted CHAMPAGNE-GOLD button "
            "closure at the natural waist, sharp tailored shoulder, with prominent IVORY SILK "
            "SATIN SHAWL LAPEL (high contrast satin sheen against the matte wool body). Slim, "
            "sharply fitted silhouette. "
            "2) Matching IVORY WOOL TUXEDO TROUSERS with a clean sharp crease, hitting the ankle, "
            "and with a SIGNATURE BLACK GROSGRAIN STRIPE running down the outer side seam of each "
            "leg (the iconic tuxedo stripe — but in BLACK grosgrain ribbon, like a couture detail). "
            "Inside: a white silk shirt with no collar, OR an open neckline showing collarbone. "
            "A small black grosgrain ribbon bow at the throat (like a tuxedo bow tie, refined). "
            "Pearl stud earrings. Hair slicked back into a tight low chignon. Black satin "
            "pointed-toe pumps (the only black footwear in the collection — for the smoking only). "
            "She stands in a sharp editorial pose, hands relaxed, weight on one leg, the silhouette "
            "is sharp, masculine-feminine, Parisian gallery-coded. "
            + TAILORING_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/detail_t.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tailleur detail still-life, editorial macro close-up. "
            "Hero subject: an EXTREME MACRO close-up of a row of FOUR SCULPTED CHAMPAGNE-GOLD "
            "SIGNATURE BUTTONS, each engraved with a small camellia motif, hand-stitched onto a "
            "front placket of CREAM IVOIRE BOUCLÉ TWEED. The metallic gold buttons gleam softly "
            "with warm afternoon light, each one is in tack-sharp focus. Around the base of each "
            "button, you can clearly see the FINE GOLD HAND-STITCHING THREAD — the maison's "
            "signature LE FIL DORÉ — securing the button with a delicate cross-stitch pattern. "
            "Beside the buttons, a strip of FINE BLACK GROSGRAIN ribbon lies along the placket "
            "edge. A couture HAND SEWING NEEDLE, threaded with the same gold filament, rests "
            "diagonally across the tweed. "
            "NO PEOPLE, NO HANDS, NO MODEL — pure couture still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 LANDSCAPE composition, macro close-up product editorial framing, "
            "~85mm look, very shallow depth of field, the gold buttons tack-sharp, the bouclé weave "
            "softly modeled by warm directional sidelight from above-left. "
            "Style: Chanel-coded couture detail editorial, ultra realistic, subtle film grain, "
            "magazine-grade. NO text, NO logos, NO watermark."
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

print("\nChapter Le Tailleur 5컷 생성 완료.")
