import streamlit as st

# =====================================
# KONFIGURASI HALAMAN
# =====================================

st.set_page_config(
    page_title="Kalkulator FPB & KPK",
    page_icon="🧮",
    layout="wide"
)

# =====================================
# TEMA RAINBOW
# =====================================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #ff0000,
        #ff7f00,
        #ffff00,
        #00ff00,
        #00ffff,
        #0000ff,
        #8b00ff
    );
}

h1{
    text-align:center;
    color:white;
    text-shadow:3px 3px 10px black;
}

h2,h3{
    color:white;
    text-shadow:2px 2px 5px black;
}

p{
    color:black;
    font-weight:500;
}

.stButton > button{
    width:100%;
    height:60px;
    border-radius:20px;
    border:none;
    font-size:20px;
    font-weight:bold;
    color:white;

    background:linear-gradient(
        90deg,
        red,
        orange,
        yellow,
        green,
        cyan,
        blue,
        violet
    );
}

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        red,
        orange,
        yellow,
        green,
        cyan,
        blue,
        violet
    );
}

</style>
""", unsafe_allow_html=True)

# =====================================
# FUNGSI FPB
# =====================================

def hitung_fpb(a, b):

    langkah = []

    while b != 0:

        q = a // b
        r = a % b

        langkah.append({
            "a": a,
            "b": b,
            "q": q,
            "r": r
        })

        a, b = b, r

    return a, langkah

# =====================================
# SIDEBAR
# =====================================

with st.sidebar:

    st.title("📚 Materi")

    st.info("""
Materi yang digunakan:

✅ FPB

✅ KPK

✅ Algoritma Euclid

✅ Relatif Prima
""")

# =====================================
# JUDUL
# =====================================

st.title("🌈🧮 KALKULATOR FPB & KPK 🌈")

st.markdown("""
### Menggunakan Algoritma Euclid

Masukkan dua bilangan.
""")

# =====================================
# INPUT
# =====================================

col1, col2 = st.columns(2)

with col1:
    a = st.number_input(
        "Bilangan Pertama",
        min_value=1,
        step=1
    )

with col2:
    b = st.number_input(
        "Bilangan Kedua",
        min_value=1,
        step=1
    )

# =====================================
# TOMBOL HITUNG
# =====================================

if st.button("🧮 Hitung"):

    a = int(a)
    b = int(b)

    fpb, langkah = hitung_fpb(a, b)

    kpk = abs(a * b) // fpb

    # =================================
    # HASIL
    # =================================

    st.markdown("---")

    st.subheader("📊 Hasil Perhitungan")

    col1, col2 = st.columns(2)

    with col1:
        st.success(f"🟢 FPB = {fpb}")

    with col2:
        st.success(f"🟣 KPK = {kpk}")

    if fpb == 1:

        st.success(
            "✨ Kedua bilangan merupakan bilangan relatif prima karena FPB = 1."
        )

    else:

        st.warning(
            "⚠️ Kedua bilangan bukan bilangan relatif prima karena FPB ≠ 1."
        )

    # =================================
    # LANGKAH EUCLID
    # =================================

    st.markdown("---")

    st.subheader("📖 Langkah Algoritma Euclid")

    for i, item in enumerate(langkah, start=1):

        st.markdown(f"### Langkah {i}")

        st.write(f"Bilangan yang dibagi = {item['a']}")
        st.write(f"Bilangan pembagi = {item['b']}")
        st.write(f"Hasil bagi = {item['q']}")
        st.write(f"Sisa = {item['r']}")

        st.latex(
            f"{item['a']} = {item['q']} \\times {item['b']} + {item['r']}"
        )

        if item["r"] != 0:

            st.info(
                f"Karena sisa pembagian masih bernilai {item['r']}, maka proses dilanjutkan dengan pasangan bilangan ({item['b']}, {item['r']})."
            )

        else:

            st.success(
                "Karena sisa pembagian sudah bernilai 0, proses Algoritma Euclid selesai."
            )

        st.markdown("---")

    # =================================
    # MENENTUKAN FPB
    # =================================

    st.subheader("🎯 Menentukan FPB")

    st.write(
        "FPB ditentukan dengan menerapkan Algoritma Euclid hingga diperoleh sisa pembagian bernilai 0."
    )

    x = a
    y = b

    while y != 0:

        st.write(
            f"FPB({x}, {y}) → FPB({y}, {x % y})"
        )

        x, y = y, x % y

    st.success(
        f"Hasil FPB (Faktor Persekutuan Terbesar) menggunakan Algoritma Euclid diperoleh dari sisa pembagian terakhir sebelum diperoleh sisa 0, yaitu {fpb}."
    )

    # =================================
    # MENENTUKAN KPK
    # =================================

    st.markdown("---")

    st.subheader("🎯 Menentukan KPK")

    st.write(
        "Setelah memperoleh FPB, KPK dapat dihitung menggunakan rumus berikut:"
    )

    st.latex(
        r"KPK(a,b)=\frac{a\times b}{FPB(a,b)}"
    )

    st.write("Substitusi nilai:")

    st.latex(
        rf"KPK({a},{b})=\frac{{{a}\times{b}}}{{{fpb}}}"
    )

    st.latex(
        rf"=\frac{{{a*b}}}{{{fpb}}}"
    )

    st.latex(
        rf"={kpk}"
    )

    st.success(
        f"Jadi KPK({a},{b}) = {kpk}"
    )

    # =================================
    # INFORMASI TAMBAHAN
    # =================================

    st.markdown("---")

    st.subheader("🧠 Informasi Bilangan")

    if a % 2 == 0:
        st.write(f"🔵 {a} adalah bilangan genap.")
    else:
        st.write(f"🟠 {a} adalah bilangan ganjil.")

    if b % 2 == 0:
        st.write(f"🔵 {b} adalah bilangan genap.")
    else:
        st.write(f"🟠 {b} adalah bilangan ganjil.")

    st.info(
        f"FPB dari {a} dan {b} adalah {fpb}."
    )

    st.info(
        f"KPK dari {a} dan {b} adalah {kpk}."
    ). coba ubah kode nya biar tema nya soft blue tapi elemennya collorful,
