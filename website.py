# import streamlit as st
# from PIL import Image

# # Set page config
# st.set_page_config(
#     page_title="صفحتي الشخصية",
#     page_icon=":wave:",
#     layout="centered",
#     initial_sidebar_state="auto",
# )

# # Custom CSS for RTL layout
# st.markdown(
#     """
#     <style>
#     body {
#         direction: rtl;
#     }
#     .css-1lcbmhc.e1fqkh3o3 {
#         text-align: right;
#     }
#     .css-18e3th9 {
#         text-align: right;
#     }
#     .css-12oz5g7 {
#         text-align: right;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # Titel der Seite
# st.title("مرحبًا بكم في صفحتي الشخصية")

# # Sidebar mit einem Bild
# with st.sidebar:
#     st.image("images/profile_image.PNG", width=150)
#     st.header("من أنا")
#     st.write("""
#     أنا مهندس ميكاترونيك، أتمتع بخبرة واسعة ومعرفة عميقة في مجالات الهندسة الميكانيكية، والهندسة الكهربائية، وعلوم الحاسوب.
#     أتميز بقدرتي على تصميم وتطوير الأنظمة الميكاترونية والأتمتة، بما في ذلك الروبوتات والماكينات.
#     بفضل معرفتي الواسعة في التحكم الآلي والتصميم الإلكتروني والبرمجة، أستطيع تصميم وتطوير الدوائر الإلكترونية وأنظمة تحكم المحركات والمستشعرات والمشغلات.
#     كما أن لدي خبرة في استخدام برامج النمذجة والمحاكاة الهندسية لتصميم واختبار الأنظمة الميكانيكية والكهربائية بكفاءة.
#     """)

# # Hauptabschnitt
# st.header("التواصل")
# st.write("""
# - **البريد الإلكتروني:** dein.email@example.com
# - **LinkedIn:** [ملفي على لينكدإن](https://www.linkedin.com/in/dein-profil)
# - **Github:** [ملفي على جيت هب](https://github.com/dein-profil)
# """)

# # Ein Abschnitt über meine Projekte
# st.header("المشاريع")
# st.write("هنا بعض من مشاريعي الأخيرة:")

# # Projekt 1
# st.subheader("المشروع 1: تحليل البيانات باستخدام بايثون")
# st.write("""
# **الوصف:** في هذا المشروع، قمت بتحليل البيانات وتصويرها للحصول على رؤى مهمة.
# - **التقنيات المستخدمة:** Python, Matplotlib, Pandas
# - **Github:** [رابط للمستودع](https://github.com/dein-profil/projekt1)
# """)

# # Projekt 2
# st.subheader("المشروع 2: تطبيق ويب باستخدام Streamlit")
# st.write("""
# **الوصف:** هذا المشروع هو تطبيق ويب بسيط قمت بتطويره باستخدام Streamlit.
# - **التقنيات المستخدمة:** Python, Streamlit
# - **Github:** [رابط للمستودع](https://github.com/dein-profil/projekt2)
# """)

# # Ein Bild hinzufügen
# st.header("المعرض")
# st.image("images/profile_image.PNG", caption="صورة من مشروعي الأخير")

# # Ein einfacher Interaktivitäts-Abschnitt
# st.header("التفاعل")
# name = st.text_input("ما اسمك؟")
# if name:
#     st.write(f"مرحبًا، {name}! سعيد بوجودك هنا.")

# # Einfache Datenvisualisierung
# st.header("تصور البيانات")
# import numpy as np
# import pandas as pd

# # Beispieldaten
# data = pd.DataFrame({
#     'A': np.random.randn(100),
#     'B': np.random.randn(100),
#     'C': np.random.randn(100)
# })

# st.line_chart(data)

# # Zusätzlicher Abschnitt über Fähigkeiten und Erfahrung
# st.header("المهارات والخبرات")
# st.write("""
# أنا مهندس ميكاترونيك، أتمتع بخبرة واسعة ومعرفة عميقة في مجالات الهندسة الميكانيكية، والهندسة الكهربائية، وعلوم الحاسوب. أتميز بقدرتي على تصميم وتطوير الأنظمة الميكاترونية والأتمتة، بما في ذلك الروبوتات والماكينات. بفضل معرفتي الواسعة في التحكم الآلي والتصميم الإلكتروني والبرمجة، أستطيع تصميم وتطوير الدوائر الإلكترونية وأنظمة تحكم المحركات والمستشعرات والمشغلات. كما أن لدي خبرة في استخدام برامج النمذجة والمحاكاة الهندسية لتصميم واختبار الأنظمة الميكانيكية والكهربائية بكفاءة.

# بالإضافة إلى ذلك، أتمتع بمهارات في تصميم صفحات الويب وتطبيقات الأجهزة المحمولة باستخدام Flutter. أستطيع تصميم وتطوير تطبيقات جذابة وتفاعلية تتوافق مع معايير التصميم الحديثة وتستجيب بشكل ممتاز على مختلف الأجهزة المحمولة والحواسب الشخصية. أنا ملم بأحدث التقنيات في تصميم التطبيقات وأسعى باستمرار لتطوير مهاراتي في هذا المجال.

# أخيرًا، أنا ملتزم بتحسين وتطوير مهاراتي باستمرار، والابتكار والبحث عن حلول جديدة للمساهمة في تقدم المجال. أنا مستعد للعمل بجد، وتحمل المسؤولية، والعمل ضمن فريق متكامل لتحقيق الأهداف المشتركة.
# """)

# # تذييل الصفحة
# st.markdown("---")
# st.write("شكرًا لزيارتك! تابعني على [لينكدإن](https://www.linkedin.com/in/dein-profil) و [جيت هب](https://github.com/dein-profil).")

# # بدء تطبيق Streamlit
# if __name__ == "__main__":
#     st.write("التطبيق يعمل...")

import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]

# Configure the Generative AI with API key (no direct SSL context support)
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Your Streamlit UI setup
col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Mohammed Alattas")

with col2:
    st.image("images/profile_image.PNG")

st.title(" ")

persona = """
    You are Mohammed AI bot. You help people answer questions about yourself (i.e Mohammed)
    Answer as if you are responding. Don't answer in second or third person.
    If you don't know the answer, you simply say "That's a secret."
    Here is more info about Mohammed: 
    
    Mohammed Alattas is an Educator/Entrepreneur in the field of Computer Vision and Robotics.
    Mohammed obtained his Bachelor’s degree in
    Mechatronics and later specialized in the field of Robotics. Prior to starting his entrepreneurial career, 
    Mohammed worked as a university lecturer and a design engineer, evaluating 
    and developing rapid prototypes of US patents.

    Mohammed's Email: contact@Mohammedalattas.com 
    Mohammed's Facebook: https://www.facebook.com/Mohammedsworkshop
    Mohammed's Instagram: https://www.instagram.com/Mohammedsworkshop/
    Mohammed's LinkedIn: https://www.linkedin.com/in/Mohammed-alattas-8045b38a/
    Mohammed's Github :https://github.com/Mohammedalattas
    """

st.title("Mohammed's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona +"Here is the question that the user asked: " +  user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

st.title(" ")

st.title("My Setup")
# st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

st.write(" ")
st.title("Gallery")

col1, col2, col3 = st.columns(3)

# with col1:
#     st.image("images/g1.jpg")
#     st.image("images/g2.jpg")
#     st.image("images/g3.jpg")

# with col2:
#     st.image("images/g4.jpg")
#     st.image("images/g5.jpg")
#     st.image("images/g6.jpg")

# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")
#     st.image("images/g9.jpg")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at:")
st.subheader("contact@Mohammedhassan.com")
