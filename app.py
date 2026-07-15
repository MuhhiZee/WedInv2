import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Undangan Pernikahan",
    page_icon="💍",
    layout="wide"
)

# --- FUNGSI MERENDER GAMBAR LATAR (BACKGROUND) VIA CSS ---
def set_bg_from_local(image_file):
    try:
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        # Menyisipkan kustomisasi gambar latar belakang pada selector utama .stApp milik Streamlit
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0.8)), url("data:image/jpg;base64,{encoded_string}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass

# Mengaplikasikan gambar latar belakang (pastikan file 'images/background.jpg' tersedia)
set_bg_from_local("images/background.jpg")

# Load CSS Eksternal Tambahan
def load_css():
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        pass

load_css()

# Ambil nama tamu dari URL
guest = st.query_params.get("to", "Tamu Undangan")


# --- SISTEM LOCK UNDANGAN (SESSION STATE) ---
if "terbuka" not in st.session_state:
    st.session_state.terbuka = False

def buka_undangan():
    st.session_state.terbuka = True


# ====================================================================
# TAMPILAN 1: JIKA UNDANGAN BELUM DIBUKA (SAMPUL AWAL TERKUNCI ELEGAN)
# ====================================================================
if not st.session_state.terbuka:
    st.markdown(
        """
        <div style='text-align: center; padding: 120px 20px; font-family: "Playfair Display", serif; background: rgba(255,255,255,0.9); border-radius: 15px; box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1); backdrop-filter: blur(5px); border: 1px solid rgba(255, 255, 255, 0.3); max-width: 600px; margin: auto;'>
            <h3 style='color: #8A7355; font-weight: 300; letter-spacing: 3px; font-size: 1.1rem; text-transform: uppercase;'>The Wedding Of</h3>
            <h1 style='font-size: 3.8rem; color: #C79A5D; margin: 20px 0; font-family: "Great Vibes", cursive;'>Andi & Siti</h1>
            <hr style='border: 0; height: 1px; background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(199, 154, 93, 0.75), rgba(0, 0, 0, 0)); margin: 30px 0;'>
            <p style='color: #666; font-size: 1.1rem; font-style: italic;'>Kepada Yth. Bapak/Ibu/Saudara/i:</p>
            <h2 style='color: #333; margin: 15px 0 40px 0; font-weight: 600; letter-spacing: 1px;'>{guest}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Tombol Pembuka Undangan Resmi
    st.button("💌 Buka Undangan", on_click=buka_undangan, use_container_width=True)


# ====================================================================
# TAMPILAN 2: JIKA UNDANGAN SUDAH DIBUKA (ISI UTAMA + MUSIK)
# ====================================================================
else:
    # --- PROSES AUTO-PLAY AUDIO VIA INTERAKSI ---
    audio_file = "musik/wedding.mp3"
    try:
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        
        # Komponen audio diletakkan di bagian atas agar langsung terpicu
        st.audio(audio_bytes, format="audio/mp3", autoplay=True, loop=True)
    except FileNotFoundError:
        # Jika file lokal eror/0:00, gunakan jalur fallback URL online otomatis agar musik tetap bunyi
        st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True, loop=True)

    # --- KONTEN UTAMA UNDANGAN DENGAN CLASS CSS ---
    st.markdown(
        """
        <div class='cover' style='text-align: center; padding: 40px 0;'>
            <h3 style='color: #8A7355; letter-spacing: 2px;'>The Wedding Of</h3>
            <h1 style='color: #C79A5D; font-size: 4rem; font-family: "Great Vibes", cursive; margin: 10px 0;'>Andi & Siti</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Mempelai
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("images/groom.jpg", width=250)
        st.subheader("Andi Pratama")
        st.write("Putra Pertama dari")
        st.write("Bapak Ahmad & Ibu Nur")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.image("images/bride.jpg", width=250)
        st.subheader("Siti Rahma")
        st.write("Putri Pertama dari")
        st.write("Bapak Yusuf & Ibu Aminah")
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # Jadwal Acara
    st.header("📅 Akad Nikah")
    st.info("""
    Hari : Minggu
    Tanggal : 20 Desember 2026
    Pukul : 09.00 WIB
    Lokasi : Gedung Serbaguna Makassar
    """)

    st.header("🎉 Resepsi")
    st.success("""
    Hari : Minggu
    Tanggal : 20 Desember 2026
    Pukul : 11.00 WIB
    Lokasi : Gedung Serbaguna Makassar
    """)

    st.divider()

    # Countdown
    st.header("⏳ Countdown")
    st.markdown(
        """
        <h2 style='text-align:center; color:#C79A5D; font-size: 2.5rem; letter-spacing: 2px;'>
        20 Desember 2026
        </h2>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Galeri Foto
    st.header("📸 Galeri")
    cols = st.columns(3)
    gallery = ["images/gallery1.jpg", "images/gallery1.jpg", "images/gallery1.jpg"]

    for col, img in zip(cols, gallery):
        with col:
            st.image(img)

    st.divider()

    # Peta Lokasi
    st.header("📍 Lokasi")
    st.components.v1.html("""
    <iframe
    src="https://google.com"
    width="100%" height="400" style="border:0; border-radius:10px; box-shadow: 0 4px 15px rgba(0,0,0,0.1);" loading="lazy">
    </iframe>
    """, height=420)

    st.divider()

    # RSVP Form
    st.header("💌 RSVP")
    nama = st.text_input("Nama")
    kehadiran = st.selectbox("Konfirmasi Kehadiran", ["Hadir", "Tidak Hadir", "Masih Ragu"])
    pesan = st.text_area("Ucapan")

    if st.button("Kirim"):
        st.success("Terima kasih atas konfirmasinya!")

    st.divider()

    # Hadiah Digital
    st.header("🎁 Wedding Gift")
    st.code("BCA\n1234567890\n\na.n Andi Pratama")
    st.caption("Terima kasih atas doa dan restunya ❤️")
