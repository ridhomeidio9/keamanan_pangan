import streamlit as st
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Food Nutrition Analyzer", layout="wide")

# Header
st.markdown("""
    <div style='text-align: center;'>
        <h1 style='color: #1E90FF;'>Food Nutrition Analyzer</h1>
        <h4 style='color: #555;'>Cari tahu nilai gizi dari makanan favoritmu!</h4>
    </div>
    <hr>
""", unsafe_allow_html=True)

# Sidebar - Menu
menu = st.sidebar.radio("Menu", ["Beranda", "Analisis Gizi", "Tentang Gizi", "Kontak"])

# Function to simulate nutrition API (mock data)
def get_nutrition_info(food_name):
    # Normally you'd call an API like Edamam or USDA here
    mock_data = {
        "nasi goreng": {"Kalori": 250, "Protein": 6, "Lemak": 10, "Karbohidrat": 35},
        "ayam bakar": {"Kalori": 300, "Protein": 25, "Lemak": 20, "Karbohidrat": 0},
        "salad": {"Kalori": 120, "Protein": 2, "Lemak": 7, "Karbohidrat": 10},
        "burger": {"Kalori": 500, "Protein": 20, "Lemak": 30, "Karbohidrat": 45}
    }
    return mock_data.get(food_name.lower(), None)

# Beranda
if menu == "Beranda":
    st.image("https://images.unsplash.com/photo-1565958011703-44f9829ba187", use_column_width=True)
    st.markdown("""
        ### Apa itu Food Nutrition Analyzer?
        Ini adalah aplikasi sederhana untuk menganalisis kandungan nutrisi makanan.
        Cukup masukkan nama makanan dan lihat informasi gizinya!
    """)

# Analisis Gizi
elif menu == "Analisis Gizi":
    st.subheader("Masukkan Nama Makanan")
    food_input = st.text_input("Contoh: nasi goreng, ayam bakar, salad, burger")

    if food_input:
        nutrition = get_nutrition_info(food_input)
        if nutrition:
            st.success(f"Informasi gizi untuk: {food_input.title()}")
            df = pd.DataFrame(nutrition.items(), columns=["Nutrisi", "Jumlah"])

            col1, col2 = st.columns(2)
            with col1:
                st.table(df)

            with col2:
                fig, ax = plt.subplots()
                sns.barplot(data=df, x="Nutrisi", y="Jumlah", palette="Blues_d", ax=ax)
                ax.set_ylabel("Jumlah (gram atau kcal)")
                st.pyplot(fig)
        else:
            st.error("Maaf, makanan tidak ditemukan di database.")

# Tentang Gizi
elif menu == "Tentang Gizi":
    st.subheader("Pentingnya Mengetahui Nutrisi")
    st.markdown("""
        Mengetahui kandungan nutrisi dalam makanan membantu kita menjaga pola makan sehat,
        menghindari penyakit kronis, dan menjaga berat badan ideal. Nutrisi utama yang harus diperhatikan:

        - **Kalori**: Total energi dari makanan
        - **Protein**: Penting untuk membangun otot dan jaringan
        - **Lemak**: Sumber energi, tapi harus dikontrol
        - **Karbohidrat**: Sumber energi utama tubuh
    """)
    st.image("https://images.unsplash.com/photo-1604908177522-4a3b891cfc2c", use_column_width=True)
