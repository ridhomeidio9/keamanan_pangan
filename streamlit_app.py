st.title("Keamanan Pangan")

# Deskripsi pembuka
st.markdown("""
Selamat datang di aplikasi edukasi **Keamanan Pangan**!  
Di sini kamu akan belajar tentang:
- Bahaya mikrobiologis dalam makanan
- Bahan kimia berbahaya
- Cara penyimpanan makanan yang benar
""")

# Navigasi konten
menu = st.sidebar.selectbox(
    "Pilih topik edukasi:",
    ["Bahaya Mikrobiologis", "Bahan Kimia Berbahaya", "Cara Penyimpanan Makanan"]
)

# Konten: Bahaya Mikrobiologis
if menu == "Bahaya Mikrobiologis":
    st.header("Bahaya Mikrobiologis")
    st.image("https://cdn.pixabay.com/photo/2016/05/19/17/37/bacteria-1403984_1280.jpg", use_column_width=True)
    st.markdown("""
    Mikroorganisme seperti bakteri, virus, dan parasit bisa mencemari makanan dan menyebabkan penyakit.  
    Beberapa contoh mikroorganisme berbahaya:
    
    - **Salmonella** – sering ditemukan pada telur mentah dan daging ayam.
    - **E. coli** – bisa berasal dari daging sapi yang tidak dimasak sempurna.
    - **Listeria** – dapat tumbuh dalam makanan dingin seperti keju lunak dan daging siap saji.
    
    **Pencegahan:**
    - Cuci tangan sebelum memasak.
    - Masak makanan hingga suhu internal aman.
    - Jangan mencampur makanan mentah dan matang.
    """)

# Konten: Bahan Kimia Berbahaya
elif menu == "Bahan Kimia Berbahaya":
    st.header("Bahan Kimia Berbahaya")
    st.image("https://cdn.pixabay.com/photo/2015/01/08/18/24/laboratory-593359_1280.jpg", use_column_width=True)
    st.markdown("""
    Beberapa bahan kimia dapat masuk ke dalam makanan dan membahayakan kesehatan, seperti:
    
    - **Pestisida** – pada buah dan sayuran yang tidak dicuci bersih.
    - **Boraks dan Formalin** – kadang digunakan secara ilegal untuk mengawetkan makanan.
    - **Pewarna tekstil** – digunakan tidak sesuai peruntukan.

    **Cara menghindari:**
    - Cuci buah dan sayur sebelum dikonsumsi.
    - Beli produk dari produsen terpercaya.
    - Waspadai makanan dengan warna mencolok atau aroma menyengat.
    """)

# Konten: Cara Penyimpanan Makanan
elif menu == "Cara Penyimpanan Makanan":
    st.header("Cara Penyimpanan Makanan yang Benar")
    st.image("https://cdn.pixabay.com/photo/2016/03/05/19/02/fridge-1234658_1280.jpg", use_column_width=True)
    st.markdown("""
    Penyimpanan makanan yang tidak tepat bisa mempercepat pembusukan dan meningkatkan risiko kontaminasi.

    **Tips penyimpanan:**
    - Simpan makanan pada suhu yang sesuai (contoh: di bawah 4°C untuk makanan dingin).
    - Gunakan wadah tertutup untuk menghindari kontaminasi silang.
    - Labeli makanan dengan tanggal simpan untuk menghindari konsumsi makanan basi.
    - Jangan menyimpan makanan panas langsung di kulkas — biarkan dingin terlebih dahulu.

    **Ingat:** FIFO (First In, First Out) – gunakan makanan yang lebih lama disimpan terlebih dahulu.
    """)

# Footer
st.markdown("---")
st.markdown("🧼 Jaga kebersihan, pilih makanan aman, dan simpan dengan benar untuk hidup yang lebih sehat.")
