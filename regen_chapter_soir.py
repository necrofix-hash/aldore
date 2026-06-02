from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection'

PERSONA = (
    "Model is a refined Korean K-drama-coded woman in her mid-to-late 20s, slim graceful figure, "
    "natural elegant beauty, full face visible and softly lit, a slick low chignon or smooth low "
    "ponytail, small 5-7mm pearl drop earrings (NOT chunky), serene confident expression. "
)

EVENING_SETTING = (
    "Setting: ALDORE Parisian maison private salon at the BLUE HOUR (early evening) — soft cream "
    "walls with delicate Haussmannian wall mouldings, warm light-oak herringbone parquet, a tall "
    "arched French window glowing with soft DUSK-BLUE Parisian twilight outside, sheer ivory "
    "linen curtains diffusing the cool window light, a single warm GLOWING TABLE LAMP with a "
    "champagne-gold base on a console behind the model casting a soft warm halo (face must "
    "still be clearly and gracefully lit — NOT dark, NOT shadowed). The mood is evening, "
    "intimate, refined — NOT a dark cave. "
)

SOIR_PALETTE = (
    "Color palette for this evening chapter: deep BLACK silk / crepe / satin (the chapter's "
    "signature color), pure white silk, cream ivoire, ivory, champagne gold, soft pearl. "
    "Absolutely NO camel, NO cognac, NO brown, NO beige-brown, NO olive, NO khaki, NO burgundy, "
    "NO wine, NO red, NO navy. "
)

EVENING_RULE = (
    "STRICTLY structured haute couture eveningwear — sculptural bodice with defined waistline, "
    "STRUCTURED bra-cup or boned bodice, sharp lines. NOT loose, NOT bias-slip, NOT spaghetti-slip "
    "lingerie, NOT loungewear, NOT pajamas. Must read as red-carpet / opera / gala couture. "
)

PORTRAIT_TECH = (
    "Camera: full-length editorial fashion portrait, vertical 3:4 portrait composition, ~50mm look, "
    "model centered or slightly off-center, eye-level, soft layered evening light (cool dusk from "
    "the window + warm lamp halo from behind), shallow depth of field, model face tack-sharp and "
    "fully lit, background softly blurred. "
    "Style: ALDORE SS27 lookbook editorial, Chanel haute-couture-coded heritage glamour, ultra "
    "realistic, subtle film grain, magazine-grade. "
    "Strictly: NO text, NO logos, NO signage, NO watermark, NO accessories beyond what is described. "
)

images = [
    {
        "path": f"{base}/look_s_01.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 13: L'Heure Bleue. The signature little black dress. "
            + PERSONA +
            "She wears a couture BLACK SILK CREPE EVENING MINI DRESS — knee-length or just above the "
            "knee, with a clean STRUCTURED silhouette. Bateau (boat) NECKLINE sitting elegantly "
            "across the collarbone, FITTED bodice with delicate boning, defined natural waistline, "
            "and a structured A-LINE / straight skirt to the knee. Short cap sleeves of black silk "
            "crepe. The fabric: deep matte BLACK silk crepe with a refined drape, NOT shiny, NOT "
            "satin — true silk crepe. A single fine BLACK GROSGRAIN ribbon belt tied softly at the "
            "natural waist. A delicate single-strand pearl necklace, pearl drop earrings. Black "
            "satin pointed-toe pumps. She stands in a graceful editorial pose, weight on one leg, "
            "hands relaxed at her sides. "
            + EVENING_RULE + EVENING_SETTING + SOIR_PALETTE + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_s_02.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 14: La Robe Perle. The pearl-trimmed couture column. "
            + PERSONA +
            "She wears a FLOOR-LENGTH IVORY SATIN COUTURE COLUMN GOWN with hero pearl detailing. "
            "Silhouette: clean straight COLUMN cut, FITTED through the bust, waist, and hips, then "
            "falling straight to the floor with the slightest sweep — STRUCTURED, NOT bias-cut, "
            "NOT slip, NOT spaghetti loungewear. STRAPLESS STRUCTURED BUSTIER bodice with delicate "
            "internal boning and a SWEETHEART NECKLINE, the entire neckline ENCRUSTED with a "
            "luminous border of small ROUND PEARLS hand-stitched along the bust edge (the hero "
            "pearl trim — bold and sculptural). A second row of pearl trim runs down the center "
            "front of the bodice as a vertical pearl seam. Ivory satin with a soft sheen. A single "
            "double-strand pearl choker at the throat to echo the dress's pearl trim. Cream satin "
            "pointed-toe pumps barely peeking from the hem. She stands in a poised editorial pose, "
            "head turned slightly, one hand at her side. "
            + EVENING_RULE + EVENING_SETTING + SOIR_PALETTE + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_s_03.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 15: Le Tuxedo Noir. The maison's couture black tuxedo. "
            + PERSONA +
            "She wears a couture WOMEN'S TUXEDO entirely in BLACK: "
            "1) A BLACK WOOL TUXEDO JACKET, single-breasted, ONE black satin button closure at the "
            "natural waist, sharp tailored shoulder line, with prominent BLACK SILK SATIN SHAWL "
            "LAPEL (high-sheen satin against the matte wool body, the lapel is the hero detail). "
            "Slim sharply fitted silhouette. "
            "2) Matching BLACK WOOL TUXEDO TROUSERS with a clean sharp crease, ankle-length, with "
            "a SIGNATURE BLACK SATIN STRIPE running down the outer side seam of each leg (subtle "
            "high-sheen satin stripe against matte wool). "
            "Inside: a CRISP WHITE SILK BUTTON-DOWN SHIRT with a small wing collar, paired with a "
            "small BLACK SATIN BOW TIE knotted at the throat. Pearl drop earrings. Hair slicked "
            "tight into a low chignon. Black satin pointed-toe pumps. "
            "She stands in a sharp, confident editorial pose, hands relaxed at her sides, weight "
            "on one leg, the silhouette is sharp and Parisian gallery-coded — sculptural, "
            "masculine-feminine. "
            + EVENING_RULE + EVENING_SETTING + SOIR_PALETTE + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/look_s_04.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Look 16: La Robe Lumière du Soir. The light-clad gown. "
            + PERSONA +
            "She wears a luminous IVORY SEQUIN MIDI GOWN — densely covered all over with tiny "
            "round IVORY-CREAM PAILLETTES and silver bugle beads, the fabric shimmering and "
            "catching the evening light dramatically (the dress IS the light). Silhouette: short "
            "CAP SLEEVES of sheer ivory tulle with paillettes scattered across, a structured "
            "BATEAU NECKLINE, FITTED bodice with subtle internal boning, a defined natural "
            "waistline, then a soft SCULPTED A-LINE SKIRT falling to mid-calf with a slight "
            "sweep. The paillette work creates concentric scalloped shimmer patterns across the "
            "skirt. A delicate single-strand pearl necklace, pearl drop earrings. Cream satin "
            "pointed-toe pumps. She stands in a graceful editorial pose, full-length visible, "
            "the gown shimmering luminously. "
            + EVENING_RULE + EVENING_SETTING + SOIR_PALETTE + PORTRAIT_TECH
        ),
    },
    {
        "path": f"{base}/detail_s.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Soir detail still-life, editorial macro close-up. "
            "Hero subject: an EXTREME MACRO close-up of a piece of MATTE BLACK SILK CREPE FABRIC, "
            "smoothly draped, with a single PERFECTLY STRAIGHT HORIZONTAL ROW of TINY ROUND IVORY "
            "SEED PEARLS HAND-STITCHED across the surface — each pearl tack-sharp, the row uniform, "
            "the gold-toned hand-stitching thread visible at the base of each pearl. The seed "
            "pearls glow softly in warm directional light, catching the warm lamp light, contrasting "
            "luminously against the deep matte black silk crepe. Beside the pearls, a couture HAND "
            "SEWING NEEDLE threaded with FINE GOLD SILK THREAD rests diagonally on the fabric. A "
            "small CHAMPAGNE-GOLD thimble partially visible at the edge. "
            "NO PEOPLE, NO HANDS, NO MODEL — pure couture still-life. "
            + SOIR_PALETTE +
            "Camera: HORIZONTAL 4:3 LANDSCAPE composition, macro close-up product editorial framing, "
            "~85mm look, very shallow depth of field, the seed pearls tack-sharp, the silk crepe "
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

print("\nChapter Le Soir 5컷 생성 완료.")
