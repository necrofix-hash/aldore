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

COUTURE_RULE = (
    "STRICTLY couture eveningwear — STRUCTURED bodice with defined waistline, NOT loose, NOT "
    "drape-y, NOT slip-style, NOT knit, NOT jersey, NOT bouclé, NOT pajamas, NOT loungewear, "
    "NOT lingerie. Must read clearly as red-carpet / runway / haute couture formal dress. "
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
            "ALDORE Spring/Summer 2027 — Look 05: La Robe Perlée. "
            + PERSONA +
            "She wears a FLOOR-LENGTH IVORY COUTURE EVENING GOWN, densely embroidered all over with "
            "tiny pearls, crystals, and seed beads — the entire surface SHIMMERING with pearl beadwork. "
            "Silhouette: thin spaghetti straps, a STRAIGHT SQUARE NECKLINE across the décolletage, a "
            "FITTED beaded BODICE that hugs through the torso and hips, then a DROP-WAIST that releases "
            "into a gently FULL BEADED SKIRT cascading softly to the floor in a long silhouette. The "
            "silhouette is CLEARLY couture red-carpet — fitted through the body, voluminous from "
            "drop-waist down. A single strand of small pearls at the neck. Cream satin pointed-toe "
            "pumps barely peeking from the hem. "
            + COUTURE_RULE +
            "She stands in a graceful editorial pose, weight on one leg, hands relaxed at her sides. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_02.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 06: La Robe Camélia. "
            + PERSONA +
            "She wears a TEA-LENGTH (mid-calf) PURE WHITE COUTURE COCKTAIL DRESS densely covered all "
            "over with hundreds of small 3D fabric WHITE CAMELLIA BLOSSOMS appliquéd onto the surface "
            "(the maison's signature flower) — every petal pristine creamy white, giving the dress a "
            "rich textural floral relief. Silhouette: STRAPLESS with a STRAIGHT NEAT NECKLINE across "
            "the bust, FITTED structured bodice with delicate boning, a defined natural waistline, "
            "then a FULL A-LINE SKIRT that flares out gracefully to mid-calf. Soft tulle underlayer "
            "gives the skirt subtle volume. A delicate single strand of pearls at the throat. Cream "
            "leather slingback heels. The dress is CLEARLY a haute couture cocktail / runway look — "
            "structured, sculptural, formal. "
            + COUTURE_RULE +
            "She stands in a confident editorial pose, slight hand resting on the skirt. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_03.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 07: La Robe en Dentelle. "
            + PERSONA +
            "She wears a KNEE-SKIMMING IVORY CHANTILLY LACE COCKTAIL DRESS — exquisite cream chantilly "
            "lace overlay over ivory silk lining, delicate floral lace pattern visible throughout. "
            "Silhouette: BATEAU (boat) NECKLINE that sits gracefully across the collarbone, short cap "
            "sleeves of sheer scalloped lace, FITTED bodice through the torso, a defined natural "
            "waistline marked by a fine BLACK GROSGRAIN ribbon belt tied in a small bow at the side, "
            "then a structured A-LINE SKIRT to the knee. The lace edges are scalloped throughout. "
            "Pearl drop earrings, a single pearl bracelet. Cream leather ankle-strap kitten heels. "
            + COUTURE_RULE +
            "She stands in a poised three-quarter editorial pose. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_r_04.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 08: La Robe Bleu Perle. "
            + PERSONA +
            "She wears a FLOOR-LENGTH PALE PEARL-BLUE COUTURE SILK EVENING GOWN. Silhouette: a "
            "STRUCTURED HALTER NECKLINE that ties at the nape of the neck, FITTED beaded bodice "
            "embellished with delicate pearl and crystal beading at the neckline cascading down the "
            "torso, a defined natural waistline, then a SLIM COLUMN SKIRT in fluid pale pearl-blue "
            "silk that drapes elegantly to the floor with the faintest sweep at the hem. The blue is "
            "a SOFT POWDERY PEARL-BLUE — never navy, never royal blue, never teal, never gray. A "
            "single strand of small pearls at the throat. Cream satin pointed-toe pumps barely "
            "peeking from the hem. "
            + COUTURE_RULE +
            "She stands in a poised editorial pose, three-quarter angle, head turned slightly. "
            + LOOK_SETTING + PALETTE_RULES + PORTRAIT_TECH
        ),
    },
]

total = len(images)
for i, item in enumerate(images, 1):
    fname = item['path'].split('/')[-1]
    print(f"[{i}/{total}] {fname} 재생성 중...")
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

print("\nChapter La Robe v2 (couture eveningwear) 4컷 재생성 완료.")
