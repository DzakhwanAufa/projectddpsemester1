# MODULE
import streamlit as st
import time

# function: pembantu perhitungan
def hitung_jarak(kecepatan, waktu):
    """Menghitung Jarak (J) = Kecepatan (K) * Waktu (W)"""
    return kecepatan * waktu

def hitung_kecepatan(jarak, waktu):
    """Menghitung Kecepatan (K) = Jarak (J) / Waktu (W)"""
    # logika: pencegahan pembagian dengan nol
    if waktu == 0:
        return None
    return jarak / waktu

def hitung_waktu(jarak, kecepatan):
    """Menghitung Waktu (W) = Jarak (J) / Kecepatan (K)"""
    # logika: pencegahan pembagian dengan nol
    if kecepatan == 0:
        return None
    return jarak / kecepatan

def Progressbar():
    st.info("Proses perhitungan...")
    progress_bar = st.progress(0)
    
    # looping: menggunakan perulangan for untuk progress bar
    for persen in range(100):
        time.sleep(0.005) 
        progress_bar.progress(persen)
    
    progress_bar.empty()
    st.success("Perhitungan selesai!")


# function: fungsi utama aplikasi
def app_jkw():
    # pengaturan halaman
    st.set_page_config(
        page_title="Kalkulator JKW",
        layout="wide"
        )

    st.title("✍️ Aplikasi Perhitungan Jarak, Kecepatan, dan Waktu")
    st.image(
        "https://cdn.discordapp.com/attachments/1446879749178654924/1450484055274688594/rumus_jokowi.jpg?ex=6942b40b&is=6941628b&hm=142fc767821cfc5c59ff2afedeb7e9c6ff0da0509e463248f7f415d141a34b43",
        width=300,
    )
    # sidebar navigasi
    # variabel
    pilihan = st.sidebar.selectbox(
        "Apa yang ingin Anda hitung?",
        ("Jarak (J)", "Kecepatan (K)", "Waktu (W)")
    )

    st.markdown("---")

    # perhitungan jarak (j)
    if pilihan == "Jarak (J)":
        st.header("Hitung Jarak (J)")
        st.latex(r''' J = K \times W ''')

        # input untuk kecepatan dan waktu
        kecepatan = st.number_input(
            "Masukkan Kecepatan (K):",
            min_value=0.0,
            value=60.0,
            step=1.0
        )
        waktu = st.number_input(
            "Masukkan Waktu (W):",
            min_value=0.0,
            value=1.5,
            step=0.1
        )

        if st.button("Hitung Jarak", key="btn_jarak"):
            Progressbar()
            
            # logika: pastikan nilai input sebelum menghitung
            if kecepatan > 0 and waktu > 0:
                hasil = hitung_jarak(kecepatan, waktu)
                st.success(f"Hasil Jarak: {hasil:,.2f} Satuan")
            else:
                st.error("Kecepatan dan Waktu harus lebih besar dari nol.")

    # perhitungan kecepatan (k)
    elif pilihan == "Kecepatan (K)":
        st.header("Hitung Kecepatan (K)")
        st.latex(r''' K = \frac{J}{W} ''')

        # input untuk jarak dan waktu
        jarak = st.number_input(
            "Masukkan Jarak (J):",
            min_value=0.0,
            value=120.0,
            step=1.0
        )
        waktu = st.number_input(
            "Masukkan Waktu (W):",
            min_value=0.0,
            value=2.0,
            step=0.1
        )

        if st.button("Hitung Kecepatan", key="btn_kecepatan"):
            Progressbar()
            
            # logika: cek apakah waktu bukan 0
            hasil = hitung_kecepatan(jarak, waktu)
            if hasil is not None:
                st.success(f"### Hasil Kecepatan: {hasil:,.2f} Satuan/Satuan")
            else:
                st.error("Waktu (W) tidak boleh nol.")

    # perhitungan waktu (w)
    elif pilihan == "Waktu (W)":
        st.header("Hitung Waktu (W)")
        st.latex(r''' W = \frac{J}{K} ''')

        # input jarak dan kecepatan
        jarak = st.number_input(
            "Masukkan Jarak (J):",
            min_value=0.0,
            value=180.0,
            step=1.0
        )
        kecepatan = st.number_input(
            "Masukkan Kecepatan (K):",
            min_value=0.0,
            value=90.0,
            step=1.0
        )

        if st.button("Hitung Waktu", key="btn_waktu"):
            Progressbar()

            # logika: cek apakah kecepatan bukan 0
            hasil = hitung_waktu(jarak, kecepatan)
            if hasil is not None:
                st.success(f"### Hasil Waktu: {hasil:,.2f} Satuan")
            else:
                st.error("Kecepatan (K) tidak boleh nol.")

    st.sidebar.header("Aplikasi Ini Dibuat Oleh :")
    st.sidebar.caption("Widi Amanda Putri. H : 0110125145")
    st.sidebar.caption("Desyfa Intania Rahlina : 0110125148")
    st.sidebar.caption("Dzakhwan Aufa Saif : 0110125149")

# menjalankan fungsi utama aplikasi
if __name__ == '__main__':

    app_jkw()




