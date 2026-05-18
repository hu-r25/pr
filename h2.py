import streamlit as st

# إعدادات الصفحة - الافتراضية للجوال والوضع الداكن
st.set_page_config(
    page_title="CS", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم CSS سحري يخفي البوكس الرمادي تماماً ويجعل النص حراً وكاملاً
st.markdown("""
    <style>
    /* خلفية التطبيق الداكنة */
    .stApp {
        background-color: #0f172a; 
    }
    
    /* تنسيق النصوص العربية وتوجيهها */
    .rtl-container {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-title {
        color: #f8fafc; 
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 8px;
        text-align: center;
    }
    
    /* بطاقات العناوين */
    .section-card {
        background: #1e293b; 
        padding: 14px 18px;
        border-radius: 12px;
        border-right: 5px solid #3b82f6; 
        margin-top: 24px;
        margin-bottom: 16px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .section-title {
        color: #f1f5f9;
        font-size: 16px;
        font-weight: 600;
        margin: 0;
    }
    
    /* إخفاء البوكس الرمادي والحدود والظلال تماماً وجعل الخلفية شفافة 100% */
    div[data-testid="stCodeBlock"] {
        background-color: transparent !important; 
        border: none !important; 
        box-shadow: none !important; 
        padding: 0 !important;
    }
    
    /* تنسيق الخط ليظهر البرومبت ككتابة عادية حرة وممتدة بالكامل داخل الموقع */
    div[data-testid="stCodeBlock"] pre {
        background-color: transparent !important;
        color: #e2e8f0 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important; 
        font-size: 15px !important;
        line-height: 1.6 !important;
        white-space: pre-wrap !important; /* يمنع ظهور شريط التمرير ويجعل النص كاملاً ممتداً */
        word-wrap: break-word !important;
        padding: 10px 5px !important;
    }
    
    /* تخصيص أيقونة النسخ الأصلية المستقرة وجعلها زرقاء واضحة في الزاوية */
    div[data-testid="stCodeBlock"] button {
        background-color: #3b82f6 !important; 
        color: #ffffff !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
        top: -12px !important; 
        right: 0px !important;
    }
    
    div[data-testid="stCodeBlock"] button:hover {
        background-color: #2563eb !important;
    }
    
    /* إخفاء قوائم ستريمليت الإضافية ليكون المظهر نظيفاً */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    hr {
        border-color: #334155 !important;
        margin: 20px 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة التطبيق الرئيسية
st.markdown('<div class="rtl-container">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 Prompt Graduation</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- البرومبت الأول ---
st.markdown('<div class="section-card"><p class="section-title">1. Prompt</p></div>', unsafe_allow_html=True)

prompt_1 = """Transform the attached photo into a professional graduation portrait with a Computer Science theme.

Keep the same original facial features and identity without changing the age, eyes, nose, mouth, or face shape.
Place the person in the center with a straight, neat posture, looking naturally at the camera.

Dress the person in a formal black graduation gown with a straight black square graduation cap on the head, and a gold tassel on the side of the cap.
Add a white shirt and black tie under the gown if suitable.
 
Use a Computer Science background: dark blue tech studio, computer screens with programming code, circuit lines, digital icons, and soft blue lighting.
Improve the photo quality, remove noise, scratches, and blur, enhance lighting and colors, and make the skin tone natural and clear for printing without over-editing.

The final result should look realistic, clean, high-resolution, and like a professional studio graduation photo.
Do not distort the face, eyes, hands, or body. Do not add random text, logos, or watermarks."""

# عرض النص عبر st.code المفرغ تماماً من الصندوق ليعمل زر النسخ الأصلي بكل استقرار
st.code(prompt_1, language="text")


# --- البرومبت الثاني ---
st.markdown('<div class="section-card"><p class="section-title">2. Prompt</p></div>', unsafe_allow_html=True)

prompt_2 = """A photorealistic graduation portrait of the young girl from the original image, maintaining her specific facial features, eyes, and sweet smile. She is wearing a classic black graduation cap and gown. She is sitting behind a small wooden desk with a large, open book in front of her. The lighting is soft studio quality, creating a professional and nostalgic atmosphere.
The background is a clean, neutral studio backdrop. High detail, 8k resolution."""

# عرض النص الثاني حراً وبدون بوكس
st.code(prompt_2, language="text")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#64748b; font-size:12px;">انقر على أيقونة النسخ الزرقاء في زاوية كل نص لنسخه مباشرة</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
