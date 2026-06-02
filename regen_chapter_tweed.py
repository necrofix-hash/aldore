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

TWEED_RULE = (
    "STRICTLY structured tailored haute couture daywear — sharp, clean, sculptural Parisian "
    "tailoring. NOT loose, NOT drape-y, NOT casual, NOT loungewear, NOT pajamas. The tweed must "
    "read as ALDORE'S SIGNATURE FABRIC: cream ivoire bouclé tweed weave with SUBTLE METALLIC "
    "CHAMPAGNE-GOLD FLECKS woven through (Le Fil Doré, the maison's golden thread), fine BLACK "
    "GROSGRAIN trim along collar / lapel / cuffs / hem / pocket flaps, sculpted CHAMPAGNE-GOLD "
    "signature buttons with engraved camellia motif. "
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
        "path": f"{base}/look_w_01.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 09: Le Tweed Mini Suit. "
            + PERSONA +
            "She wears the iconic ALDORE TWO-PIECE TWEED SUIT in a youthful mini silhouette: a "
            "CROPPED CREAM BOUCLÉ TWEED JACKET with metallic champagne-gold flecks (Le Fil Doré) "
            "woven through, fine BLACK GROSGRAIN trim along the collarless rounded neckline, edges, "
            "cuffs, and pocket flaps, four sculpted CHAMPAGNE-GOLD signature buttons down the front "
            "(camellia-engraved), four small front patch pockets with gold-button accents. The jacket "
            "is fitted, structured, ending just at the waist. Underneath: a simple ivory silk camisole "
            "barely visible at the V. Below: a matching CREAM BOUCLÉ TWEED PLEATED MINI SKIRT with "
            "the same black grosgrain trim at the hem, clean knife pleats, sitting at the natural "
            "waist, ending mid-thigh. A single small fresh white camellia brooch pinned at the lapel. "
            "Single-strand pearl necklace. Cream leather slingback heels with black toe cap (the "
            "iconic Chanel-coded slingback silhouette). She stands in a graceful editorial pose, "
            "weight on one leg, hands relaxed. "
            + TWEED_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_w_02.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 10: The Sky Pearl Set. "
            + PERSONA +
            "She wears a TWO-PIECE TWEED SET in pale pearl-blue: a BOXY CROPPED PALE PEARL-BLUE "
            "BOUCLÉ TWEED JACKET with subtle metallic champagne-gold flecks woven through, fine "
            "BLACK GROSGRAIN trim along the rounded collarless neckline, edges, sleeve cuffs, and "
            "two flap pockets, four sculpted CHAMPAGNE-GOLD signature buttons down the front. The "
            "jacket has a clean structured silhouette, ending at the natural waist. Below: a "
            "CREAM IVORY SILK PLEATED MIDI SKIRT with fine accordion knife pleats, sitting at the "
            "natural waist, falling fluidly to mid-calf. The blue is a SOFT POWDERY PEARL-BLUE — "
            "never navy, never royal blue, never teal, never gray. White silk shell camisole "
            "barely visible inside the jacket V. A single white camellia brooch at the lapel. "
            "Pearl necklace, pearl drop earrings. Cream leather slingbacks with black toe cap. "
            "She stands in a poised three-quarter angle. "
            + TWEED_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_w_03.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 11: La Veste Camélia. "
            + PERSONA +
            "She wears a LONG CREAM BOUCLÉ TWEED JACKET / coat — the maison's elongated silhouette, "
            "single-breasted, ending at mid-thigh. Cream ivoire bouclé tweed with subtle metallic "
            "champagne-gold flecks (Le Fil Doré), fine BLACK GROSGRAIN trim along the lapel edge, "
            "front placket, cuffs, hem, and four flap pockets, six sculpted CHAMPAGNE-GOLD signature "
            "buttons down the front (camellia-engraved). Three small fresh WHITE CAMELLIA BROOCHES "
            "clustered together at the left lapel — the chapter's signature accent. Worn open over "
            "a CRISP WHITE SILK BUTTON-DOWN BLOUSE with a soft tie at the neck. Below: SLIM IVORY "
            "TAILORED TROUSERS with a clean creased line, ending at the ankle. Pearl necklace. "
            "Cream pointed-toe leather pumps. She stands in a confident editorial pose, slight "
            "hand in pocket. "
            + TWEED_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_w_04.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 12: Le Tweed Cape. "
            + PERSONA +
            "She wears a CREAM BOUCLÉ TWEED CAPE draped softly over both shoulders — the cape is "
            "structured but flowing, ending just below the hip, with a clean rounded shoulder line. "
            "Cream ivoire bouclé tweed with subtle metallic champagne-gold flecks (Le Fil Doré), "
            "fine BLACK GROSGRAIN trim along the entire perimeter (collar, front opening, hem), "
            "two sculpted CHAMPAGNE-GOLD signature buttons closing at the throat. A single white "
            "camellia brooch pinned at the right shoulder. Beneath: an IVORY SILK SHELL CAMISOLE "
            "TOP with a delicate scoop neckline, paired with SLIM IVORY HIGH-WAISTED TAILORED "
            "TROUSERS, sharply creased, ankle-length. A single strand of pearls. Cream pointed-toe "
            "leather pumps. She stands in a graceful editorial three-quarter pose, the cape gently "
            "swept by movement. "
            + TWEED_RULE + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/detail_w.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Tweed Doré detail still-life, editorial macro close-up. "
            "Hero subject: an EXTREME MACRO close-up of CREAM IVOIRE BOUCLÉ TWEED FABRIC with the "
            "maison's signature LE FIL DORÉ — a single THIN METALLIC CHAMPAGNE-GOLD THREAD woven "
            "delicately through the bouclé weave, catching warm afternoon light and glinting softly. "
            "The fabric texture (looped boucle yarn, soft cream tones, the gold filament running "
            "diagonally) must be tack-sharp and prominent. Beside the tweed: a single sculpted "
            "CHAMPAGNE-GOLD signature button (engraved with a small camellia motif), partially "
            "resting on the fabric. Beside it, a single fresh WHITE CAMELLIA bloom and a couture "
            "needle threaded with the same gold filament, gently placed on the tweed surface. "
            "NO PEOPLE, NO HANDS, NO MODEL — pure couture still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 LANDSCAPE composition, macro close-up product editorial framing, "
            "~85mm look, very shallow depth of field, the gold thread tack-sharp, the bouclé weave "
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

print("\nChapter Le Tweed Doré 5컷 생성 완료.")
