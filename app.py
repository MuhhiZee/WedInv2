import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Undangan Pernikahan Andi & Siti",
    page_icon="💍",
    layout="wide"
)

# --- FUNGSI MERENDER GAMBAR LATAR (BACKGROUND) VIA CSS ---
def set_bg(desktop_img, mobile_img):
    with open(desktop_img, "rb") as f:
        desktop = base64.b64encode(f.read()).decode()

    with open(mobile_img, "rb") as f:
        mobile = base64.b64encode(f.read()).decode()

    st.markdown(f"""
    <style>

    .stApp {{
        background-image:
            linear-gradient(rgba(255,255,255,.35), rgba(255,255,255,.45)),
            url("data:image/jpeg;base64,{desktop}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    @media (max-width:768px) {{

        .stApp {{
            background-image:
                linear-gradient(rgba(255,255,255,.35), rgba(255,255,255,.45)),
                url("data:image/jpeg;base64,{mobile}");
            background-size: cover;
            background-position: center;
            background-attachment: scroll;
        }}

    }}

    </style>
    """, unsafe_allow_html=True)
    
    #except FileNotFoundError:
    #   st.warning("⚠️ File 'images/background.jpg' tidak ditemukan. Menggunakan warna dasar.")

# Mengaplikasikan gambar latar belakang tema watercolor hijau-emas
set_bg(
    "images/background.jpg",
    "images/background1.jpg"
)

# Load CSS Eksternal
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
# TAMPILAN 1: SAMPUL AWAL TERKUNCI (BLUR GLASS CARD)
# ====================================================================
if not st.session_state.terbuka:
    st.markdown(
        f"""
        <div class="wedding-card">
            <h3 class="title-sub">THE WEDDING OF</h3>
            <h1 class="title-main">Muhaimin & Nabila</h1>
            <div class="wedding-divider"></div>
            <p class="guest-text">Kepada Yth. Bapak/Ibu/Saudara/i:</p>
            <h2 class="guest-name">{guest}</h2>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("💌 Buka Undangan", on_click=buka_undangan, use_container_width=True)


# ====================================================================
# TAMPILAN 2: ISI UTAMA UNDANGAN (AKSESIBEL SETELAH DIKLIK)
# ====================================================================
else:
    # --- KONTEN HEADER UTAMA ---
    st.markdown(
        """
        <div style='text-align: center; padding: 5px 0;'>
            <h3 class="title-sub">THE WEDDING OF</h3>
            <h1 class="title-main" style="font-size: 4.5rem;">Muhaimin & Nabila</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Mempelai
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='mempelai-box'>", unsafe_allow_html=True)
        st.image("images/groom.jpg", width=220)
        st.subheader("Muhaimin")
        st.write("Anak Ke-empat dari")
        st.write("**Bapak Ali & Ibu Nur**")
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='mempelai-box'>", unsafe_allow_html=True)
        st.image("images/bride.jpg", width=220)
        st.subheader("Nabila")
        st.write("Putri Ke-dua dari")
        st.write("**Bapak Yusuf & Ibu Aminah**")
        st.markdown("</div>", unsafe_allow_html=True)

    st.divider()

    # Jadwal Acara
    st.header("📅 Akad Nikah")
    st.info("""
    **Hari** : Minggu  
    **Tanggal** : 20 Desember 2026  
    **Pukul** : 09.00 WIB  
    **Lokasi** : Gedung Serbaguna Makassar
    """)

    st.header("🎉 Resepsi")
    st.success("""
    **Hari** : Minggu  
    **Tanggal** : 20 Desember 2026  
    **Pukul** : 11.00 WIB  
    **Lokasi** : Gedung Serbaguna Makassar
    """)

    st.divider()

    # Countdown
    st.header("⏳ Countdown")
    st.markdown(
        """
        <h2 style='text-align:center; color:#2E5A44; font-family:"Playfair Display", serif; font-size: 2.5rem; letter-spacing: 2px;'>
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
    width="100%" height="400" style="border:0; border-radius:15px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);" loading="lazy">
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

    # --- PROSES AUTO-PLAY AUDIO ---
    audio_file = "music/wed.mp3"
    try:
        with open(audio_file, "rb") as f:
            audio_bytes = f.read()
        st.audio(audio_bytes, format="audio/mp3", start_time=15, autoplay=True, loop=True)
    except FileNotFoundError:
        # Fallback online jika file lokal belum siap/kosong
        st.audio("https://soundhelix.com", format="audio/mp3", autoplay=True, loop=True)

