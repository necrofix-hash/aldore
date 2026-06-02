from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

save_path = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection/cat_robe.jpg'

prompt = (
    "Editorial luxury fashion photograph for Parisian haute couture maison ALDORE (since 1948), "
    "Spring/Summer 2027 collection chapter cover image — Chapter II: La Robe. "
    "HORIZONTAL 16:9 landscape composition. The MODEL is placed on the RIGHT half of the frame; "
    "the LEFT half is clean luminous negative-space background (soft pale ivory-cream studio "
    "backdrop with the faintest gradient of soft daylight) reserved for editorial typographic "
    "overlay (do not place anything on the left half). "
    "Model: a refined Korean K-drama-coded woman in her mid-to-late 20s, slim graceful figure, "
    "natural elegant beauty, full face visible and softly lit, long dark hair styled in soft "
    "loose waves brushed gently back from the face (NOT slick chignon — flowing romantic waves), "
    "small 5-7mm pearl drop earrings, serene confident gaze straight to camera. "
    "She wears the FLAGSHIP COUTURE GOWN of the chapter: a FLOOR-LENGTH PALE PEARL-BLUE / SOFT "
    "SILVERY-IVORY EVENING GOWN. STRAPLESS sweetheart neckline (with a delicate sheer illusion "
    "mesh panel rising softly above the bust), FITTED beaded bodice densely embroidered with "
    "pearls, crystals, and silver bugle beads, defined natural waistline marked by a slim "
    "pale satin band, then a FULL A-LINE BALL-GOWN SKIRT cascading to the floor with a soft "
    "subtle train. The skirt is covered in TIERED SCALLOPED beadwork — concentric horizontal "
    "scalloped/feather rows of pearl and crystal beadwork creating a luminous shimmering relief, "
    "with sheer tulle layers underneath catching the soft light. The color is a SOFT POWDERY "
    "PEARL-BLUE — never navy, never royal blue, never teal, never gray. The dress is unmistakably "
    "haute couture red-carpet — STRUCTURED, sculptural, formal eveningwear. "
    "She stands tall and centered in graceful editorial pose, full-length visible from head "
    "to floor, weight evenly distributed, hands relaxed at her sides, the gown's skirt softly "
    "spreading around her feet. Pale satin pointed-toe pumps barely peek from beneath the hem. "
    "Lighting: soft luminous studio light from above-front, gently modeling the bead texture, "
    "no harsh shadow. Background: very soft pale ivory-cream studio backdrop, slight gradient, "
    "completely empty on the left half. "
    "Strict color palette: cream ivoire, ivory, pure white, champagne gold, pale pearl-blue, "
    "soft pearl beadwork, with discreet silver crystal accents. Absolutely NO camel, NO cognac, "
    "NO brown, NO beige-brown, NO olive, NO khaki, NO burgundy, NO wine, NO red, NO navy, NO gray. "
    "STRICTLY couture eveningwear — STRUCTURED bodice with defined waistline, NOT loose, NOT a slip, "
    "NOT bias-cut, NOT drape-y, NOT lingerie, NOT pajamas. Must read clearly as red-carpet / runway "
    "/ haute couture flagship gown. "
    "Camera: full-length editorial fashion portrait in HORIZONTAL 16:9 landscape, ~50mm look, "
    "eye-level, soft natural studio daylight, shallow depth of field, model tack-sharp, background "
    "softly blurred. "
    "Style: ALDORE SS27 lookbook chapter cover, Chanel haute-couture-coded heritage glamour, ultra "
    "realistic, subtle film grain, magazine-grade. "
    "STRICTLY: NO text, NO logos, NO signage, NO watermark, NO Chinese / Korean / English captions."
)

print("ALDORE cat_robe (Chapter II 커버) 재생성 중...")
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
