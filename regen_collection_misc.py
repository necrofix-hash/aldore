from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection'

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, soft pearl, "
    "with discreet black grosgrain accents only. Absolutely NO camel, NO cognac, NO brown, "
    "NO beige-brown, NO olive, NO khaki, NO burgundy, NO wine, NO red, NO navy. "
)

PERSONA = (
    "Model is a refined Korean K-drama-coded woman in her mid-to-late 20s, slim graceful figure, "
    "natural elegant beauty, full face visible and softly lit, a slick low chignon or smooth low "
    "ponytail, small 5-7mm pearl drop earnings (NOT chunky), serene confident expression. "
)

images = [
    {
        "path": f"{base}/designer_note.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Designer's Note: Atelier Rue de Sèvres. "
            "An editorial still-life of the maison's couture atelier worktable in Paris 6e. "
            "Hero subject: a wide overhead-leaning view of a smooth cream-ivory atelier worktable, "
            "softly lit by Parisian afternoon daylight from a tall window off to the left. "
            "Arranged thoughtfully on the surface with negative space and editorial composition: "
            "1) A folded swatch of CREAM IVOIRE BOUCLÉ TWEED with subtle CHAMPAGNE-GOLD metallic "
            "flecks (Le Fil Doré weave). "
            "2) A pair of HAND-DRAWN COUTURE FASHION ILLUSTRATIONS on cream paper showing pencil "
            "sketches of a tweed jacket and a long evening gown — soft graphite lines, no text "
            "or logos, just elegant fashion croquis silhouettes. "
            "3) A small SPOOL of FINE GOLD SILK THREAD (the maison's signature Le Fil Doré). "
            "4) A spool of FINE BLACK GROSGRAIN ribbon partially unwound. "
            "5) A small pair of slim VINTAGE COUTURE SCISSORS in champagne-gold finish, resting "
            "diagonally. "
            "6) A single fresh WHITE CAMELLIA bloom set softly to the side — the maison's signature flower. "
            "7) A few loose IVORY-CREAM PEARLS scattered. "
            "8) A few sculpted CHAMPAGNE-GOLD camellia-engraved BUTTONS arranged in a small line. "
            "Soft directional Parisian afternoon light, gentle shadows, warm and contemplative mood, "
            "magazine-grade editorial atelier still-life, the kind that whispers 'the lining speaks "
            "before the cloth'. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO mannequins, NO text, NO logos, NO signage, "
            "NO watermark, NO sewing machine, NO clutter — refined editorial composition. "
            + PALETTE_RULES +
            "Camera: VERTICAL 3:4 portrait composition (the image will be displayed as a tall image "
            "panel beside the designer's note text), ~50mm look, slightly elevated three-quarter "
            "angle on the worktable, shallow depth of field with the camellia and the tweed "
            "swatch tack-sharp, the rest softly defocused. "
            "Style: Chanel-coded couture atelier editorial, ultra realistic, subtle film grain, "
            "magazine-grade luxury editorial."
        ),
    },
    {
        "path": f"{base}/film_thumb.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Collection Film: 'The Quiet Hour'. Cinematic film still. "
            + PERSONA +
            "Wide cinematic framing inside the ALDORE Parisian maison private salon at the BLUE "
            "HOUR (early evening) — soft cream walls with delicate Haussmannian wall mouldings, "
            "warm light-oak herringbone parquet, a tall arched French window glowing with cool "
            "DUSK-BLUE Parisian twilight outside, sheer ivory linen curtains diffusing the cool "
            "window light, a single warm GLOWING TABLE LAMP with a champagne-gold base on a "
            "console casting a warm halo across the room. "
            "MODEL POSITIONED ON THE LEFT THIRD of the frame (NOT center, NOT right) — she stands "
            "in a graceful slow-motion-cinematic pose near the tall arched window, slight three-"
            "quarter angle to camera, face softly turned toward the warm lamp, FULL-LENGTH visible. "
            "She wears a FLOOR-LENGTH IVORY SATIN COUTURE COLUMN GOWN with structured strapless "
            "sweetheart bustier bodice, fitted through the bust and waist, falling straight to the "
            "floor. Single-strand pearl necklace, pearl drop earrings, slick low chignon. "
            "STRICTLY structured haute couture eveningwear — NOT slip, NOT bias-cut, NOT spaghetti "
            "lingerie, NOT loungewear, NOT pajamas. "
            "RIGHT TWO-THIRDS of the frame is the salon interior — the warm lamp on a console, "
            "the parquet floor catching warm light, soft cream walls receding into atmospheric "
            "depth, the tall window letting cool dusk-blue light spill across. Compositional "
            "negative space at the right and center — the model is the only figure on the left. "
            "Cinematic dual-light contrast: cool dusk-blue from the window + warm gold from the "
            "lamp, mood is contemplative, slow, magic-hour. The image will be shown as a 16:9 "
            "cinematic film thumbnail with a subtle play button overlay at center — so the center "
            "should be calmer atmospheric salon space, NOT the model's face. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~35mm cinematic look, "
            "shallow-to-medium depth of field, model fully lit and tack-sharp on the left, salon "
            "softly modeled, subtle filmic grain, anamorphic feel. "
            "Style: Wong Kar-wai meets Sofia Coppola couture campaign film still, Chanel-coded "
            "haute-couture cinematic glamour, ultra realistic, magazine-grade. "
            "STRICTLY: NO text, NO logos, NO subtitles, NO play button (will be added in HTML), "
            "NO watermark, NO Pinterest UI icons."
        ),
    },
    {
        "path": f"{base}/closing.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Collection Closing: 'Un seul fil d'or' (a single golden "
            "thread). Editorial macro still-life. "
            "Hero subject: a sweeping wide horizontal view of a softly draped piece of CREAM "
            "IVOIRE SILK FABRIC laid across a smooth cream-ivory surface, gentle organic folds. "
            "Across the fabric, a SINGLE FINE GOLD SILK THREAD — perfectly straight, taut, "
            "horizontal — runs from edge to edge of the frame at roughly the lower-third line. "
            "The gold thread catches warm directional Parisian afternoon light, glowing luminously, "
            "tack-sharp, with a delicate cast micro-shadow on the silk beneath it. "
            "The composition is CALM AND MEDITATIVE with substantial NEGATIVE SPACE in the upper "
            "two-thirds and the center of the frame — soft cream silk receding into out-of-focus "
            "creaminess, no other props, no text, no clutter. The single gold thread is the only "
            "luminous accent against the entire cream-ivory composition. "
            "Mood: poetic, restrained, the maison's quiet signature. The image will be displayed "
            "as a hero banner with French and Korean text overlaid at center — so the CENTER OF "
            "THE FRAME must be calm soft-focus cream silk with no detail (allowing text overlay "
            "to read cleanly), and the gold thread placed at the lower-third line. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO mannequins, NO sewing tools, NO needles, "
            "NO text, NO logos, NO signage, NO watermark. Pure single-thread editorial composition. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 wide cinematic landscape composition, ~85mm macro look, "
            "very shallow depth of field — the gold thread along the lower-third line is "
            "tack-sharp, the silk fabric is luminously soft-focused around it, very subtle "
            "warm directional sidelight from above-left. "
            "Style: Chanel-coded couture campaign closing image, ultra realistic, subtle film "
            "grain, magazine-grade luxury minimalism, the kind of restrained image that closes "
            "a haute-couture lookbook."
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

print("\nCollection 미스셀 3컷 생성 완료.")
