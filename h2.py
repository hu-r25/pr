import streamlit as st

# إعدادات الصفحة - الافتراضية للجوال والوضع الداكن
st.set_page_config(
    page_title="CS", 
    page_icon="🎓", 
    layout="centered",
    initial_sidebar_state="collapsed"
)

# تصميم CSS احترافي مخصص بالكامل لجعل النصوص حرة والأزرار متناسقة
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
    
    /* تنسيق النص الإنجليزي ليكون حراً تماماً وصافياً وبدون أي بوكس رمادي أو حدود نهائياً */
    .prompt-text-pure {
        color: #e2e8f0;
        font-size: 16px;
        line-height: 1.6;
        text-align: left;
        direction: ltr;
        padding: 12px 5px;
        word-wrap: break-word;
        white-space: pre-wrap; /* للمحافظة على الأسطر كاملة وممتدة للأسفل */
    }
    
    /* تصميم زر التحديد والتظليل السحري أسفل النص */
    .select-btn {
        display: block;
        width: 100%;
        background-color: #3b82f6;
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
        margin-top: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.3);
        text-align: center;
    }
    
    .select-btn:active {
        background-color: #2563eb;
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

# عرض الكلام ككتابة عادية حرة وصافية 100% بدون أي بوكس مع إعطائه معرّف ID للتحديد
st.markdown(f'<div id="p1" class="prompt-text-pure">{prompt_1}</div>', unsafe_allow_html=True)

# زر التحديد التلقائي المضمون للجوال للنص الأول
st.html("""
<button class="select-btn" onclick="
    const textNode = document.getElementById('p1');
    const range = document.createRange();
    range.selectNodeContents(textNode);
    const select = window.getSelection();
    select.removeAllRanges();
    select.addRange(range);
">📋 اضغط هنا لتظليل النص الأول (ثم اختر نسخ)</button>
""")


# --- البرومبت الثاني ---
st.markdown('<div class="section-card"><p class="section-title">2. Prompt</p></div>', unsafe_allow_html=True)

prompt_2 = """A photorealistic graduation portrait of the young girl from the original image, maintaining her specific facial features, eyes, and sweet smile. She is wearing a classic black graduation cap and gown. She is sitting behind a small wooden desk with a large, open book in front of her. The lighting is soft studio quality, creating a professional and nostalgic atmosphere.
The background is a clean, neutral studio backdrop. High detail, 8k resolution."""

# عرض الكلام الثاني ككتابة عادية حرة وصافية 100% بدون أي بوكس
st.markdown(f'<div id="p2" class="prompt-text-pure">{prompt_2}</div>', unsafe_allow_html=True)

# زر التحديد التلقائي المضمون للجوال للنص الثاني
st.html("""
<button class="select-btn" onclick="
    const textNode = document.getElementById('p2');
    const range = document.createRange();
    range.selectNodeContents(textNode);
    const select = window.getSelection();
    select.removeAllRanges();
    select.addRange(range);
">📋 اضغط هنا لتظليل النص الثاني (ثم اختر نسخ)</button>
""")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
