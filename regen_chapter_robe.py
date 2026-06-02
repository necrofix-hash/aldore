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
        "path": f"{base}/look_r_01.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 05: The Pearl Knit Dress. "
            + PERSONA +
            "She wears an exquisite WHITE ribbed knit MIDI DRESS with a fine BLACK GROSGRAIN trim along "
            "the rounded neckline and along the front placket, fastened with a vertical row of small "
            "PEARL BUTTONS (champagne-gold settings). Slim, refined silhouette, knee-skimming midi "
            "length. Cream slingback heels (NOT brown). A delicate single-strand pearl necklace. "
            "She stands in a graceful neutral pose, weight on one leg, hands relaxed. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_02.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 06: La Robe Camélia. "
            + PERSONA +
            "She wears a SOFT ROSE PINK-BEIGE bouclé tweed RUFFLED MINI DRESS — short hem with delicate "
            "tiered ruffles, fitted bodice, BLACK GROSGRAIN trim along the round neckline and short "
            "cap sleeves, three SCULPTED CHAMPAGNE-GOLD buttons down the bodice. A single fresh "
            "WHITE CAMELLIA bloom pinned at the lapel/shoulder as a brooch. Cream leather slingback "
            "heels (NOT brown). The pink is a SOFT POWDERY ROSE — never red, never coral, never burgundy. "
            "She stands in a confident editorial pose, slight hand on hip. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_03.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 07: La Robe Lumière. "
            + PERSONA +
            "She wears a luminous IVORY SILK BIAS-CUT SLIP MIDI DRESS — fluid, liquid silk, thin "
            "spaghetti straps, V-neckline, the bias-cut hem grazing mid-calf with a soft drape. "
            "A single small white camellia clipped above the ear, a strand of pearls. Cream silk "
            "ankle-strap kitten heels. She is in mid-stride, the silk catching the light, walking "
            "gently across the salon — a frozen moment of soft motion. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_04.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 08: La Robe Plissée Bleue. "
            + PERSONA +
            "She wears a PALE PEARL-BLUE PLISSÉ MIDI DRESS — finely pleated lightweight silk, slim "
            "shoulder straps, cinched at the waist, falling in delicate pleats to mid-calf. Layered "
            "over the shoulders is a cropped CREAM PEARL bouclé tweed jacket with BLACK GROSGRAIN "
            "trim and CHAMPAGNE-GOLD sculpted buttons (the iconic ALDORE Tweed). A single-strand "
            "pearl necklace. Cream leather slingback kitten heels. The blue is a SOFT POWDERY "
            "PEARL-BLUE — never navy, never royal blue, never teal, never gray. "
            "She stands in a poised three-quarter angle. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/detail_r.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — La Robe detail still-life, editorial macro close-up. "
            "Hero subject: the delicate BIAS-CUT IVORY SILK HEM of a slip midi dress, draped softly "
            "against a warm light-oak herringbone parquet floor — the silk catches a beam of soft "
            "afternoon Parisian daylight, glowing luminous and liquid. Resting at the hem on the "
            "silk: a single fresh WHITE CAMELLIA pin set in CHAMPAGNE-GOLD (small couture brooch), "
            "the camellia petals pristine and creamy white. Beside it, a thin strand of pearls "
            "casually arranged. "
            "NO PEOPLE, NO MODEL, NO HANDS — pure still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 LANDSCAPE composition, macro close-up product editorial framing, "
            "~85mm look, very shallow depth of field, the camellia pin tack-sharp, silk and parquet "
            "softly blurred at the edges. Soft warm directional sidelight from above-left. "
            "Style: Chanel-coded couture detail editorial, ultra realistic, subtle film grain, "
            "magazine-grade. NO text, NO logos, NO watermark, NO sewing tools."
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

print("\nChapter La Robe 5컷 생성 완료.")
