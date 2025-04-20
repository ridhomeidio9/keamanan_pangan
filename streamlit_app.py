import streamlit as st

# Judul halaman
st.set_page_config(page_title="Keamanan Pangan", layout="centered")

st.title("🛡️ Keamanan Pangan")
st.markdown("""
Selamat datang di aplikasi edukasi **Keamanan Pangan**!  
Di sini, kamu akan belajar mengenai berbagai aspek penting dalam menjaga makanan tetap aman untuk dikonsumsi.
""")

# Menu navigasi
menu = st.sidebar.selectbox(
    "Pilih topik edukasi",
    ["Bahaya Mikrobiologis", "Bahan Kimia Berbahaya", "Penyimpanan Makanan yang Benar"]
)

# Konten Bahaya Mikrobiologis
if menu == "Bahaya Mikrobiologis":
    st.header("🔬 Bahaya Mikrobiologis")
    st.markdown("""
Mikroorganisme seperti bakteri, virus, dan jamur dapat mencemari makanan dan menyebabkan penyakit.

**Contoh mikroorganisme berbahaya:**
- *Salmonella*: Menyebabkan keracunan makanan dari telur mentah atau daging yang kurang matang.
- *E. coli*: Ditemukan pada daging yang tidak dimasak sempurna dan produk susu yang tidak dipasteurisasi.
- *Listeria*: Bisa tumbuh pada makanan dingin seperti keju lunak dan makanan siap saji.

**Pencegahan:**
- Masak makanan hingga suhu yang tepat.
- Cuci tangan dan peralatan masak dengan bersih.
- Simpan makanan dengan suhu yang sesuai.
""")

# Konten Bahan Kimia Berbahaya
elif menu == "Bahan Kimia Berbahaya":
    st.header("☣️ Bahan Kimia Berbahaya dalam Makanan")
    st.markdown("""
Bahan kimia dapat masuk ke dalam makanan secara sengaja atau tidak sengaja.

**Contoh bahan kimia berbahaya:**
- **Pestisida berlebih** pada buah dan sayur.
- **Formalin** sebagai pengawet ilegal untuk tahu, ikan, atau mie.
- **Boraks** yang biasa disalahgunakan pada makanan seperti bakso atau kerupuk.

**Cara menghindari:**
- Cuci buah dan sayuran dengan air mengalir.
- Beli makanan dari produsen terpercaya.
- Hindari makanan dengan warna mencolok atau tekstur tidak wajar.
""")

# Konten Penyimpanan Makanan
elif menu == "Penyimpanan Makanan yang Benar":
    st.header("🥶 Penyimpanan Makanan yang Benar")
    st.markdown("""
Penyimpanan makanan yang tepat mencegah pertumbuhan mikroba dan memperpanjang umur simpan.

**Tips penyimpanan:**
- Simpan makanan cepat saji di kulkas (≤ 4°C).
- Bekukan daging mentah jika tidak segera digunakan.
- Gunakan wadah tertutup agar makanan tidak terkontaminasi.
- Labeli makanan dengan tanggal simpan agar tidak lupa kapan harus digunakan.
- Jangan menyimpan makanan panas langsung ke dalam kulkas, biarkan dingin terlebih dahulu.

**Ingat!** Penyimpanan yang salah dapat membuat makanan cepat rusak dan berbahaya untuk dikonsumsi.
""")

# Footer
st.markdown("---")
st.markdown("🧠 **Edukasi ini bertujuan untuk meningkatkan kesadaran akan pentingnya keamanan pangan bagi kesehatan.**")
