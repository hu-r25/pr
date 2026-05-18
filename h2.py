import streamlit as st

# إعدادات الصفحة - الافتراضية للجوال تكون أفضل عند اختيار خطوط واضحة وتباعد متناسق
st.set_page_config(
    page_title="منصة البرومبت الذكية", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم CSS احترافي مخصص بالكامل للهواتف الذكية مع دعم واجهة RTL (من اليمين لليسار)
st.markdown("""
    <style>
    /* تحسين المظهر العام وخلفية التطبيق */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* تنسيق النصوص العربية وتوجيهها */
    .rtl-container {
        direction: rtl;
        text-align: right;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    .main-title {
        color: #1e293b;
        font-size: 24px;
        font-weight: 700;
        margin-bottom: 8px;
        text-align: center;
    }
    
    .sub-title {
        color: #64748b;
        font-size: 14px;
        margin-bottom: 24px;
        text-align: center;
        line-height: 1.5;
    }
    
    /* بطاقات احترافية مبسطة لعرض العناوين */
    .section-card {
        background: #ffffff;
        padding: 12px 16px;
        border-radius: 12px;
        border-right: 5px solid #3b82f6;
        margin-top: 20px;
        margin-bottom: 10px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    
    .section-title {
        color: #1e293b;
        font-size: 16px;
        font-weight: 600;
        margin: 0;
    }
    
    /* تحسين مظهر صندوق الأكواد والنسخ على الجوال */
    div[data-testid="stCodeBlock"] {
        border-radius: 12px !important;
        border: 1px solid #e2e8f0 !important;
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05) !important;
        background-color: #1e293b !important;
    }
    
    /* جعل زر النسخ الافتراضي الخاص بـ streamlit بارزاً ومريحاً للمس على الجوال */
    div[data-testid="stCodeBlock"] button {
        background-color: #3b82f6 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 6px 12px !important;
        top: 8px !important;
        right: 8px !important;
    }
    
    /* إخفاء القوائم العلوية الإضافية والرموز لتبدو كتطبيق مستقل ونظيف على الشاشة */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# واجهة التطبيق الرئيسية
st.markdown('<div class="rtl-container">', unsafe_allow_html=True)

st.markdown('<div class="main-title">🎓 مساعد البرومبت الذكي</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">موقع مخصص للجوال لنسخ الأوامر (Prompts) بضغطة زر واحدة وبشكل احترافي.</div>', unsafe_allow_html=True)

# --- البرومبت الأول ---
st.markdown('<div class="section-card"><p class="section-title">📋 1. البرومبت الكلاسيكي (صورة طفلة)</p></div>', unsafe_allow_html=True)

prompt_1 = """A photorealistic graduation portrait of the young girl from the original image, maintaining her specific facial features, eyes, and sweet smile. She is wearing a classic black graduation cap and gown. She is sitting behind a small wooden desk with a large, open book in front of her. The lighting is soft studio quality, creating a professional and nostalgic atmosphere.
The background is a clean, neutral studio backdrop. High detail, 8k resolution."""

# عرض النص داخل صندوق برمجي يوفر زر نسخ مدمج ممتاز جداً للجوال
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

# تذييل الصفحة
st.markdown('<br><p style="text-align:center; color:#94a3b8; font-size:12px;">انقر على الأيقونة الزرقاء داخل المربع لنسخ النص فوراً</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
