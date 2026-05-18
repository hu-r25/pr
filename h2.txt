import streamlit as st

# إعدادات الصفحة لتكون مريحة ومتناسقة
st.set_page_config(page_title="منصة نسخ برومبت التخرج", page_icon="🎓", layout="centered")

# تنسيق مخصص لجعل النصوص تظهر بشكل ممتاز ومن اليمين إلى اليسار في الشروحات العربية
st.markdown("""
    <style>
    .rtl-text {
        direction: rtl;
        text-align: right;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 منصة نسخ برومبت تخرج الذكاء الاصطناعي")
st.markdown('<p class="rtl-text">اضغط على أيقونة النسخ في الزاوية اليمنى لكل مربع نص لنسخ البرومبت مباشرة واستخدامه.</p>', unsafe_allow_html=True)

st.markdown("---")

# النص الأول - برومبت التخرج الكلاسيكي للطفلة
st.markdown('<h3 class="rtl-text">📋 البرومبت الأول: صورة تخرج كلاسيكية لطفلة</h3>', unsafe_allow_html=True)
prompt_1 = """A photorealistic graduation portrait of the young girl from the original image, maintaining her specific facial features, eyes, and sweet smile. She is wearing a classic black graduation cap and gown. She is sitting behind a small wooden desk with a large, open book in front of her. The lighting is soft studio quality, creating a professional and nostalgic atmosphere.
The background is a clean, neutral studio backdrop. High detail, 8k resolution."""

st.code(prompt_1, language="text")

st.markdown("---")

# النص الثاني - برومبت تخرج علوم الحاسوب
st.markdown('<h3 class="rtl-text">💻 البرومبت الثاني: صورة تخرج احترافية (علوم حاسوب)</h3>', unsafe_allow_html=True)
prompt_2 = """Transform the attached photo into a professional graduation portrait with a Computer Science theme.

Keep the same original facial features and identity without changing the age, eyes, nose, mouth, or face shape.
Place the person in the center with a straight, neat posture, looking naturally at the camera.

Dress the person in a formal black graduation gown with a straight black square graduation cap on the head, and a gold tassel on the side of the cap.
Add a white shirt and black tie under the gown if suitable.
 
Use a Computer Science background: dark blue tech studio, computer screens with programming code, circuit lines, digital icons, and soft blue lighting.
Improve the photo quality, remove noise, scratches, and blur, enhance lighting and colors, and make the skin tone natural and clear for printing without over-editing.

The final result should look realistic, clean, high-resolution, and like a professional studio graduation photo.
Do not distort the face, eyes, hands, or body. Do not add random text, logos, or watermarks."""

st.code(prompt_2, language="text")

st.markdown("---")
st.markdown('<p class="rtl-text" style="text-align:center; color:gray;">صُنع ببساطة ومتاح للنسخ السريع</p>', unsafe_allow_html=True)