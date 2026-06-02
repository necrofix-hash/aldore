from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

save_path = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/home/maison_teaser.jpg'

prompt = (
    "Editorial luxury interior photograph of the ALDORE Parisian maison private salon / boutique on "
    "Rue de Sèvres in the 6th arrondissement of Paris (haute couture maison since 1948). "
    "Atmosphere: a refined private fitting salon — heritage, intimate, serene Parisian elegance. "
    "Architecture: classic Haussmannian interior with tall ceilings, soft cream walls with delicate "
    "wall mouldings, herringbone parquet floor in warm light oak, a tall arched French window on the "
    "left wall with sheer ivory linen curtains glowing with soft afternoon daylight, a small Juliet "
    "balcony glimpsed beyond. "
    "Hero feature on the RIGHT wall: a built-in CHAMPAGNE-GOLD / brass garment display system — slim "
    "vertical gold frames mounted to the wall holding two horizontal gold rails, with a curated row of "
    "ALDORE garments hung evenly on cream wooden hangers — finished cream bouclé tweed jackets, ivory "
    "silk blouses, a pale pearl-blue tweed dress, a soft rose pink-beige blouse, all trimmed with fine "
    "black grosgrain. Above the hanging rail, a top shelf displays ALDORE signature handbags — exclusively "
    "in CREAM, IVORY, and PURE WHITE leather (NO brown, NO camel, NO cognac handbags). Below, a low "
    "white lacquer cabinet with champagne-gold pull handles, neatly displaying a few pairs of ivory "
    "leather slingbacks and cream loafers. "
    "Center foreground: a small round Parisian salon side table with a fluted champagne-gold base, "
    "supporting a generous bouquet of fresh WHITE CAMELLIA blooms in a clear glass vase (the maison's "
    "signature flower), a small leather-bound ALDORE lookbook, and a strand of pearls casually placed. "
    "Beside it, a single boucle cream upholstered pouf with a champagne-gold base. "
    "Left foreground accent: a tall full-length gold-framed Parisian arched mirror leaning against the "
    "wall, reflecting the window light. A small potted olive-leafless white orchid OR a green leafy "
    "ficus in a cream stone planter at the corner. "
    "Floor: warm light oak herringbone parquet partially covered by a soft cream Aubusson-style rug "
    "with subtle ivory medallion pattern. "
    "Lighting: layered — warm afternoon daylight pouring softly from the arched window on the left "
    "(primary), discreet recessed warm spotlights from the ceiling gently catching the gold rails and "
    "garments, a pair of small brass picture lights illuminating the hanging garments. NO harsh contrast, "
    "NO dark shadow areas — overall airy, luminous, dreamy. "
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold / brass, soft pearl, with "
    "tiny black grosgrain trim accents and warm light-oak wood grain. Absolutely NO camel, NO cognac, "
    "NO brown bags, NO beige-brown, NO olive, NO burgundy, NO wine red. "
    "Crucially: NO PEOPLE, NO MANNEQUIN WITH FACE, NO sewing, NO needle, NO thread spools, NO atelier "
    "workbench — this is a finished boutique salon space, not a workroom. "
    "Camera: wide editorial interior, ~24–35mm look, eye level, balanced composition, deep depth of field, "
    "everything in crisp luxurious focus. "
    "Style: Architectural Digest meets Chanel rue Cambon salon, Parisian heritage boutique editorial, "
    "ultra realistic, soft film grain, horizontal 16:9 composition, magazine-grade luxury interior. "
    "No text, no logos, no signage, no watermark."
)

print("ALDORE maison_teaser 재생성 중...")
response = client.models.generate_content(
    model='gemini-3-pro-image-preview',
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
    )
)

for part in response.candidates[0].content.parts:
    if part.inline_data:
        with open(save_path, 'wb') as f:
            f.write(part.inline_data.data)
        print(f"저장 완료: {save_path}")
        break
else:
    print("이미지 데이터 없음 — 응답 확인 필요")
