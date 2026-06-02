from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

base = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection'

PRODUCT_TECH = (
    "Camera: SQUARE 1:1 composition, luxury product still-life, ~85mm look, soft Parisian "
    "afternoon daylight from above-left, very slight directional shadow, shallow depth of field "
    "with the hero object tack-sharp and edges softly defocused. The object is centered or "
    "very slightly off-center with thoughtful negative space around it. Background: a plain "
    "soft warm cream-ivory surface (subtle texture — like raw silk or smooth matte plaster), "
    "no props beyond what is described. "
    "Style: Chanel-coded couture e-commerce / lookbook product photography, ultra realistic, "
    "subtle film grain, magazine-grade luxury hero still-life. "
    "STRICTLY: NO PEOPLE, NO HANDS, NO MODEL, NO text, NO logos, NO signage, NO watermark, "
    "NO sewing tools, NO mannequins. Pure single-product hero shot. "
)

PRODUCT_PALETTE = (
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold / brass hardware, "
    "soft pearl, with discreet black grosgrain or black leather accents only where specified. "
    "Absolutely NO camel, NO cognac, NO brown, NO beige-brown, NO olive, NO khaki, NO burgundy, "
    "NO wine, NO red, NO navy. "
)

images = [
    {
        "path": f"{base}/acc_handbag.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Les Accessoires: Le Sac Doré. The maison's signature "
            "top-handle handbag, hero product still-life. "
            "Hero product: a single CREAM IVOIRE LAMBSKIN TOP-HANDLE HANDBAG, mid-size structured "
            "rectangular silhouette. Construction: butter-soft cream lambskin leather with subtle "
            "DIAMOND QUILTING stitched across the body, a single rigid TOP HANDLE in matching "
            "cream lambskin attached with two CHAMPAGNE-GOLD hardware rings, a thin detachable "
            "CHAMPAGNE-GOLD chain shoulder strap with woven cream leather threading, and a single "
            "sculpted CHAMPAGNE-GOLD CAMELLIA-engraved clasp at the front center closing the flap. "
            "A delicate FINE BLACK GROSGRAIN ribbon piping runs along the front flap edge. "
            "The bag stands upright on a smooth cream ivory surface, slightly three-quarter angle "
            "to show both the front face and the side gusset, casting a soft directional shadow "
            "to the right. "
            + PRODUCT_PALETTE + PRODUCT_TECH
        ),
    },
    {
        "path": f"{base}/acc_shoes.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Les Accessoires: L'Escarpin Camélia. The maison's signature "
            "slingback pointed pumps, hero product still-life. "
            "Hero product: A PAIR of CREAM IVOIRE LAMBSKIN POINTED-TOE SLINGBACK PUMPS arranged "
            "side by side, slightly three-quarter angle. The shoe: cream ivoire smooth lambskin "
            "upper with a sharply elegant POINTED TOE CAPPED IN BLACK PATENT LEATHER (the iconic "
            "couture two-tone slingback silhouette — cream body, BLACK pointed toe), a mid-height "
            "(~7cm) sculptural CHAMPAGNE-GOLD heel, an elastic slingback strap at the back, and a "
            "single small CHAMPAGNE-GOLD CAMELLIA-engraved hardware ornament at the vamp / instep. "
            "The shoes rest on a smooth cream ivory surface, casting soft directional shadows. "
            + PRODUCT_PALETTE + PRODUCT_TECH
        ),
    },
    {
        "path": f"{base}/acc_jewelry.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Les Accessoires: Le Collier Perle. The maison's signature "
            "multi-strand pearl necklace, hero product still-life. "
            "Hero product: A LUXURIOUS THREE-STRAND LAYERED PEARL NECKLACE — three concentric "
            "strands of slightly graduated round IVORY-CREAM PEARLS (each pearl 6-9mm, classically "
            "lustrous, perfectly matched), connected at the back by a sculpted CHAMPAGNE-GOLD "
            "CAMELLIA-engraved clasp. The strands are arranged in a softly draped FAN / CASCADE "
            "shape on the cream ivory surface — the longest strand spread out at the bottom, "
            "the shortest strand curved gracefully at the top, creating a luminous fan of pearls. "
            "Soft directional light catches each pearl creating tiny crisp highlights and a "
            "delicate cast shadow on the cream surface. "
            + PRODUCT_PALETTE + PRODUCT_TECH
        ),
    },
    {
        "path": f"{base}/acc_pearls.jpg",
        "prompt": (
            "ALDORE Spring/Summer 2027 — Les Accessoires: La Broche Camélia. The maison's signature "
            "white camellia brooch, hero product still-life. "
            "Hero product: A SINGLE COUTURE WHITE CAMELLIA BROOCH — a sculpted ivory-white silk "
            "fabric camellia bloom (the maison's signature flower) with multiple layered pristine "
            "creamy-white petals arranged in a perfect spiral, mounted onto a delicate sculpted "
            "CHAMPAGNE-GOLD circular setting with an engraved fine border, with a small visible "
            "CHAMPAGNE-GOLD pin clasp behind it. The brooch sits centered on a smooth cream "
            "ivory surface, slightly three-quarter angled so we can see the depth of the "
            "petals and a glimpse of the gold setting peeking from underneath. The pearl-white "
            "petals catch soft directional daylight, casting a delicate shadow. "
            + PRODUCT_PALETTE + PRODUCT_TECH
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

print("\nChapter Les Accessoires 4컷 생성 완료.")
