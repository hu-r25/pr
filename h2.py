import streamlit as st

# إعدادات الصفحة - الافتراضية للجوال والوضع الداكن
st.set_page_config(
    page_title="  التخرج برومبت ", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم CSS احترافي مخصص بالكامل للوضع الداكن (Dark Mode) ومناسب للجوال
st.markdown("""
    <style>
    /* تحسين المظهر العام وخلفية التطبيق الداكنة */
    .stApp {
        background-color: #0f172a; /* لون داكن مريح جداً للعين */
    }
    
    /* تنسيق النصوص العربية وتوجيهها */
    .rtl-container {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-title {
        color: #f8fafc; /* نص أبيض مائل للمطفي */
        font-size: 26px;
        font-weight: 700;
        margin-bottom: 8px;
        text-align: center;
        letter-spacing: -0.5px;
    }
    
    .sub-title {
        color: #94a3b8; /* لون رمادي فاتح متناسق */
        font-size: 14px;
        margin-bottom: 28px;
        text-align: center;
        line-height: 1.6;
    }
    
    /* بطاقات احترافية مبسطة لعرض العناوين تتناسب مع الوضع الداكن */
    .section-card {
        background: #1e293b; /* لون البطاقة أفتح قليلاً من الخلفية العامة */
        padding: 14px 18px;
        border-radius: 12px;
        border-right: 5px solid #3b82f6; /* حافة زرقاء مميزة */
        margin-top: 24px;
        margin-bottom: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }
    
    .section-title {
        color: #f1f5f9;
        font-size: 16px;
        font-weight: 600;
        margin: 0;
    }
    
    /* تحسين مظهر مربع النص (صندوق الكود) بالكامل ليكون مرتباً واحترافياً */
    div[data-testid="stCodeBlock"] {
        border-radius: 12px !important;
        border: 1px solid #334155 !important; /* حدود داكنة متناسقة */
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3) !important;
        background-color: #1e293b !important; /* نفس لون البطاقات الفاخرة */
        padding: 4px !important;
    }
    
    /* تعديل النص داخل مربع الكود ليكون واضحاً وقابلاً للقراءة */
    div[data-testid="stCodeBlock"] pre {
        background-color: #1e293b !important;
        color: #e2e8f0 !important;
        font-family: 'Courier New', Courier, monospace !important;
        font-size: 14px !important;
        line-height: 1.5 !important;
        padding: 12px !important;
    }
    
    /* جعل زر النسخ بارزاً ومريحاً جداً للمس على الجوال */
    div[data-testid="stCodeBlock"] button {
        background-color: #3b82f6 !important; /* زر أزرق برّاق */
        color: #ffffff !important;
        border-radius: 8px !important;
        padding: 6px 14px !important;
        top: 12px !important;
        right: 12px !important;
        font-weight: 600 !important;
        transition: background-color 0.2s ease;
    }
    
    div[data-testid="stCodeBlock"] button:hover {
        background-color: #2563eb !important;
    }
    
    /* إخفاء القوائم والخطوط العلوية الإضافية لتبدو كتطبيق مستقل ونظيف */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* تحسين الخط الفاصل */
    hr {
        border-color: #334155 !important;
        margin: 20px 0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# واجهة التطبيق الرئيسية
st.markdown('<div class="rtl-container">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 مساعد البرومبت الذكي</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">منصة احترافية بالوضع الداكن مخصصة للجوال لنسخ الأوامر بضغطة زر واحدة وبشكل مرتب.</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- البرومبت الأول ---
st.markdown('<div class="section-card"><p class="section-title">📋 1. البرومبت الكلاسيكي (صورة طفلة)</p></div>', unsafe_allow_html=True)

prompt_1 = """A photorealistic graduation portrait of the young girl from the original image, maintaining her specific facial features, eyes, and sweet smile. She is wearing a classic black graduation cap and gown. She is sitting behind a small wooden desk with a large, open book in front of her. The lighting is soft studio quality, creating a professional and nostalgic atmosphere.
The background is a clean, neutral studio backdrop. High detail, 8k resolution."""

# عرض النص داخل المربع المرتب المخصص للنسخ
st.code(prompt_1, language="text")


# --- البرومبت الثاني ---
st.markdown('<div class="section-card"><p class="section-title">💻 2. برومبت التخرج (علوم الحاسوب)</p></div>', unsafe_allow_html=True)

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

st.markdown("<hr>", unsafe_allow_html=True)

# تذييل الصفحة
st.markdown('<p style="text-align:center; color:#64748b; font-size:12px;">انقر على الأيقونة الزرقاء داخل المربع لنسخ البرومبت فوراً</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
