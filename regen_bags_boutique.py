from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

bags_base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/bags'
bout_base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/boutique'

PALETTE_RULES = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, soft pearl, "
    "warm light-oak wood, with discreet black grosgrain or black silk satin accents only "
    "where described. Absolutely NO camel, NO cognac, NO brown leather, NO beige-brown, "
    "NO olive, NO khaki, NO burgundy, NO wine, NO red, NO navy. "
)

PRODUCT_TECH = (
    "Camera: SQUARE 1:1 composition, luxury product still-life, ~85mm look, soft Parisian "
    "afternoon daylight from above-left, very slight directional shadow, shallow depth of "
    "field with the hero object tack-sharp and edges softly defocused. Background: a plain "
    "soft warm cream-ivory surface (subtle texture — like raw silk or smooth matte plaster), "
    "no props beyond what is described. "
    "Style: Chanel-coded couture e-commerce / lookbook product photography, ultra realistic, "
    "subtle film grain, magazine-grade luxury hero still-life. "
    "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos, NO signage, NO watermark, "
    "NO Pinterest UI icons, NO sewing tools, NO mannequins. Pure single-product hero shot. "
)

INTERIOR_TECH = (
    "Camera: HORIZONTAL 4:3 landscape composition, ~28-35mm slightly wide architectural "
    "framing, eye-level, shallow-to-medium depth of field, magazine-grade luxury retail "
    "interior editorial. Style: Chanel-coded couture maison boutique, ultra realistic, "
    "subtle film grain, magazine-grade. STRICTLY: NO PEOPLE, NO MODELS, NO HANDS, NO text, "
    "NO logos, NO signage, NO watermark, NO Pinterest UI icons. "
)

images = [
    # ---------- BAGS ----------
    {
        "path": f"{bags_base}/bag_shoulder.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Sac à l'Épaule. The maison's medium structured "
            "shoulder bag, hero product still-life. "
            "Hero product: a single CREAM IVOIRE LAMBSKIN MEDIUM SHOULDER BAG, slightly "
            "rounded structured rectangular silhouette (medium-large size, larger than a "
            "top-handle). Construction: butter-soft cream lambskin leather with subtle DIAMOND "
            "QUILTING stitched across the body, a single rigid TOP HANDLE in matching cream "
            "lambskin attached with two CHAMPAGNE-GOLD hardware rings, AND a longer "
            "DETACHABLE CHAMPAGNE-GOLD CHAIN SHOULDER STRAP threaded through with cream "
            "leather strips, draped naturally to the side as if recently set down. A FINE "
            "BLACK GROSGRAIN ribbon piping runs along the front flap edge. The flap closes "
            "with a sculpted CHAMPAGNE-GOLD CAMELLIA-engraved clasp at center. "
            "The bag stands upright on a smooth cream ivory surface, slight three-quarter "
            "angle, the chain strap visible draped to the side, casting soft directional "
            "shadow. " + PALETTE_RULES + PRODUCT_TECH
        ),
    },
    {
        "path": f"{bags_base}/bag_clutch.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — La Pochette Doré. The maison's signature evening "
            "clutch, hero product still-life. "
            "Hero product: a single ELEGANT EVENING CLUTCH in BLACK SILK SATIN with a refined "
            "envelope silhouette, slim flat shape, no handle. The silk satin body has a "
            "luminous matte sheen (NOT shiny PVC, true silk satin couture finish). The flap "
            "closes with a single sculpted CHAMPAGNE-GOLD CAMELLIA-engraved clasp at center "
            "front. A discreet FINE GOLD CHAIN wrist strap is visible coiled beside the clutch "
            "(removable). A FINE WHITE CAMELLIA fabric flower brooch sits at the upper-left "
            "corner of the clutch as the maison's hero detail. The clutch lies flat on a "
            "smooth cream ivory surface, slight three-quarter angle, soft directional shadow "
            "to the right. The contrast: deep black silk against cream cream ivory surface, "
            "with luminous gold and white camellia accents. " + PALETTE_RULES + PRODUCT_TECH
        ),
    },
    {
        "path": f"{bags_base}/bag_micro.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Le Mini Sac. The maison's micro top-handle bag, "
            "hero product still-life. "
            "Hero product: a single TINY MICRO TOP-HANDLE BAG (palm-sized, very small) in "
            "CREAM IVOIRE LAMBSKIN with subtle DIAMOND QUILTING. The micro bag is a perfectly "
            "miniaturized version of Le Sac Doré: same rigid TOP HANDLE in matching cream "
            "lambskin attached with two tiny CHAMPAGNE-GOLD hardware rings, a slim detachable "
            "CHAMPAGNE-GOLD CHAIN crossbody strap looped around it, a tiny sculpted "
            "CHAMPAGNE-GOLD CAMELLIA clasp closing the front flap, FINE BLACK GROSGRAIN "
            "piping along the flap edge. The bag stands upright on a smooth cream ivory "
            "surface, the chain crossbody strap softly coiled around the base, slight three-"
            "quarter angle. " + PALETTE_RULES + PRODUCT_TECH
        ),
    },

    # ---------- BOUTIQUE — 4 cities ----------
    {
        "path": f"{bout_base}/bout_paris.jpg",
        "prompt": (
            "ALDORE Boutique — Paris flagship at 14 Rue de Sèvres, exterior at GOLDEN HOUR. "
            "An EDITORIAL EXTERIOR architectural photograph of the maison's flagship boutique "
            "facade in Paris's 6e arrondissement: a graceful HAUSSMANNIAN limestone CREAM-"
            "IVORY building facade with classic ornate Parisian wrought-iron balcony railings "
            "on the upper floors, a discreet polished BRASS DOOR PLAQUE beside the boutique's "
            "wooden double door, two tall arched display windows on either side of the "
            "entrance softly lit from within with warm champagne-gold light, sheer ivory "
            "linen curtains diffusing the interior glow. "
            "On the cobblestone sidewalk in front of the entrance: two large champagne-gold "
            "PLANTERS each holding a single tall WHITE CAMELLIA shrub in full bloom, framing "
            "the door symmetrically. The polished cobblestones glow warm gold in the late-"
            "afternoon raking sunlight. NO PEOPLE, NO modern cars, NO modern signage — pure "
            "timeless 6e arrondissement atmosphere. The plaque text is purposely soft / "
            "unreadable (NO actual readable text or logos). " + PALETTE_RULES + INTERIOR_TECH
        ),
    },
    {
        "path": f"{bout_base}/bout_seoul.jpg",
        "prompt": (
            "ALDORE Boutique — Seoul Cheongdam-dong flagship, INTERIOR. "
            "An EDITORIAL INTERIOR architectural photograph of the maison's Seoul boutique "
            "salon: a refined contemporary luxury retail interior with cream travertine walls "
            "and warm light-oak HERRINGBONE PARQUET (the same Parisian-coded floor as the "
            "atelier), a tall central CHAMPAGNE-GOLD-FRAMED ROCOCO MIRROR on the back wall, "
            "two CREAM SILK UPHOLSTERED LOUIS XVI ARMCHAIRS arranged in a private fitting "
            "vignette beside a small champagne-gold side table holding a WHITE CAMELLIA "
            "bouquet, softly diffused warm Korean afternoon daylight pouring through tall "
            "floor-to-ceiling windows on the right (with sheer ivory linen curtains), one "
            "champagne-gold-and-cream display console showing a single CREAM BOUCLÉ TWEED "
            "JACKET on a vintage couture dress form. Clean, airy, magazine-grade luxury "
            "Korean retail interior — Parisian heritage applied to a Seoul flagship. "
            + PALETTE_RULES + INTERIOR_TECH
        ),
    },
    {
        "path": f"{bout_base}/bout_tokyo.jpg",
        "prompt": (
            "ALDORE Boutique — Tokyo Ginza flagship, INTERIOR. "
            "An EDITORIAL INTERIOR architectural photograph of the maison's Tokyo Ginza "
            "boutique salon: a refined Japanese-coded interpretation of the Parisian maison — "
            "soft cream walls with delicate Haussmannian-style mouldings, polished light-oak "
            "HERRINGBONE PARQUET, a single tall CHAMPAGNE-GOLD-FRAMED MIRROR on the back wall, "
            "ONE quietly placed CREAM SILK LOUIS XVI ARMCHAIR (the Japanese restraint — fewer "
            "objects, more space), a small low cream-and-champagne-gold pedestal table holding "
            "a single fresh WHITE CAMELLIA in a slim champagne-gold ikebana-style vase, soft "
            "Tokyo afternoon daylight pouring through a single tall arched window on the "
            "left, and on the back wall a single CREAM BOUCLÉ TWEED jacket displayed on an "
            "antique couture dress form spotlit by soft directional light. The Ginza-coded "
            "atmosphere is hushed, minimal, almost zen — Parisian heritage filtered through "
            "Japanese refinement. " + PALETTE_RULES + INTERIOR_TECH
        ),
    },
    {
        "path": f"{bout_base}/bout_nyc.jpg",
        "prompt": (
            "ALDORE Boutique — New York Madison Avenue flagship, INTERIOR. "
            "An EDITORIAL INTERIOR architectural photograph of the maison's New York Madison "
            "Avenue boutique salon: a refined American-coded interpretation of the Parisian "
            "maison — soft cream walls with delicate Haussmannian wall mouldings, polished "
            "CREAM-IVORY MARBLE FLOOR (NOT brown, NOT dark — pure cream marble), a tall "
            "central CHAMPAGNE-GOLD ROCOCO MIRROR on the back wall flanked by two slim "
            "CHAMPAGNE-GOLD wall sconces, two CREAM SILK UPHOLSTERED LOUIS XVI ARMCHAIRS "
            "facing each other in a private fitting arrangement, a small champagne-gold side "
            "table between them holding a generous WHITE CAMELLIA bouquet, soft warm "
            "afternoon daylight pouring through a tall arched window on the right (with sheer "
            "ivory linen curtains), TWO CREAM BOUCLÉ TWEED jackets displayed on antique "
            "couture dress forms along the left wall, softly spotlit. The Madison Avenue "
            "atmosphere is more dramatic and luxurious — slightly more glamour, slightly "
            "richer warm-gold tonality, but still strictly the maison's cream-and-gold "
            "palette. " + PALETTE_RULES + INTERIOR_TECH
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

print(f"\nBags + Boutique {total}컷 생성 완료.")
