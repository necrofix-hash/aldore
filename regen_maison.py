from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/maison'

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, soft pearl, "
    "warm wood (light oak / honeyed parquet, NOT dark walnut), with discreet black grosgrain "
    "accents only where described. Absolutely NO camel, NO cognac, NO brown leather, NO "
    "beige-brown, NO olive, NO khaki, NO burgundy, NO wine, NO red, NO navy. "
)

VINTAGE_BW_RULE = (
    "Style: ARCHIVAL VINTAGE BLACK-AND-WHITE silver gelatin photograph, 1948 Vogue Paris "
    "editorial portrait coded by Cecil Beaton / Erwin Blumenfeld, the kind of refined Parisian "
    "couture portrait the maison would archive. Subtle film grain, soft cinematic contrast, "
    "the highlights luminous, the shadows deep but never crushed. The image must read as a "
    "GENUINE 1948 silver gelatin photograph — slightly aged, archival quality. NO modern "
    "color, NO color grading — fully monochrome BLACK AND WHITE. "
)

VINTAGE_SEPIA_RULE = (
    "Style: ARCHIVAL VINTAGE SEPIA-TONED silver gelatin photograph from the 1940s-1950s "
    "couture archive, slightly faded, archival quality, subtle film grain, soft cinematic "
    "contrast, warm sepia tones. NO modern color saturation — vintage aged sepia only. "
)

CONTEMPORARY_TECH = (
    "Camera: ~50mm look, soft natural Parisian afternoon daylight, shallow-to-medium depth "
    "of field, magazine-grade luxury interior editorial. Style: Chanel-coded couture maison "
    "interior, ultra realistic, subtle film grain, magazine-grade. STRICTLY: NO text, NO "
    "logos, NO signage, NO watermark, NO Pinterest UI icons. "
)

images = [
    # ---------- 1. HERO — atelier salon at golden hour ----------
    {
        "path": f"{base}/maison_hero.jpg",
        "prompt": (
            "ALDORE Maison — Atelier Rue de Sèvres, the founding salon. "
            "Editorial wide cinematic interior of the ALDORE Parisian maison private SALON at "
            "GOLDEN HOUR (late afternoon, the warm raking sunlight pouring in from the tall "
            "arched French windows on the left, painting long warm golden light across the "
            "herringbone parquet floor). "
            "The salon: soft cream walls with delicate Haussmannian wall mouldings (panels and "
            "dado rails), polished light-oak HERRINGBONE parquet glowing warm honey-gold in the "
            "raking light, two tall arched French windows on the LEFT with sheer ivory linen "
            "curtains diffusing the golden light, a tall vintage GOLD-FRAMED ROCOCO MIRROR on "
            "the back wall, a small champagne-gold console table with a large bouquet of WHITE "
            "CAMELLIAS in a champagne-gold vase, a SINGLE EMPTY SCULPTED LOUIS XVI ARMCHAIR "
            "upholstered in cream silk standing thoughtfully off-center toward the right (as if "
            "Élise herself just stepped away), an antique couture dress form draped with a "
            "single piece of cream bouclé tweed in the background depth. "
            "The mood: contemplative, hushed, the maison at its quietest hour — narrative, "
            "unmistakably 1948 Paris. NO PEOPLE, NO MODELS — pure atmospheric salon. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~35mm wide-ish look, "
            "shallow-to-medium depth of field, the empty armchair tack-sharp, the windows "
            "softly bloomed with golden light, deep cinematic atmosphere with substantial "
            "negative space for text overlay. " + CONTEMPORARY_TECH
        ),
    },

    # ---------- 2. FOUNDER — vintage 1948 portrait of Élise Aldore ----------
    {
        "path": f"{base}/maison_founder.jpg",
        "prompt": (
            "ALDORE Maison — Élise Aldore, the maison's founder, as captured in 1948 at age 27. "
            "An ARCHIVAL VINTAGE 1948 VOGUE PARIS-CODED PORTRAIT photograph of a refined young "
            "KOREAN-CODED woman in her late 20s with the K-drama-coded refinement of a 1940s "
            "Vogue Paris cover model. Full face visible, gracefully lit, serene confident "
            "expression, slim graceful figure. Hair: a smooth low CHIGNON pinned at the nape "
            "with a single small camellia tucked at the side (1948 Parisian couture coiffure). "
            "She wears: a 1948-CODED CRISP IVORY-WHITE SILK BLOUSE with a soft Peter Pan collar "
            "and a FINE BLACK GROSGRAIN RIBBON BOW tied at the throat (the maison's earliest "
            "signature). Small pearl drop earrings. A small white CAMELLIA brooch pinned at her "
            "shoulder. She is seated at her atelier worktable in a slight three-quarter angle, "
            "one hand resting gracefully on a folded piece of CREAM BOUCLÉ TWEED on the table "
            "before her, the other lightly at her lap. "
            "Setting: the atelier interior — soft cream wall behind her with a single tall "
            "arched window throwing soft Parisian daylight across her face from the side, the "
            "edge of a vintage couture worktable visible at the bottom of the frame. "
            "The portrait should radiate quiet authority — the founder of a haute-couture "
            "maison, photographed in 1948 Paris. " + VINTAGE_BW_RULE +
            "Camera: VERTICAL 4:5 portrait composition, ~85mm portrait lens, classic head-and-"
            "shoulders 1948 portrait framing (chest up to crown of head, slight space at top), "
            "sharp focus on her face, soft side-light. "
            "STRICTLY: NO text, NO logos, NO signage, NO watermark, NO Pinterest UI icons, NO "
            "modern color — fully monochrome BLACK AND WHITE silver-gelatin look."
        ),
    },

    # ---------- 3. ARCHIVE 1948 — sketchbook + first collection croquis ----------
    {
        "path": f"{base}/maison_archive_1948.jpg",
        "prompt": (
            "ALDORE Maison — Heritage Archive: 1948 first-collection croquis. "
            "An EDITORIAL VINTAGE STILL-LIFE of a 1948 couture archive: an open VINTAGE "
            "SKETCHBOOK on a smooth aged cream-ivory worktable, the LEFT page showing a "
            "delicate hand-drawn 1948-style PENCIL FASHION CROQUIS — a slim sketched figure "
            "wearing a fitted bouclé tailleur jacket with peplum waist and a knee-length "
            "skirt, classic 1948 New Look silhouette. Pencil and faded gouache wash details. "
            "The RIGHT page contains handwritten FRENCH ATELIER NOTES in elegant 1940s "
            "calligraphy (the words gracefully unreadable / illegible — just the impression "
            "of an atelier note, NO actual readable text or logos, just the visual texture of "
            "calligraphic French handwriting), with a small embossed maison seal in champagne-"
            "gold ink at the corner showing a stylized A and D interlocked. "
            "Beside the open sketchbook: a small vintage couture TAPE MEASURE coiled at the "
            "edge, a folded swatch of CREAM BOUCLÉ TWEED with subtle gold flecks, a small "
            "spool of FINE BLACK GROSGRAIN ribbon, and a worn brass-and-mother-of-pearl "
            "fountain pen resting diagonally. The page edges are slightly aged. "
            + VINTAGE_SEPIA_RULE + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, slight overhead three-quarter "
            "angle, the croquis sketch tack-sharp at center frame, very shallow depth of "
            "field on the surrounding objects, soft warm directional light. "
            "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO mannequins, NO readable text or "
            "logos, NO modern items, NO Pinterest UI icons, NO watermark. Pure vintage "
            "couture archive still-life."
        ),
    },

    # ---------- 4. ATELIER VINTAGE — archival B&W interior ----------
    {
        "path": f"{base}/maison_atelier_vintage.jpg",
        "prompt": (
            "ALDORE Maison — Heritage Archive: the original Atelier Rue de Sèvres, c. 1948. "
            "An ARCHIVAL VINTAGE INTERIOR PHOTOGRAPH of the maison's original 1948 atelier: "
            "an empty Parisian salon-atelier room with cream Haussmannian wall mouldings, "
            "tall arched French windows on the left letting in soft 1948-quality grainy "
            "daylight, polished herringbone parquet, a single ANTIQUE COUTURE DRESS FORM at "
            "the center of the room with a draped 1948 New Look bouclé tailleur jacket on it "
            "(jacket form readable but unfinished, with pinning marks), a vintage worktable "
            "to the side with a couture sewing machine of the 1940s era, fabric bolts stacked "
            "neatly against the back wall, an empty Louis XVI armchair, a vintage gold-framed "
            "mirror leaning against the wall. The composition reads: the maison's first "
            "atelier, captured in time. NO PEOPLE — pure architectural interior. "
            + VINTAGE_BW_RULE +
            "Camera: HORIZONTAL 4:3 landscape composition, ~28mm slightly wide architectural "
            "framing, soft natural daylight, sharp focus on the dress form at center, vintage "
            "1940s-camera depth of field. "
            "STRICTLY: NO text, NO logos, NO modern items (no laptops, no plastic), NO "
            "Pinterest UI icons, NO watermark — pure 1948 archival interior in B&W."
        ),
    },

    # ---------- 5. ATELIER OVERVIEW — current wide interior ----------
    {
        "path": f"{base}/maison_atelier_overview.jpg",
        "prompt": (
            "ALDORE Maison — the current Atelier Rue de Sèvres, Paris 6e. "
            "Editorial wide cinematic interior of the maison's CONTEMPORARY couture atelier "
            "in full daylight: a spacious salon-atelier room with cream Haussmannian wall "
            "mouldings, polished light-oak herringbone parquet glowing warm in afternoon "
            "Parisian daylight from tall arched French windows along the right wall, two long "
            "cream-ivory worktables running parallel through the center of the room with "
            "neatly arranged cream tweed swatches, fine black grosgrain ribbons spooled, gold "
            "thread spools, couture sewing tools, illustration croquis spread across the "
            "tables, a row of three antique COUTURE DRESS FORMS along the back wall each "
            "with a different cream bouclé tweed jacket-in-progress draped on them. Bolts of "
            "cream wool tweed and ivory silk neatly stacked on shelving on the left wall. A "
            "single bouquet of WHITE CAMELLIAS on a champagne-gold console at the back. The "
            "atelier is alive but empty — an editorial moment between work, the air still. "
            "NO PEOPLE — atmospheric architectural interior only. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~28mm slightly wide "
            "architectural framing, eye-level, shallow-to-medium depth of field, the worktable "
            "and dress forms tack-sharp, magazine-grade. " + CONTEMPORARY_TECH
        ),
    },

    # ---------- 6. ATELIER FABRIC — swatch wall macro ----------
    {
        "path": f"{base}/maison_atelier_fabric.jpg",
        "prompt": (
            "ALDORE Maison — the Atelier Fabric Wall. "
            "An EDITORIAL CLOSE-UP of an atelier wall covered with a CURATED PRESENTATION OF "
            "FABRIC SWATCHES pinned in a precise neat grid: rows of small CREAM BOUCLÉ TWEED "
            "swatches (each ~10×10cm), some with subtle CHAMPAGNE-GOLD FILAMENT FLECKS, "
            "alternating with small swatches of pure ivory silk, soft pearl-blue silk, and "
            "soft rose-pink silk, each pinned with a small handwritten paper label (labels "
            "purposefully blurry / unreadable, no actual readable text). Below the swatches, "
            "a horizontal row of FINE BLACK GROSGRAIN RIBBONS hanging neatly from small brass "
            "tacks, and a few small spools of fine GOLD SILK THREAD on a wooden ledge. "
            "Soft Parisian afternoon daylight from the side, warm honey-gold light grazing "
            "across the swatches highlighting texture, the cream wall behind softly lit. "
            "NO PEOPLE, NO HANDS — pure couture atelier still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~50mm look, eye-level facing the "
            "wall, shallow depth of field on the central swatches, magazine-grade. "
            + CONTEMPORARY_TECH
        ),
    },

    # ---------- 7. ATELIER DRESSFORMS ----------
    {
        "path": f"{base}/maison_atelier_dressforms.jpg",
        "prompt": (
            "ALDORE Maison — the Atelier Dress Forms. "
            "An EDITORIAL INTERIOR shot of FOUR ANTIQUE COUTURE DRESS FORMS lined up side by "
            "side in the atelier, each form is a vintage cream-linen-covered tailor's dummy "
            "on a champagne-gold metal stand. EACH dress form wears a different garment-in-"
            "progress: "
            "1) the leftmost form has a CREAM BOUCLÉ TWEED JACKET with subtle gold flecks, "
            "draped and pinned, one sleeve unfinished. "
            "2) The second form wears a STRAPLESS IVORY SILK BUSTIER MUSLIN — a structured "
            "couture toile in pristine ivory cotton muslin, partly basted. "
            "3) The third form wears an IVORY-CREAM SILK ROBE BODICE with delicate pearl "
            "trim being hand-set along the neckline (pearls visible, partially complete). "
            "4) The rightmost form wears a BLACK SILK CREPE LITTLE BLACK DRESS, finished and "
            "draped elegantly. "
            "Behind the row of dress forms: cream Haussmannian walls and a glimpse of polished "
            "light-oak herringbone parquet beneath. Soft Parisian afternoon daylight from the "
            "left. NO PEOPLE — atmospheric interior with the four 'silent witnesses' of the "
            "maison's craft. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 4:3 landscape composition, ~50mm look, slight three-quarter "
            "angle showing the forms in mild perspective, eye-level, shallow depth of field "
            "with the second and third forms tack-sharp, the outer two softly defocused. "
            + CONTEMPORARY_TECH
        ),
    },

    # ---------- 8. PHILOSOPHY — abstract poetic time-as-luxury ----------
    {
        "path": f"{base}/maison_philosophy.jpg",
        "prompt": (
            "ALDORE Maison — 'Le temps est le seul luxe' philosophy hero. "
            "An ABSTRACT POETIC EDITORIAL composition expressing the maison's philosophy that "
            "time is the only true luxury. "
            "Hero subject: a sweeping view across a stretch of polished LIGHT-OAK HERRINGBONE "
            "PARQUET FLOOR, with a long warm GOLDEN beam of Parisian late-afternoon sunlight "
            "raking diagonally across the parquet from the upper-left to the lower-right, "
            "lighting up the wood grain and creating long soft shadows. "
            "Resting at the lower-third of the frame on the parquet: a single ANTIQUE "
            "champagne-gold POCKET WATCH on a fine gold chain, the watch face open showing "
            "delicate Roman numerals (the numerals can be soft / not perfectly readable), "
            "the gold luminously catching the raking sunlight. The watch sits on top of a "
            "small softly draped piece of CREAM IVOIRE SILK FABRIC. "
            "Substantial NEGATIVE SPACE in the upper two-thirds of the frame — just sunlit "
            "parquet receding into atmospheric softness, allowing centered editorial text "
            "overlay. The mood is contemplative, time-reverent, hushed, golden. "
            "NO PEOPLE, NO HANDS — pure poetic still-life. "
            + PALETTE_RULES +
            "Camera: HORIZONTAL 16:9 cinematic landscape composition, ~50mm look, slightly "
            "elevated 30-degree angle on the parquet, very shallow depth of field with the "
            "pocket watch tack-sharp at lower-third, the parquet gradually softening into "
            "warm golden bokeh behind. " + CONTEMPORARY_TECH
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

print(f"\nMaison {total}컷 생성 완료.")
