from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyCP_wD7ORGxXzgNRXogP_ZoCC_nt7UiBdc')

save_path = '/Users/miaro/claude/job/portfolio/brand_sites/aldore/images/collection/cat_tweed.jpg'

prompt = (
    "Editorial luxury still-life photograph for Parisian haute couture maison ALDORE (since 1948), "
    "Spring/Summer 2027 collection chapter cover image — Chapter III: Le Tweed Doré. "
    "Hero subject (placed on the RIGHT half of the frame, the LEFT third must be a clean negative-space "
    "background for overlay text — empty soft cream wall with a single arched Parisian window): "
    "a couture dressmaker's mannequin (linen-wrapped torso form, no face, no head — just the shoulder-to-"
    "hip torso) wearing a finished, exquisite cream bouclé TWEED jacket — clearly the signature ALDORE "
    "Le Tweed Doré jacket. NO PEOPLE in frame. NO FACE. Only the headless tailor's mannequin form. "
    "Jacket details, very crisp and prominent: cream ivoire bouclé tweed weave with subtle metallic "
    "champagne-gold flecks woven through the fabric (Le Fil Doré), a fine BLACK GROSGRAIN trim along "
    "the collar / lapel edge / cuffs / hem, four sculpted CHAMPAGNE-GOLD signature buttons down the "
    "front, a single white camellia brooch pinned at the lapel. Open neckline shows a glimpse of ivory "
    "silk lining inside. The jacket falls cropped at the hip with a clean tailored silhouette. "
    "Atelier setting, soft and reverent: pale cream walls, light oak parquet floor, a tall arched "
    "Parisian window on the LEFT background with sheer ivory linen curtains glowing from outside "
    "afternoon daylight (this provides the negative space for typographic overlay). On the right "
    "behind the mannequin, a softly blurred wooden wall rack of cream and champagne-gold thread spools. "
    "On the floor at the base of the mannequin: 2~3 champagne-gold thread spools and a single white "
    "camellia bloom resting on the parquet. "
    "Lighting: warm cinematic afternoon daylight from the window-left, soft diffused, beautifully "
    "modeling the tweed texture and gold buttons. NO harsh top spotlight, NO heavy shadows. "
    "The jacket is the absolute hero — every weave, every button, the black grosgrain trim, and the "
    "subtle gold flecks must read clearly. "
    "Color palette strict: cream ivoire, ivory, pure white, champagne gold, with discreet black "
    "grosgrain. Absolutely no camel, cognac, brown, beige-brown, olive, burgundy, or wine. "
    "Camera: medium-wide editorial still-life, ~50mm, slight three-quarter angle on the mannequin to "
    "see lapel and gold button line cleanly, shallow depth of field, mannequin tack-sharp, background "
    "softly defocused. "
    "Style: Chanel-coded Parisian haute couture chapter cover, cinematic luxury heritage editorial, "
    "ultra realistic, subtle film grain, horizontal 16:9 composition, magazine-grade. "
    "No text, no logos, no signage, no watermark, no people, no face."
)

print("ALDORE Le Tweed Doré 챕터 커버 재생성 중...")
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
