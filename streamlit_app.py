import streamlit as st

# Konfigurasi halaman
st.set_page_config(page_title="Keamanan Pangan", page_icon="🛡️", layout="centered")

# CSS custom untuk tampilan lebih estetik
st.markdown("""
    <style>
    .title-style {
        background-color: #4CAF50;
        color: white;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .section-title {
        font-size: 24px;
        margin-top: 20px;
        color: #4CAF50;
        font-weight: bold;
    }
    .content-box {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-bottom: 20px;
    }
    ul {
        padding-left: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title-style">🛡️ Keamanan Pangan</div>', unsafe_allow_html=True)

st.markdown("""
Selamat datang di aplikasi edukasi **Keamanan Pangan**.  
Yuk pelajari bagaimana menjaga makanan tetap aman dan sehat!
""")

# Sidebar menu
menu = st.sidebar.radio(
    "📚 Pilih Topik Edukasi",
    ["Bahaya Mikrobiologis", "Bahan Kimia Berbahaya", "Penyimpanan Makanan yang Benar"]
)

# Konten: Bahaya Mikrobiologis
if menu == "Bahaya Mikrobiologis":
    st.markdown('<div class="section-title">🔬 Bahaya Mikrobiologis</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="content-box">
        Mikroorganisme seperti bakteri, virus, dan jamur dapat mencemari makanan dan menyebabkan penyakit serius.<br><br>

        <b>Contoh mikroorganisme berbahaya:</b>
        <ul>
            <li><b>Salmonella</b>: dari telur mentah & daging kurang matang</li>
            <li><b>E. coli</b>: pada daging tidak matang & susu tidak dipasteurisasi</li>
            <li><b>Listeria</b>: pada keju lunak & makanan siap saji</li>
        </ul>

        <b>Langkah pencegahan:</b>
        <ul>
            <li>✅ Masak makanan hingga suhu aman</li>
            <li>✅ Cuci tangan & alat masak secara bersih</li>
            <li>✅ Simpan makanan pada suhu yang sesuai</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# Konten: Bahan Kimia Berbahaya
elif menu == "Bahan Kimia Berbahaya":
    st.markdown('<div class="section-title">☣️ Bahan Kimia Berbahaya</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown("""
        <div class="content-box">
        Bahan kimia dapat masuk ke makanan secara sengaja atau tidak sengaja. Jika berlebihan, bisa berbahaya bagi tubuh.<br><br>

        <b>Contoh bahan kimia berbahaya:</b>
        <ul>
            <li><b>Pestisida</b> berlebih pada buah/sayur</li>
            <li><b>Formalin</b> sebagai pengawet ilegal (pada tahu, ikan)</li>
            <li><b>Boraks</b> pada bakso atau kerupuk</li>
        </ul>

        <b>Cara menghindari:</b>
        <ul>
            <li>🧼 Cuci buah & sayuran dengan air bersih</li>
            <li>🛒 Beli dari tempat terpercaya</li>
            <li>⚠️ Hindari makanan dengan warna mencolok atau tekstur aneh</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# Konten: Penyimpanan Makanan
elif menu == "Penyimpanan Makanan yang Benar":
    st.markdown('<div class="section-title">🥶 Penyimpanan Makanan yang Benar</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 1.2])
    with col1:
        st.image("https://cdn.pixabay.com/photo/2017/04/26/10/39/refrigerator-2263584_1280.jpg", use_column_width=True)
    with col2:
        st.markdown("""
        <div class="content-box">
        Penyimpanan makanan yang tepat menjaga kualitas & mencegah pertumbuhan mikroorganisme.<br><br>

        <b>Tips penting:</b>
        <ul>
            <li>📦 Simpan makanan di wadah tertutup</li>
            <li>🧊 Dinginkan makanan cepat saji (≤ 4°C)</li>
            <li>📅 Beri label tanggal simpan</li>
            <li>🔥 Jangan masukkan makanan panas langsung ke kulkas</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.info("📌 Edukasi ini bertujuan untuk meningkatkan kesadaran akan pentingnya keamanan pangan bagi kesehatan.")
st.markdown("<small>© 2025 - Aplikasi Edukasi Keamanan Pangan</small>", unsafe_allow_html=True)
