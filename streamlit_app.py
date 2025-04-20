import streamlit as st
from PIL import Image
import base64

# Set page config
st.set_page_config(page_title="Edukasi Keamanan Pangan", layout="wide")

# Helper to set background
def set_bg_hack(main_bg):
    main_bg_ext = "png"

    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )

# Optional: Uncomment to add background image
# set_bg_hack("background.png")

# Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #2E8B57;'>Edukasi Keamanan Pangan</h1>
        <h4 style='color: #555;'>Mari kita pelajari pentingnya menjaga keamanan makanan untuk kesehatan kita</h4>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.radio("Navigasi", ["Beranda", "Apa itu Keamanan Pangan?", "Tips Aman Konsumsi", "Kuis Interaktif"])

# Page Content
if menu == "Beranda":
    col1, col2 = st.columns(2)

    with col1:
        st.image("https://images.unsplash.com/photo-1606787366850-de6330128bfc", caption="Ilustrasi Keamanan Pangan", use_column_width=True)

    with col2:
        st.subheader("Mengapa Keamanan Pangan Penting?")
        st.write("""
            Keamanan pangan adalah kondisi dan upaya yang diperlukan untuk mencegah makanan dari bahaya biologis, kimia, dan fisik
            yang dapat membahayakan kesehatan konsumen. Penting untuk memahami cara menyimpan, mengolah, dan mengonsumsi makanan
            dengan aman agar terhindar dari penyakit bawaan makanan.
        ""
        )

elif menu == "Apa itu Keamanan Pangan?":
    st.subheader("Definisi Keamanan Pangan")
    st.write("""
        Keamanan pangan mencakup semua tindakan yang dilakukan untuk memastikan makanan aman dikonsumsi, mulai dari produksi,
        penyimpanan, hingga penyajian. Ancaman terhadap keamanan pangan bisa datang dari bakteri, virus, kontaminan kimia, dan
        lain-lain. Organisasi seperti WHO dan BPOM menetapkan standar keamanan pangan untuk melindungi kesehatan masyarakat.
    ""
    )
    st.image("https://www.fao.org/images/newsroom/news/2021/1102/FAO_FoodSafety.jpg", use_column_width=True)

elif menu == "Tips Aman Konsumsi":
    st.subheader("Tips Keamanan Pangan di Rumah")
    tips = [
        "1. Cuci tangan sebelum mengolah makanan",
        "2. Pisahkan makanan mentah dan matang",
        "3. Masak makanan hingga matang sempurna",
        "4. Simpan makanan pada suhu yang tepat",
        "5. Periksa tanggal kedaluwarsa sebelum konsumsi"
    ]
    for tip in tips:
        st.success(tip)

    st.markdown("**Video Edukasi:**")
    st.video("https://www.youtube.com/watch?v=USe3fWy2CqU")

elif menu == "Kuis Interaktif":
    st.subheader("Kuis Keamanan Pangan")

    score = 0

    with st.expander("1. Mengapa penting mencuci tangan sebelum mengolah makanan?"):
        q1 = st.radio("", [
            "A. Agar tangan wangi",
            "B. Mencegah kontaminasi makanan",
            "C. Kebiasaan saja",
            "D. Tidak penting"
        ])
        if q1 == "B. Mencegah kontaminasi makanan":
            score += 1

    with st.expander("2. Apa yang harus dilakukan pada makanan mentah dan matang?"):
        q2 = st.radio("", [
            "A. Disimpan bersama",
            "B. Dimasak bersamaan",
            "C. Dipisahkan agar tidak saling mencemari",
            "D. Didinginkan saja"
        ])
        if q2 == "C. Dipisahkan agar tidak saling mencemari":
            score += 1

    with st.expander("3. Apa yang harus dilakukan jika makanan sudah kedaluwarsa?"):
        q3 = st.radio("", [
            "A. Dibuang",
            "B. Dicoba sedikit",
            "C. Diberikan ke hewan",
            "D. Disimpan di kulkas"
        ])
        if q3 == "A. Dibuang":
            score += 1

    if st.button("Lihat Skor"):
        st.info(f"Skor kamu: {score}/3")
        if score == 3:
            st.balloons()
            st.success("Hebat! Kamu sangat paham tentang keamanan pangan.")
        elif score == 2:
            st.warning("Bagus! Tapi masih ada yang bisa dipelajari.")
        else:
            st.error("Yuk, pelajari lagi tentang keamanan pangan!")
